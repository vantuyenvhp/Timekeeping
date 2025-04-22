# Kết nối đến máy chấm công và lấy thông tin.
from zk import ZK, const
from datetime import datetime, timedelta

def thong_tin_may_cham_cong(ip: str, port: int):
    zk = ZK(ip, port=port, timeout=5, password=0, force_udp=False, ommit_ping=True)
    try:
        print(f"\nĐang kết nối đến máy chấm công tại {ip}:{port}...")
        conn = zk.connect()
        print("Kết nối thành công!\n")

        while True:
            print("Bạn muốn thực hiện thao tác nào?")
            print("1. Lấy thông tin máy chấm công")
            print("2. Lấy danh sách người dùng")
            print("3. Lấy dữ liệu chấm công của tất cả người dùng")
            print("4. Lọc dữ liệu chấm công theo User ID")
            print("0. Thoát")
            lua_chon = input("Nhập lựa chọn (0-4): ")

            if lua_chon == "1":
                info = conn.get_device_name()
                firmware = conn.get_firmware_version()
                platform = conn.get_platform()
                serial = conn.get_serialnumber()

                print("\n=== Thông tin máy chấm công ===")
                print(f"Tên thiết bị     : {info}")
                print(f"Firmware version : {firmware}")
                print(f"Nền tảng         : {platform}")
                print(f"Số seri          : {serial}\n")

            elif lua_chon == "2":
                users = conn.get_users()
                print("\n=== Danh sách người dùng ===")
                for user in users:
                    print(f"UserID: {user.user_id}, Tên: {user.name}, Card: {user.card}, Group ID: {user.group_id}")
                print()

            elif lua_chon == "3":
                print("\nChọn khoảng thời gian muốn lấy dữ liệu chấm công:")
                print("1. 1 tháng")
                print("2. 6 tháng")
                print("3. 1 năm")
                print("4. Toàn bộ")
                print("5. Hôm nay")
                thoi_gian = input("Nhập lựa chọn (1-5): ")

                now = datetime.now()
                if thoi_gian == "1":
                    start_time = now - timedelta(days=30)
                elif thoi_gian == "2":
                    start_time = now - timedelta(days=180)
                elif thoi_gian == "3":
                    start_time = now - timedelta(days=365)
                elif thoi_gian == "4":
                    start_time = None  # Toàn bộ
                else:
                    start_time = now - timedelta(days=1)

                users = conn.get_users()
                user_dict = {user.user_id: user.name for user in users}
                attendance = conn.get_attendance()
                print("\n=== Dữ liệu chấm công ===")
                for record in attendance:
                    if start_time is None or record.timestamp >= start_time:
                        user_name = user_dict.get(record.user_id, "Không rõ tên")
                        print(f"UserID: {record.user_id}, Tên: {user_name}, Thời gian: {record.timestamp}")
                print()

            elif lua_chon == "4":
                user_id = input("Nhập User ID cần lọc: ").strip()

                print("\nChọn khoảng thời gian:")
                print("1. 1 ngày")
                print("2. 1 tuần")
                print("3. 1 tháng")
                print("4. 6 tháng")
                thoi_gian = input("Nhập lựa chọn (1-4): ")

                now = datetime.now()
                if thoi_gian == "1":
                    start_time = now - timedelta(days=1)
                elif thoi_gian == "2":
                    start_time = now - timedelta(weeks=1)
                elif thoi_gian == "3":
                    start_time = now - timedelta(days=30)
                elif thoi_gian == "4":
                    start_time = now - timedelta(days=180)
                else:
                    print("Lựa chọn không hợp lệ.\n")
                    continue

                users = conn.get_users()
                user_dict = {user.user_id: user.name for user in users}
                attendance = conn.get_attendance()

                print(f"\n=== Dữ liệu chấm công của UserID {user_id} ===")
                found = False
                for record in attendance:
                    if str(record.user_id) == user_id and record.timestamp >= start_time:
                        user_name = user_dict.get(record.user_id, "Không rõ tên")
                        print(f"Thời gian: {record.timestamp}, Tên: {user_name}")
                        found = True
                if not found:
                    print("Không có bản ghi nào phù hợp.")
                print()

            elif lua_chon == "0":
                print("Đã thoát chương trình.")
                break
            else:
                print("Lựa chọn không hợp lệ. Vui lòng chọn lại.\n")

        conn.disconnect()
    except Exception as e:
        print(f"Lỗi khi kết nối: {e}")

# === Bắt đầu chương trình chính ===
if __name__ == "__main__":
    print("===== CHƯƠNG TRÌNH KẾT NỐI MÁY CHẤM CÔNG =====")
    ip = input("Nhập địa chỉ IP của máy chấm công: ")
    port = 4370  # Port mặc định cho thiết bị ZKTeco
    thong_tin_may_cham_cong(ip, port)
