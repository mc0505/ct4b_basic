yeu_thich = ["Bóng rổ", "Bóng đá",  "Ăn"]

if "LOL " not in yeu_thich:
    print("Không thích LOL.")
else:
    yeu_thich.remove(LOL)

print(*yeu_thich, sep=", ")