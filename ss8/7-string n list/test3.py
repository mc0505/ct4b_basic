import random
print("Đoán các thương hiệu!!")

while True:
    score = 0
    false = 5
    brand = ["The north face", "GAP", "MLB", "off white", "supreme", "vans", "converse","HNBMG", "nike","adidas","jordan","champion","thrasher", "bathing ape"]
    b = random.choice(brand)
    i = brand.index(b)
    x = list(b)
    random.shuffle(x)
    
    print(*x)
<<<<<<< HEAD

    answer = input("Đây là thương hiệu nào?  ")
=======
    answer = print(input("Đây là thương hiệu nào?  "))
>>>>>>> 9d55d88393fb42b66d5d4193c21ccffa55ade0eb

    if answer == b and score < 10:
        print("Đúng rồi")
        score +=1
        print("Điểm của bạn là: " + str(score))
        continue
    if answer != b and false >0:
        print("Sai rồi")
        false -=1
        print("Điểm của bạn là: " + str(score))
        continue
    if score == 10:
        print("Bạn đã thắng cuộc!")
        break
    if false == 0:
        print("Bạn đã thua cuộc!")
        break    