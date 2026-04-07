```markdown
# TravelBuddy - AI Agent Trợ lý Du lịch Thông minh ✈️🏨

Đây là dự án AI Agent thuộc **Lab 4: Xây dựng AI Agent đầu tiên với LangGraph**. TravelBuddy là một trợ lý ảo thông minh có khả năng giúp người dùng lên kế hoạch chuyến đi, tự động tra cứu chuyến bay, kiểm tra ngân sách, và tìm kiếm khách sạn phù hợp thông qua cơ chế Reasoning and Acting (ReAct) và Tool Calling.

## 🌟 Tính năng nổi bật

* **Multi-Step Tool Chaining:** Agent có khả năng tư duy chuỗi. Ví dụ: Tự động tìm vé máy bay rẻ nhất -> Tính toán số dư -> Dùng số dư đó để tìm khách sạn phù hợp trong ngân sách, tất cả trong một câu lệnh của người dùng.
* **Xử lý Chuyến bay Nối chuyến (Transit):** Thuật toán tìm kiếm nâng cao tự động ghép nối các chặng bay nếu không có chuyến bay thẳng.
* **Trí nhớ Hội thoại (Context Memory):** Sử dụng `MemorySaver` của LangGraph, giúp Agent nhớ được lịch sử trò chuyện (VD: Nhớ điểm đến từ câu trước và điểm đi từ câu sau).
* **Hệ thống Logging Chi tiết:** Ghi vết mọi hoạt động của User, Agent và quá trình thực thi Tools ra Terminal và lưu vào file `logs/system_log` để dễ dàng debug.
* **An toàn (Guardrails):** Tự động từ chối lịch sự các yêu cầu không liên quan đến du lịch (như lập trình, toán học).

## 📁 Cấu trúc thư mục

```text
2A202600164_lab_04/
│
├── src/
│   ├── agent/
│   │   └── agent.py         # Cấu hình LangGraph, LLM (gpt-4o-mini) và Memory
│   ├── tool/
│   │   └── tools.py         # Định nghĩa Custom Tools (Flights, Hotels, Budget)
│   └── telemetry/
│       └── logger.py        # Thiết lập hệ thống ghi log (Console & File)
│
├── logs/                    # (Tự động tạo) Chứa file system_log
├── .env                     # File chứa OPENAI_API_KEY (Không push lên Git)
├── .gitignore               # Cấu hình bỏ qua các file rác/nhạy cảm
├── main.py                  # File chạy chính của ứng dụng
├── system_prompt.txt        # Lưu trữ Persona, Rules và Constraints của Agent
├── test_results.md          # Báo cáo kết quả kiểm thử 5 Test Cases
└── README.md                # Tài liệu hướng dẫn này
```

## 🚀 Hướng dẫn cài đặt và chạy thử nghiệm

### 1. Yêu cầu môi trường
Đảm bảo máy tính của bạn đã cài đặt Python 3.8 trở lên.

### 2. Cài đặt thư viện
Mở Terminal, di chuyển vào thư mục dự án và cài đặt các thư viện cần thiết:
```bash
python -m venv venv
source venv/bin/activate  # (Dành cho Linux/Mac)
# venv\Scripts\activate   # (Dành cho Windows)

pip install langchain langchain-openai langgraph python-dotenv
```

### 3. Cấu hình biến môi trường
Tạo một file `.env` ở thư mục gốc của dự án và thêm OpenAI API Key của bạn:
```env
OPENAI_API_KEY=sk-proj-xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx
```

### 4. Chạy ứng dụng
Khởi động Agent bằng lệnh:
```bash
python main.py
```
Gõ `quit` hoặc `exit` để kết thúc phiên trò chuyện.

## 🧪 Kịch bản Kiểm thử (Test Cases)

Agent đã vượt qua toàn bộ 5 test cases yêu cầu của bài Lab:
1.  **Direct Answer:** Trả lời trực tiếp, hỏi thăm thông tin cơ bản.
2.  **Single Tool Call:** Gọi tool `search_flights` chính xác khi đủ thông tin.
3.  **Multi-Step Tool Chaining:** Tính toán và chia ngân sách phức tạp cho nhiều tool.
4.  **Missing Info:** Chủ động hỏi lại khi thiếu thành phố hoặc ngân sách để đặt phòng.
5.  **Guardrail:** Từ chối giải bài tập Python/toán học thành công.

*Chi tiết kết quả kiểm thử và log hội thoại có thể xem tại file `test_results.md`, `logs/system_log`.*
```

