color = ["blue", "red", "teal", "green"]
for index, item in enumerate(color, start =1):
    print(index, item, sep =".")

i = int(input("Chọn 1 vị trí muốn xoá: "))
color.pop(i)
print(*color, sep = ", ")


x = input("Chọn 1 màu muốn xoá: ")
color.remove(x)
print(*color, sep = ", ")
