employees = [
    "emp-001 | nGuYEN vaN a | sale | 0987654321",
    "emp-002 | tRan thi b | hr | 0911222333",
    "emp-003 | le van c | marketing | 09a8888888"
]

while True:
    print("\n===== MENU =====")
    print("1. Hiển thị danh sách nhân viên")
    print("2. Tìm kiếm nhân viên theo ID")
    print("3. Thoát chương trình")

    choice = input("Nhập lựa chọn: ")
    if choice == "1":

        print("\n===== DANH SÁCH NHÂN VIÊN =====")
        for emp in employees:
            parts = emp.split("|")
            emp_id = parts[0].strip().upper()
            full_name = parts[1].strip().title()
            department = parts[2].strip().upper()
            phone = parts[3].strip()
            if phone.isdigit():
                phone = "******" + phone[-4:]
            else:
                phone = "Invalid Format"

            print(f"""
ID: {emp_id}
Họ tên: {full_name}
Phòng ban: {department}
SĐT: {phone}
""")

    elif choice == "2":

        search_id = input("Nhập mã nhân viên: ").strip().upper()

        found = False

        for emp in employees:

            parts = emp.split("|")

            emp_id = parts[0].strip().upper()
            full_name = parts[1].strip().title()
            department = parts[2].strip().upper()
            phone = parts[3].strip()
            if phone.isdigit():
                phone = "******" + phone[-4:]
            else:
                phone = "Invalid Format"
            if emp_id == search_id:
                print("\n===== THÔNG TIN NHÂN VIÊN =====")

                print(f"ID: {emp_id}")
                print(f"Họ tên: {full_name}")
                print(f"Phòng ban: {department}")
                print(f"SĐT: {phone}")
                found = True
                break
        if found == False:
            print("Không tìm thấy nhân viên")
    elif choice == "3":
        print("Thoát chương trình")
        break
    else:
        print("Lựa chọn không hợp lệ, vui lòng nhập lại!")