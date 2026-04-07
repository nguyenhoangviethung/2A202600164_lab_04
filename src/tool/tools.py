from langchain_core.tools import tool
from src.telemetry.logger import get_logger

# Khởi tạo logger
logger = get_logger("Tools")

# ==========================================
# MOCK DATA
# ==========================================
FLIGHTS_DB = {
    ("Hà Nội", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "07:20", "price": 1450000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "14:00", "arrival": "15:20", "price": 2800000, "class": "business"},
        {"airline": "VietJet Air", "departure": "08:30", "arrival": "09:50", "price": 890000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "11:00", "arrival": "12:20", "price": 1200000, "class": "economy"},
    ],
    # ("Hà Nội", "Phú Quốc"): [
    #     {"airline": "Vietnam Airlines", "departure": "07:00", "arrival": "09:15", "price": 2100000, "class": "economy"},
    #     {"airline": "VietJet Air", "departure": "10:00", "arrival": "12:15", "price": 1350000, "class": "economy"},
    #     {"airline": "VietJet Air", "departure": "16:00", "arrival": "18:15", "price": 1100000, "class": "economy"},
    # ],
    ("Hà Nội", "Hồ Chí Minh"): [
        {"airline": "Vietnam Airlines", "departure": "06:00", "arrival": "08:10", "price": 1600000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "07:30", "arrival": "09:40", "price": 950000, "class": "economy"},
        {"airline": "Bamboo Airways", "departure": "12:00", "arrival": "14:10", "price": 1300000, "class": "economy"},
        {"airline": "Vietnam Airlines", "departure": "18:00", "arrival": "20:10", "price": 3200000, "class": "business"},
    ],
    ("Hồ Chí Minh", "Đà Nẵng"): [
        {"airline": "Vietnam Airlines", "departure": "09:00", "arrival": "10:20", "price": 1300000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "13:00", "arrival": "14:20", "price": 780000, "class": "economy"},
    ],
    ("Hồ Chí Minh", "Phú Quốc"): [
        {"airline": "Vietnam Airlines", "departure": "08:00", "arrival": "09:00", "price": 1100000, "class": "economy"},
        {"airline": "VietJet Air", "departure": "15:00", "arrival": "16:00", "price": 650000, "class": "economy"},
    ],
}

HOTELS_DB = {
    "Đà Nẵng": [
        {"name": "Mường Thanh Luxury", "stars": 5, "price_per_night": 1800000, "area": "Mỹ Khê", "rating": 4.5},
        {"name": "Sala Danang Beach", "stars": 4, "price_per_night": 1200000, "area": "Mỹ Khê", "rating": 4.3},
        {"name": "Fivitel Danang", "stars": 3, "price_per_night": 650000, "area": "Sơn Trà", "rating": 4.1},
        {"name": "Memory Hostel", "stars": 2, "price_per_night": 250000, "area": "Hải Châu", "rating": 4.6},
        {"name": "Christina's Homestay", "stars": 2, "price_per_night": 350000, "area": "An Thượng", "rating": 4.7},
    ],
    "Phú Quốc": [
        {"name": "Vinpearl Resort", "stars": 5, "price_per_night": 3500000, "area": "Bãi Dài", "rating": 4.4},
        {"name": "Sol by Meliá", "stars": 4, "price_per_night": 1500000, "area": "Bãi Trường", "rating": 4.2},
        {"name": "Lahana Resort", "stars": 3, "price_per_night": 800000, "area": "Dương Đông", "rating": 4.0},
        {"name": "9Station Hostel", "stars": 2, "price_per_night": 200000, "area": "Dương Đông", "rating": 4.5},
    ],
    "Hồ Chí Minh": [
        {"name": "Rex Hotel", "stars": 5, "price_per_night": 2800000, "area": "Quận 1", "rating": 4.3},
        {"name": "Liberty Central", "stars": 4, "price_per_night": 1400000, "area": "Quận 1", "rating": 4.1},
        {"name": "Cochin Zen Hotel", "stars": 3, "price_per_night": 550000, "area": "Quận 3", "rating": 4.4},
        {"name": "The Common Room", "stars": 2, "price_per_night": 1800000, "area": "Quận 1", "rating": 4.6},
    ],
}

# ==========================================
# CUSTOM TOOLS
# ==========================================

