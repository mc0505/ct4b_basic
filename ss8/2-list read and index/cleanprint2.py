yeu_thich = ["Bóng rổ", "Bóng đá",  "Ăn"]
yeu_thich.append(input("Thứ bạn yêu thích là gì? "))
yeu_thich_moi = ', '.join(yeu_thich)
print(yeu_thich_moi) 

yeu_thich = ["Bóng rổ", "Bóng đá",  "Ăn"]
yeu_thich.append(input("Thứ bạn yêu thích là gì? "))
print(*yeu_thich, sep=", ")