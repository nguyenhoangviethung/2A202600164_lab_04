============================================================
TravelBuddy - Trợ lý Du lịch Thông minh
Gõ 'quit' để thoát
============================================================

**Bạn**: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.

2026-04-07 15:39:27 - Main - INFO - 👤 User input: Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu.
2026-04-07 15:39:32 - AgentCore - INFO - 🤖 Agent trả lời trực tiếp cho khách hàng.

TravelBuddy: Chào bạn! Đi du lịch thật tuyệt vời, nhưng để mình có thể tư vấn tốt hơn, bạn có thể cho mình biết ngân sách của bạn cho chuyến đi này không? Và bạn muốn đi đến thành phố nào? 

**Bạn**: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng

2026-04-07 15:39:45 - Main - INFO - 👤 User input: Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng
2026-04-07 15:39:47 - AgentCore - INFO - 🤖 Agent quyết định gọi tool: search_flights với tham số {'origin': 'Hà Nội', 'destination': 'Đà Nẵng'}
2026-04-07 15:39:47 - Tools - INFO - ✈️ Đang thực thi 'search_flights' | Khởi hành: Hà Nội -> Đích: Đà Nẵng
2026-04-07 15:39:47 - Tools - INFO - ✅ Đã tìm thấy 4 chuyến bay.
2026-04-07 15:39:51 - AgentCore - INFO - 🤖 Agent trả lời trực tiếp cho khách hàng.

TravelBuddy: Dưới đây là danh sách chuyến bay từ Hà Nội đi Đà Nẵng:

- **VietJet Air**: 08:30 - 09:50 | Hạng: economy | Giá: 890.000₫
- **Bamboo Airways**: 11:00 - 12:20 | Hạng: economy | Giá: 1.200.000₫
- **Vietnam Airlines**: 06:00 - 07:20 | Hạng: economy | Giá: 1.450.000₫
- **Vietnam Airlines**: 14:00 - 15:20 | Hạng: business | Giá: 2.800.000₫

Nếu bạn cần thêm thông tin về khách sạn hoặc các kế hoạch khác cho chuyến đi, hãy cho tôi biết nhé!

**Bạn**: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!

2026-04-07 15:40:08 - Main - INFO - 👤 User input: Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!
2026-04-07 15:40:11 - AgentCore - INFO - 🤖 Agent quyết định gọi tool: search_flights với tham số {'origin': 'Hà Nội', 'destination': 'Phú Quốc'}
2026-04-07 15:40:11 - Tools - INFO - ✈️ Đang thực thi 'search_flights' | Khởi hành: Hà Nội -> Đích: Phú Quốc
2026-04-07 15:40:11 - Tools - INFO - ✅ Đã tìm thấy 3 chuyến bay.
2026-04-07 15:40:14 - AgentCore - INFO - 🤖 Agent quyết định gọi tool: calculate_budget với tham số {'total_budget': 5000000, 'expenses': 'vé máy bay: 1100000'}
2026-04-07 15:40:14 - Tools - INFO - 💰 Đang thực thi 'calculate_budget' | Ngân sách: 5,000,000₫ | Chi phí: vé máy bay: 1100000
2026-04-07 15:40:14 - Tools - INFO - ✅ Tính toán thành công. Ngân sách còn lại: 3.900.000₫
2026-04-07 15:40:19 - AgentCore - INFO - 🤖 Agent quyết định gọi tool: search_hotels với tham số {'city': 'Phú Quốc', 'max_price_per_night': 1950000}
2026-04-07 15:40:19 - Tools - INFO - 🏨 Đang thực thi 'search_hotels' | Thành phố: Phú Quốc | Max Price: 1,950,000₫
2026-04-07 15:40:19 - Tools - INFO - ✅ Đã tìm thấy 3 khách sạn phù hợp tiêu chí.

**Bạn**: Tôi muốn đặt khách sạn

2026-04-07 15:41:22 - Main - INFO - 👤 User input: Tôi muốn đặt khách sạn
2026-04-07 15:41:40 - AgentCore - INFO - 🤖 Agent trả lời trực tiếp cho khách hàng.

TravelBuddy: Mình rất vui khi được giúp đỡ bạn về việc du lịch, nhưng trước tiên, mình cần thêm thông tin để có thể tư vấn chính xác hơn. Bạn đang có dự định đến thành phố nào? Ngân sách của bạn khoảng bao nhiêu cho việc đặt khách sạn mỗi đêm?

