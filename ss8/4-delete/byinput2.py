yeu_thich = ["Bóng rổ", "Bóng đá",  "Ăn"]
while True:
    i = input("Nhập một thứ yêu thích cần bỏ: ")
    """ x = i[0].upper()""" # làm như thế nào để dù gõ chữ b hay ă k hoa nhưng mà máy tính vẫn sửa??
    if i in yeu_thich:
        yeu_thich.remove(i)
        break
    else: 
        print("Thử lại! ")

print(*yeu_thich, sep=", ")