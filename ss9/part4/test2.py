num = list(map(int, input("Nhập các số cách nhau bằng dấu phẩy: ").split(",")))
for i in range len(num):
    if num[i]%2==0:
        print(num[i])

