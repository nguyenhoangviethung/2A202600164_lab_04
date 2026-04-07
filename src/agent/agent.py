import os
from typing import Annotated
from typing_extensions import TypedDict
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import add_messages
from langgraph.prebuilt import ToolNode, tools_condition
from langchain_openai import ChatOpenAI
from langchain_core.messages import SystemMessage
from src.tool.tools import TOOLS
from src.telemetry.logger import get_logger
from dotenv import load_dotenv

load_dotenv()
logger = get_logger("AgentCore")

# Đọc System Prompt
try:
    with open("system_prompt.txt", "r", encoding="utf-8") as f:
        SYSTEM_PROMPT = f.read()
except FileNotFoundError:
    SYSTEM_PROMPT = "Bạn là trợ lý du lịch TravelBuddy thân thiện."
    logger.warning("Không tìm thấy system_prompt.txt, sử dụng prompt mặc định.")

class AgentState(TypedDict):
    messages: Annotated[list, add_messages]

tools_list = TOOLS
llm = ChatOpenAI(model="gpt-4o-mini")
llm_with_tools = llm.bind_tools(tools_list)

def agent_node(state: AgentState):
    messages = state["messages"]
    if not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages
    
    response = llm_with_tools.invoke(messages)
    
    if response.tool_calls:
        for tc in response.tool_calls:
            logger.info(f"🤖 Agent quyết định gọi tool: {tc['name']} với tham số {tc['args']}")
    else:
        logger.info("🤖 Agent trả lời trực tiếp cho khách hàng.")
        
    return {"messages": [response]}

# Xây dựng Graph
builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)

tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

graph = builder.compile()