@tool
def search_flights(origin: str, destination: str) -> str:
    """
    Tìm kiếm các chuyến bay giữa hai thành phố. Bao gồm cả chuyến bay thẳng và nối chuyến (1 điểm dừng).
    Tham số:
    origin: thành phố khởi hành (VD: 'Hà Nội', 'Hồ Chí Minh')
    destination: thành phố đến (VD: 'Đà Nẵng', 'Phú Quốc')
    """
    logger.info(f"✈️ Đang thực thi 'search_flights' | Khởi hành: {origin} -> Đích: {destination}")
    try:
   
        city_map = {
            "thành phố hồ chí minh": "Hồ Chí Minh",
            "tp hồ chí minh": "Hồ Chí Minh",
            "tphcm": "Hồ Chí Minh",
            "sài gòn": "Hồ Chí Minh"
        }
        norm_origin = city_map.get(origin.lower(), origin)
        norm_dest = city_map.get(destination.lower(), destination)

        def get_direct_flights(city1, city2):
            return FLIGHTS_DB.get((city1, city2)) or FLIGHTS_DB.get((city2, city1))

        flights = get_direct_flights(norm_origin, norm_dest)

        if flights:
            logger.info(f"✅ Đã tìm thấy {len(flights)} chuyến bay thẳng.")
            result = f"Danh sách chuyến bay THẲNG giữa {norm_origin} và {norm_dest}:\n"
            for f in flights:
                price_formatted = f"{f['price']:,}".replace(',', '.')
                result += f"- {f['airline']}: {f['departure']} - {f['arrival']} | Hạng: {f['class']} | Giá: {price_formatted}₫\n"
            return result

        logger.info("⚠️ Không có chuyến bay thẳng, hệ thống đang quét các chặng nối chuyến...")
        connecting_options = []

        all_cities = set()
        for (c1, c2) in FLIGHTS_DB.keys():
            all_cities.add(c1)
            all_cities.add(c2)

        for transit_city in all_cities:
            if transit_city == norm_origin or transit_city == norm_dest:
                continue

            leg1 = get_direct_flights(norm_origin, transit_city)
            leg2 = get_direct_flights(transit_city, norm_dest)

            if leg1 and leg2:
                for f1 in leg1:
                    for f2 in leg2:
                        if f1["arrival"] < f2["departure"]:
                            connecting_options.append({
                                "transit": transit_city,
                                "f1": f1,
                                "f2": f2,
                                "total_price": f1["price"] + f2["price"]
                            })

        if connecting_options:
            connecting_options.sort(key=lambda x: x["total_price"])
            logger.info(f"✅ Đã tìm ra {len(connecting_options)} lựa chọn nối chuyến hợp lý.")
            
            result = f"Không có chuyến bay thẳng từ {origin} đến {destination}. Gợi ý các chuyến bay NỐI CHUYẾN (1 điểm dừng):\n"
            for opt in connecting_options:
                price_formatted = f"{opt['total_price']:,}".replace(',', '.')
                transit = opt['transit']
                f1 = opt['f1']
                f2 = opt['f2']
                result += (f"\n📍 Nối chuyến tại {transit} | Tổng giá: {price_formatted}₫\n"
                           f"  + Chặng 1 ({norm_origin} -> {transit}): {f1['airline']}, {f1['departure']} - {f1['arrival']}\n"
                           f"  + Chặng 2 ({transit} -> {norm_dest}): {f2['airline']}, {f2['departure']} - {f2['arrival']}\n")
            return result

        logger.warning(f"❌ Không tìm thấy bất kỳ chuyến bay thẳng lẫn nối chuyến nào từ {norm_origin} đến {norm_dest}.")
        return f"Rất tiếc, hiện tại không có chuyến bay thẳng hay nối chuyến nào từ {origin} đến {destination}."

    except Exception as e:
        logger.exception("❌ Lỗi hệ thống trong search_flights")
        return f"Đã xảy ra lỗi khi tra cứu chuyến bay: {str(e)}"
    
