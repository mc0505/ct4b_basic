month = int(input("Nhập một tháng trong năm: "))
a = [1,3,5,7,8,10,12]
if month  in a:
    print("Tháng",month,"có 31 ngày")
elif month ==2:
    print("Tháng",month,"có 28 ngày")
else:
    print("Tháng",month,"có 30 ngày")