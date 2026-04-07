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
from langgraph.checkpoint.memory import MemorySaver

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

from langchain_core.messages import SystemMessage, AIMessage 

def agent_node(state: AgentState):
    messages = state["messages"]
    
    last_message = messages[-1].content.lower()
    
    injection_keywords = [
        "bỏ qua lệnh trên", "ignore previous", "system prompt", 
        "forget all", "quên hết", "you are no longer", 
        "bỏ qua các quy tắc", "xóa db", "drop table", "bỏ qua giới hạn"
    ]
    
    if any(keyword in last_message for keyword in injection_keywords):
        logger.warning(f"🚨 CẢNH BÁO BẢO MẬT: Phát hiện nỗ lực thao túng prompt! Input: {last_message}")
        return {"messages": [AIMessage(content="Cảnh báo an toàn: Yêu cầu của bạn chứa nội dung không hợp lệ hoặc cố gắng thao túng hệ thống. TravelBuddy xin phép từ chối trả lời.")]}
    
    logger.info(f"🧠 Kích thước bộ nhớ hiện tại: {len(messages)} tin nhắn.")
    
    if not isinstance(messages[0], SystemMessage):
        messages = [SystemMessage(content=SYSTEM_PROMPT)] + messages
    
    response = llm_with_tools.invoke(messages)
    
    if response.tool_calls:
        for tc in response.tool_calls:
            logger.info(f"🤖 Agent quyết định gọi tool: {tc['name']} với tham số {tc['args']}")
    else:
        logger.info(f"🤖 Agent trả lời trực tiếp:\n{response.content}")
        
    return {"messages": [response]}

# Xây dựng Graph
builder = StateGraph(AgentState)
builder.add_node("agent", agent_node)

tool_node = ToolNode(tools_list)
builder.add_node("tools", tool_node)

builder.add_edge(START, "agent")
builder.add_conditional_edges("agent", tools_condition)
builder.add_edge("tools", "agent")

memory = MemorySaver()

graph = builder.compile()