@tool
def search_hotels(city: str, max_price_per_night: int = 99999999) -> str:
    """
    Tìm kiếm khách sạn tại một thành phố, có thể lọc theo giá tối đa mỗi đêm.
    Tham số:
    city: tên thành phố (VD: 'Đà Nẵng', 'Phú Quốc', 'Hồ Chí Minh')
    max_price_per_night: giá tối đa mỗi đêm (VNĐ), mặc định không giới hạn
    """
    logger.info(f"🏨 Đang thực thi 'search_hotels' | Thành phố: {city} | Max Price: {max_price_per_night:,}₫")
    try:
        hotels = HOTELS_DB.get(city)
        if not hotels:
            logger.warning(f"❌ Không có dữ liệu khách sạn tại {city}.")
            return f"Không có dữ liệu khách sạn tại {city}."
            
        filtered_hotels = [h for h in hotels if h["price_per_night"] <= max_price_per_night]
        sorted_hotels = sorted(filtered_hotels, key=lambda x: x["rating"], reverse=True)
        
        if not sorted_hotels:
            logger.warning(f"❌ Không tìm thấy khách sạn dưới {max_price_per_night:,}₫ tại {city}.")
            return f"Không tìm thấy khách sạn tại {city} với giá dưới {max_price_per_night:,}₫/đêm. Hãy thử tăng ngân sách."
            
        logger.info(f"✅ Đã tìm thấy {len(sorted_hotels)} khách sạn phù hợp tiêu chí.")
        result = f"Khách sạn tại {city} (Giá dưới {max_price_per_night:,}₫):\n"
        for h in sorted_hotels:
            price_formatted = f"{h['price_per_night']:,}".replace(',', '.')
            result += f"- {h['name']} ({h['stars']} sao, {h['area']}): Đánh giá {h['rating']}/5 | Giá: {price_formatted}₫/đêm\n"
            
        return result
    except Exception as e:
        logger.exception("❌ Lỗi hệ thống trong search_hotels")
        return f"Đã xảy ra lỗi khi tra cứu khách sạn: {str(e)}"

@tool
def calculate_budget(total_budget: int, expenses: str) -> str:
    """
    Tính toán ngân sách còn lại sau khi trừ các khoản chi phí.
    Tham số:
    total_budget: tổng ngân sách ban đầu (VNĐ)
    expenses: chuỗi mô tả các khoản chi, mỗi khoản cách nhau bởi dấu phẩy, định dạng 'tên khoản: số tiền' (VD: 'vé máy bay: 890000, khách sạn: 650000')
    """
    logger.info(f"💰 Đang thực thi 'calculate_budget' | Ngân sách: {total_budget:,}₫ | Chi phí: {expenses}")
    try:
        expense_items = [item.strip() for item in expenses.split(',')]
        total_expense = 0
        expense_details = []
        
        for item in expense_items:
            name, amount_str = item.split(':')
            name = name.strip().capitalize()
            amount = int(amount_str.strip())
            total_expense += amount
            
            amount_formatted = f"{amount:,}".replace(',', '.')
            expense_details.append(f"{name}: {amount_formatted}₫")
            
        remaining = total_budget - total_expense
        
        # Format bảng chi tiết theo đúng yêu cầu
        result = "Bảng chi phí:\n"
        for detail in expense_details:
            result += f"- {detail}\n"
            
        total_formatted = f"{total_expense:,}".replace(',', '.')
        budget_formatted = f"{total_budget:,}".replace(',', '.')
        
        result += f"\nTổng chi: {total_formatted}₫\n"
        result += f"Ngân sách: {budget_formatted}₫\n"
        
        if remaining < 0:
            deficit_formatted = f"{abs(remaining):,}".replace(',', '.')
            logger.warning(f"⚠️ Vượt ngân sách! Âm {deficit_formatted}₫")
            result += f"Vượt ngân sách {deficit_formatted}₫! Cần điều chỉnh."
        else:
            remaining_formatted = f"{remaining:,}".replace(',', '.')
            logger.info(f"✅ Tính toán thành công. Ngân sách còn lại: {remaining_formatted}₫")
            result += f"Còn lại: {remaining_formatted}₫"
            
        return result
        
    except ValueError as ve:
        logger.error(f"❌ Lỗi Value Error khi parse dữ liệu budget: {str(ve)}")
        return "Lỗi format đầu vào. Vui lòng cung cấp danh sách chi phí theo định dạng 'tên khoản: số tiền' cách nhau bằng dấu phẩy."
    except Exception as e:
        logger.exception("❌ Lỗi hệ thống không xác định trong calculate_budget!")
        return f"Đã xảy ra lỗi trong quá trình tính toán: {str(e)}"

TOOLS = [search_flights, search_hotels, calculate_budget]