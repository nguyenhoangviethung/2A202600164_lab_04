from src.agent.agent import graph
from src.telemetry.logger import get_logger
import uuid
logger = get_logger("Main")

def run_chat():
    print("=" * 60)
    print("TravelBuddy - Trợ lý Du lịch Thông minh")
    print("Gõ 'quit' để thoát")
    print("=" * 60)
    
    while True:
        try:
            thread_id = str(uuid.uuid4())
            config = {"configurable": {"thread_id": thread_id}}
            user_input = input("\nBạn: ").strip()
            if not user_input:
                continue
                
            if user_input.lower() in ("quit", "exit", "q"):
                print("Tạm biệt!")
                break
            
            logger.info(f"👤 User input: {user_input}")
            
            # Lấy kết quả từ LangGraph
            result = graph.invoke({"messages": [("human", user_input)]}, config = config)
            final_response = result["messages"][-1].content
            
            print(f"\nTravelBuddy: {final_response}")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            logger.error(f"Lỗi hệ thống: {str(e)}")
            print(f"Có lỗi xảy ra: {e}")

if __name__ == "__main__":
    run_chat()