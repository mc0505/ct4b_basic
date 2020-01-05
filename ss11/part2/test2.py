a = {
    "name":["HP","Dell","Macbook","ASUS"],
    "quantity" :[20,50,12,30]
}
u = input("Nhập tên loại máy mới: ")
i = int(input("Nhập số lượng loại máy này: "))
a["name"].append(u)
a["quantity"].append(i)
print(a)