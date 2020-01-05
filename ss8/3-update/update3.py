yeu_thich = ["Bóng rổ", "Bóng đá",  "Ăn"]

i = int(input("Nhập một số: "))
x = input("Nhập một thứ bạn thích: ")
yeu_thich_moi = yeu_thich.insert(i, x)


print(*yeu_thich, sep=", ")