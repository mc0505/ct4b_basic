list_1 = ["Sport", "Lol", "Bts", "Death note", "Netflix"]
choices = ["C", "R", "U" , "D"]
<<<<<<< HEAD

while True:
    userchoice = input("Bạn muốn chọn 'C', 'R', 'U' hay 'D'? " )
=======
userchoice = input("Bạn muốn chọn 'C', 'R', 'U' hay 'D'? " )
while True:
>>>>>>> 9d55d88393fb42b66d5d4193c21ccffa55ade0eb
    if userchoice[0].upper() == "C":
        list_2= input("Bạn yêu thích gì? ")
        list_1.append(list_2)
        print(*list_1, sep=", ")
        break
    elif  userchoice[0].upper() == "R":
        for item in list_1:
            print(item)
        break
    elif userchoice[0].upper() == "U":
        while True:
            x = input("Nhập một thứ bạn thích: ")
            i = int(input("Nhập vị trí của phần tử trong danh sách muốn thay đổi: "))
            if i in range(5):
                list_1[i] = x
                print(*list_1)
                break
            else: 
                print("Try again!")
        break
    elif userchoice[0].upper() == "D":
        while True:
            i = int(input("Bạn muốn xoá thứ yêu thích số mấy? "))
            if i in range(5):
                list_1.pop(i)
                print(*list_1)
                break
            else:
                print("Try again!!")
        break
    else: 
        print("Hãy chọn đúng ký tự!! ")

        

