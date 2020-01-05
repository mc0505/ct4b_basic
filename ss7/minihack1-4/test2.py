print("Đăng kí tài khoản.")
tdn = input("Hãy nhập tên đăng nhập: ")
email= input("Hãy nhập email: ")
while True:

    mk = input("Hãy nhập mật khẩu: ")
    mk1= input("Hãy nhập lại mật khẩu: ")

    if  len(mk)>0 and mk==mk1:
        print("Đăng kí thành công!")
        break
    elif mk!=mk1:
        print("Mật khẩu nhập lại sai! Hãy thử lại.")
    else:
        print("Đăng kí thất bại! Hãy thử lại.")