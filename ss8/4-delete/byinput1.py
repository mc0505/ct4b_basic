yeu_thich = ["Bóng rổ", "Bóng đá",  "Ăn"]
while True:
    i = int(input("Nhập 1 số: "))
    if i in range (3):
        yeu_thich.pop(i)
        break
    else: 
        print("Thử lại 1 số từ 0 đến 2: ")

print(*yeu_thich, sep=", ")