**Bạn**: Giải giúp tôi bài tập lập trình Python về linked list

2026-04-07 15:41:56 - Main - INFO - 👤 User input: Giải giúp tôi bài tập lập trình Python về linked list
2026-04-07 15:42:23 - AgentCore - INFO - 🤖 Agent trả lời trực tiếp cho khách hàng.

TravelBuddy: Xin lỗi, nhưng mình chỉ là trợ lý du lịch và không thể hỗ trợ về lập trình hay bài tập học thuật. Nếu bạn có câu hỏi nào về du lịch hoặc cần tư vấn kế hoạch cho chuyến đi của mình, mình rất sẵn lòng giúp!


### Bonus
- Gợi ý chuyến bay chuyển tiếp, ví dụ không có chuyến thẳng từ Hà Nội đến Phú Quốc (em đã comment lại trong MockData, nó sẽ gợi ý chuyến nối tiếp)
- Có hiểu các từ đồng nghĩa như (TPHCM, Sài Gòn) (Hà Nội, Thủ Đô)
- Có lưu memory, context
- có file ghi log

2026-04-07 16:53:04 - Main - INFO - 👤 User input: HI
2026-04-07 16:53:08 - AgentCore - INFO - 🤖 Agent trả lời trực tiếp cho khách hàng: Chào bạn! Bạn đang có kế hoạch du lịch gì không? Mình có thể giúp bạn tư vấn điểm đến, phương tiện di chuyển hay chỗ nghỉ ngơi!
2026-04-07 16:53:22 - Main - INFO - 👤 User input: Tôi muốn đi từ Hà Nội đến Phú Quốc
2026-04-07 16:53:26 - AgentCore - INFO - 🤖 Agent quyết định gọi tool: search_flights với tham số {'origin': 'Hà Nội', 'destination': 'Phú Quốc'}
2026-04-07 16:53:26 - Tools - INFO - ✈️ Đang thực thi 'search_flights' | Khởi hành: Hà Nội -> Đích: Phú Quốc
2026-04-07 16:53:26 - Tools - INFO - ⚠️ Không có chuyến bay thẳng, hệ thống đang quét các chặng nối chuyến...
2026-04-07 16:53:26 - Tools - INFO - ✅ Đã tìm ra 3 lựa chọn nối chuyến hợp lý.
2026-04-07 16:53:33 - AgentCore - INFO - 🤖 Agent trả lời trực tiếp cho khách hàng: Mình đã tìm được một số chuyến bay nối chuyến từ Hà Nội đến Phú Quốc cho bạn như sau:

### Chuyến bay:
1. **Nối chuyến tại Hồ Chí Minh | Tổng giá: 1.600.000₫**
   - Chặng 1: Hà Nội -> Hồ Chí Minh - VietJet Air, 07:30 - 09:40
   - Chặng 2: Hồ Chí Minh -> Phú Quốc - VietJet Air, 15:00 - 16:00

2. **Nối chuyến tại Hồ Chí Minh | Tổng giá: 1.950.000₫**
   - Chặng 1: Hà Nội -> Hồ Chí Minh - Bamboo Airways, 12:00 - 14:10
   - Chặng 2: Hồ Chí Minh -> Phú Quốc - VietJet Air, 15:00 - 16:00

3. **Nối chuyến tại Hồ Chí Minh | Tổng giá: 2.250.000₫**
   - Chặng 1: Hà Nội -> Hồ Chí Minh - Vietnam Airlines, 06:00 - 08:10
   - Chặng 2: Hồ Chí Minh -> Phú Quốc - VietJet Air, 15:00 - 16:00

Bạn có thể cho mình biết ngân sách của bạn để mình hỗ trợ tìm khách sạn ở Phú Quốc nhé!
2026-04-07 16:54:10 - Main - INFO - 👤 User input: Tôi muốn đi từ Hà Nội đến Sài Gòn
2026-04-07 16:54:13 - AgentCore - INFO - 🤖 Agent quyết định gọi tool: search_flights với tham số {'origin': 'Hà Nội', 'destination': 'Sài Gòn'}
2026-04-07 16:54:13 - Tools - INFO - ✈️ Đang thực thi 'search_flights' | Khởi hành: Hà Nội -> Đích: Sài Gòn
2026-04-07 16:54:13 - Tools - INFO - ✅ Đã tìm thấy 4 chuyến bay thẳng.
2026-04-07 16:54:17 - AgentCore - INFO - 🤖 Agent trả lời trực tiếp cho khách hàng: Chuyến bay:
- **VietJet Air**: 07:30 - 09:40 | Hạng: economy | Giá: 950.000₫
- **Bamboo Airways**: 12:00 - 14:10 | Hạng: economy | Giá: 1.300.000₫
- **Vietnam Airlines**: 06:00 - 08:10 | Hạng: economy | Giá: 1.600.000₫
- **Vietnam Airlines**: 18:00 - 20:10 | Hạng: business | Giá: 3.200.000₫

