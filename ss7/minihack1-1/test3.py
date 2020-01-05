while True:
    num = (input("Place a number:  "))
    if num.isdigit():
        print(int(num)**2)
        break
    else:
        print("Try Again!")