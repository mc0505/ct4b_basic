print("Đăng kí tài khoản.")
while True:
    tdn = input("Hãy nhập tên đăng nhập: ")
    mk = input("Hãy nhập mật khẩu: ")
    email= input("Hãy nhập email: ")
    if len(tdn)>0 and len(mk)>0 and len(email)>0:
        print("Đăng kí thành công!")
        break
    else:
        print("Không hợp lệ! Hãy thử lại")