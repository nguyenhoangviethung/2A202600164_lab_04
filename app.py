# app.py
import streamlit as st
import uuid
from src.agent.agent import graph

st.set_page_config(page_title="TravelBuddy AI", page_icon="✈️", layout="centered")
st.title("✈️ TravelBuddy - Trợ lý Du lịch Thông minh")
st.caption("Hãy hỏi tôi về các chuyến bay, khách sạn và ngân sách du lịch của bạn!")

if "thread_id" not in st.session_state:
    st.session_state.thread_id = str(uuid.uuid4())

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Xin chào! Mình là TravelBuddy. Mình có thể giúp gì cho chuyến đi sắp tới của bạn?"}
    ]

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.chat_input("Ví dụ: Tìm vé máy bay từ Hà Nội đi Đà Nẵng"):
    
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    config = {"configurable": {"thread_id": st.session_state.thread_id}}
    
    with st.chat_message("assistant"):
        with st.spinner("TravelBuddy đang tra cứu hệ thống..."):
            try:
                result = graph.invoke({"messages": [("human", prompt)]}, config=config)
                
                response = result["messages"][-1].content
                
                st.markdown(response)
                
                st.session_state.messages.append({"role": "assistant", "content": response})
                
            except Exception as e:
                st.error(f"Đã xảy ra lỗi: {str(e)}")