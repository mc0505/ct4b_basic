tk = input("Nhập tên tài khoản: ")

mkdung = "mc0505"
while True:
    mk = input("Nhập mật khẩu:")
    if mk == mkdung:
        print("Access allowed!")
        break
    else:
        print("Try Again!")