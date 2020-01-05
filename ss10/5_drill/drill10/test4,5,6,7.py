a ={
    "q1" :[66,65,32,64],
    "q2":[7,-6,6,5]
}
print("Select the correct answer!!")
i=0
x=0
while True:
    for index, item in enumerate(a["q1"],start=1):
        print(index, item, sep = ". ")
    b = int(input("8 + 8 x 2? "))
    if b == 32:
        print("Hura!!")
        i+=1
        x+=1
        break
    else:
        print("Wrong!!")
        x+=1
        break

while True:
    for index, item in enumerate(a["q2"],start=1):
        print(index, item, sep = ". ")
    c =int(input("2 + 1 x 3 =? "))
    if c == 5:
        print("Hura!!")
        i+=1
        x+=1
        break
    else:
        print("Wrong!!")
        x+=1
        break

print("Your score is", i)
print("The percentage of getting the right answer is", i/x*100,"%")