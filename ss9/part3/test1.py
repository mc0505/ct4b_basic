num = ["-8", "1", "5", "13", "45", "99"]
while True:
    x =input("Hãy đoán 1 số trong dãy: ")
    if x in num:
        print("Số",x,"có trong dãy!")
        index = num.index(x)
        print("Số",x, "ở vị trí số",index)
        
        break
    else:
        print("Try again!")