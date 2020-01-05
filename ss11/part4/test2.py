a = [
    {
        "name" : "HP",
        "quantity" :20,
        "price":600
    },
    {
        "name": " Dell ",
        "quantity":50,
        "price": 650
    },
    {
        "name":"Macbook",
        "quantity":12,
        "price":12000
    },
    {
        "name":"ASUS",
        "quantity": 30,
        "price":400
    },
    {
        "name":"Fujitsu",
        "quantity":15,
        "price": 900
    },
    {
        "name":"Alienware",
        "quantity":5,
        "price":1000
    },
    {
        "name":"Toshiba",
        "quantity":50,
        "price":600
    }
]
b = 0
while b < 4:
    for k,v in a[b].items():
        print(k,":",v)
    b+=1
b = 0
while b<3:
    u = input("Hãy nhập đúng máy tính cần tìm: ")
    i=0
    while i<7:
        if u in a[i]["name"]:
            print("Giá của",a[i]["name"],"là",a[i]["price"])
            break
        else:
            i+=1
    if i >= 7:
        print("Try again!")
    else:
        break
