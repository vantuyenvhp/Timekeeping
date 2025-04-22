```markdown
# Attendance Device Connector (`chamcong.py`)

This Python script provides a command-line interface to connect with and retrieve data from a ZKTeco biometric attendance device via IP.

## 📦 Features

- Connect to ZKTeco time attendance machines via IP.
- Display device information.
- List all registered users.
- Retrieve attendance logs for all users.
- Filter attendance records by User ID and time range.

## 🧰 Requirements

- Python 3.6+
- `pyzk` library

Install dependencies:

```bash
pip install pyzk
```

## 🚀 How to Use

Run the script using Python:

```bash
python chamcong.py
```

You will be prompted to enter the IP address of the attendance device (default port 4370 is used).

### Menu Options

After successful connection, you can choose from the following actions:

1. **Get device information** – View name, firmware, platform, and serial number.
2. **List users** – Display all users registered in the device.
3. **Fetch all users' attendance data** – Filter by time range:
   - 1 month
   - 6 months
   - 1 year
   - All records
   - Today
4. **Filter attendance by User ID** – Narrow down logs by:
   - 1 day
   - 1 week
   - 1 month
   - 6 months
0. **Exit** – Close the program.

## 📝 Notes

- Default port used for connection is `4370`.
- Connection timeout is set to 5 seconds.
- If the connection fails, a descriptive error will be shown.

## 📄 License

This project is intended for educational and integration purposes. Please ensure you comply with your local IT policies before deploying in production.

---

Developed with ❤️ for ZKTeco integration.
```

---

Bạn có thể chỉnh sửa thêm để phù hợp với yêu cầu branding hoặc quy chuẩn nội bộ của bạn. Nếu bạn cần bản Việt hóa README này, vui lòng cho biết!