Nếu bạn cần thêm thông tin về khách sạn hay chuyến đi chi tiết hơn, hãy cho mình biết nhé!
2026-04-07 16:56:17 - Main - INFO - 👤 User input: Tôi muốn đi Đà Nẵng
2026-04-07 16:56:24 - AgentCore - INFO - 🤖 Agent trả lời trực tiếp cho khách hàng: Tuyệt vời! Bạn muốn đi Đà Nẵng trong bao lâu và bạn đã có ngân sách khoảng bao nhiêu cho chuyến đi này chưa?
2026-04-07 16:56:48 - Main - INFO - 👤 User input: Tìm cho tôi chuyến bay đến Đà Nẵng
2026-04-07 16:56:50 - AgentCore - INFO - 🤖 Agent trả lời trực tiếp cho khách hàng: Bạn đi từ đâu đến Đà Nẵng?
2026-04-07 16:57:02 - Main - INFO - 👤 User input: Hà Nội
2026-04-07 16:57:02 - AgentCore - INFO - 🤖 Agent quyết định gọi tool: search_flights với tham số {'origin': 'Hà Nội', 'destination': 'Đà Nẵng'}
2026-04-07 16:57:09 - Tools - INFO - ✈️ Đang thực thi 'search_flights' | Khởi hành: Hà Nội -> Đích: Đà Nẵng
2026-04-07 16:57:09 - Tools - INFO - ✅ Đã tìm thấy 4 chuyến bay.
2026-04-07 16:57:13 - AgentCore - INFO - 🤖 Agent trả lời trực tiếp cho khách hàng.

TravelBuddy: Dưới đây là danh sách chuyến bay từ Hà Nội đi Đà Nẵng:

- **VietJet Air**: 08:30 - 09:50 | Hạng: economy | Giá: 890.000₫
- **Bamboo Airways**: 11:00 - 12:20 | Hạng: economy | Giá: 1.200.000₫
- **Vietnam Airlines**: 06:00 - 07:20 | Hạng: economy | Giá: 1.450.000₫
- **Vietnam Airlines**: 14:00 - 15:20 | Hạng: business | Giá: 2.800.000₫

Nếu bạn cần thêm thông tin về khách sạn hoặc các kế hoạch khác cho chuyến đi, hãy cho tôi biết nhé!

## Đánh giá

Dưới đây là bản báo cáo kiểm thử hoàn chỉnh cho **TravelBuddy Agent** (Lab 4), được trình bày chuyên nghiệp dựa trên kết quả thực tế từ console log bạn đã cung cấp.

---

# Báo cáo Kiểm thử TravelBuddy Agent

## 1. Kiểm tra kết nối API (`testapi_log.txt`)

| Hạng mục | Kết quả | Đánh giá |
| :--- | :--- | :--- |
| Kết nối LLM API | ✅ Thành công | Model `gpt-4o-mini` phản hồi ổn định |
| Model phản hồi | ✅ Tiếng Việt | Agent tuân thủ ngôn ngữ yêu cầu |
| Trạng thái | **Sẵn sàng** | Hệ thống đã cấu hình đầy đủ API Key và môi trường |

---

## 2. Test Cases Chính (Test 1 → Test 5)

### Test 1 — Direct Answer (Không cần tool)
**Input:** *"Xin chào! Tôi đang muốn đi du lịch nhưng chưa biết đi đâu."*

| Tiêu chí | Kỳ vọng | Thực tế | Đánh giá |
| :--- | :--- | :--- | :--- |
| Chào hỏi thân thiện | ✅ | Chào mừng người dùng niềm nở | ✅ Đạt |
| Hỏi thêm thông tin | ✅ (Ngân sách/Điểm đến) | Hỏi đúng về ngân sách và thành phố | ✅ Đạt |
| Không gọi tool | ✅ (0 tool calls) | Agent phản hồi trực tiếp | ✅ Đạt |
| Số bước LLM | — | 1 bước xử lý | ✅ Tối ưu |

