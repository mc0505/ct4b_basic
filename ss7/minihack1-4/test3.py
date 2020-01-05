print("Đăng kí tài khoản.")
tdn = input("Hãy nhập tên đăng nhập: ")

while True:
    email= input("Hãy nhập email: ")
    mk = input("Hãy nhập mật khẩu: ")
    mk1= input("Hãy nhập lại mật khẩu: ")


    if "@" in email and "." in email and len(mk)>8 and mk==mk1:
        print("Đăng kí thành công!")
        break
    elif mk!=mk1 and len(mk) <= 8:
        print("Mật khẩu nhập lại sai! Hãy thử lại.")
    elif "@" not in email and "." not in email :
        print("Email không hợp lệ! Hãy thử lạị.")
    else:
        print("Đăng kí thất bại! Hãy thử lại.")