> **Nhận xét:** Agent phản hồi tự nhiên theo đúng Persona, đóng vai trò người khởi gợi cảm hứng du lịch và thu thập dữ liệu đầu vào cần thiết.

---

### Test 2 — Single Tool Call
**Input:** *"Tìm giúp tôi chuyến bay từ Hà Nội đi Đà Nẵng"*

| Tiêu chí | Kỳ vọng | Thực tế | Đánh giá |
| :--- | :--- | :--- | :--- |
| Gọi `search_flights` | ✅ (`origin`, `dest`) | Gọi tool với tham số chính xác | ✅ Đạt |
| Liệt kê đủ chuyến bay | ✅ (4 chuyến) | Hiển thị đủ 4 chuyến từ Database | ✅ Đạt |
| Trình bày rõ ràng | ✅ | Markdown đẹp, in đậm tên hãng và giá | ✅ Đạt |
| Gợi ý bước tiếp theo | — | Mời hỏi thêm về khách sạn/kế hoạch | ✅ Bonus |

> **Nhận xét:** Agent nhận diện Intent cực nhanh ngay khi có đủ 2 địa danh. Logic chuẩn hóa tên thành phố giúp Tool truy vấn chính xác dữ liệu từ `FLIGHTS_DB`.

---

### Test 3 — Multi-Step Tool Chaining
**Input:** *"Tôi ở Hà Nội, muốn đi Phú Quốc 2 đêm, budget 5 triệu. Tư vấn giúp!"*

| Tiêu chí | Kỳ vọng | Thực tế | Đánh giá |
| :--- | :--- | :--- | :--- |
| Gọi `search_flights` | ✅ | Tìm thấy 3 chuyến bay thẳng | ✅ Đạt |
| Gọi `calculate_budget` | ✅ | Trừ 1.100.000đ vé máy bay | ✅ Đạt |
| Gọi `Google Hotels` | ✅ | `max_price_per_night`: 1.950.000đ | ✅ Đạt |
| Chuỗi tool tuần tự | ✅ | Flight → Budget → Hotel | ✅ Đạt |
| Ngân sách hợp lý | ✅ | Tự chia ngân sách cho 2 đêm | ✅ Tuyệt vời |

> **Chuỗi thực thi:** `search_flights` → `calculate_budget` → `Google Hotels`
> **Nhận xét:** Đây là minh chứng cho khả năng suy luận mạnh mẽ. Agent không chỉ gọi tool mà còn **tự thực hiện phép chia** (3.9tr / 2 đêm) để lọc khách sạn phù hợp nhất cho người dùng.

---

### Test 4 — Missing Info / Clarification
**Input:** *"Tôi muốn đặt khách sạn"*

| Tiêu chí | Kỳ vọng | Thực tế | Đánh giá |
| :--- | :--- | :--- | :--- |
| Hỏi lại thành phố | ✅ | Nhận ra thiếu địa điểm | ✅ Đạt |
| Hỏi lại ngân sách | ✅ | Nhận ra thiếu giới hạn chi phí | ✅ Đạt |
| Không gọi tool vội | ✅ (0 tool calls) | Trả lời trực tiếp để lấy thêm thông tin | ✅ Đạt |

> [cite_start]**Nhận xét:** Agent tuân thủ nghiêm ngặt Rule "Hỏi lại khi thiếu thông tin", tránh việc gọi Tool với tham số rỗng (gây lỗi hệ thống). [cite: 368-371]

---

### Test 5 — Guardrail / Refusal
**Input:** *"Giải giúp tôi bài tập lập trình Python về linked list"*

| Tiêu chí | Kỳ vọng | Thực tế | Đánh giá |
| :--- | :--- | :--- | :--- |
| Từ chối lịch sự | ✅ | "Xin lỗi, mình chỉ là trợ lý du lịch..." | ✅ Đạt |
| Giữ vững Persona | ✅ | Duy trì giọng văn TravelBuddy | ✅ Đạt |
| Không gọi tool | ✅ | Không bị đánh lừa để thực hiện logic lạ | ✅ Đạt |

> **Nhận xét:** Hệ thống Guardrail trong `system_prompt.txt` hoạt động hiệu quả. [cite_start]Agent biết rõ giới hạn nhiệm vụ và không thực hiện các yêu cầu học thuật ngoài ngành. [cite: 372-374, 52-53]
