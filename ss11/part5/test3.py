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
        "name":"Toshiba",
        "quantity":50,
        "price":600
    }
]
i=0
u=0
y=0
while True:
    if "Toshiba" in a[i]["name"]:
        a[i]["quantity"] =10
        break
    else:
        i+=1
while True:
    if "Dell" in a[u]["name"]:
        a[u]["quantity"] +=10
        break
    else:
        u+=1
while True:
    if  "Macbook" in a[y]["name"]:
        a[y]["quantity"]=2
        break
    else: 
        y+=1
print(a)
q1 ={
    "name":"Fujitsu",
    "quantity":15
}
q2 ={
    "name":"Alienware",
    "quantity":5
}
q=[q1,q2]
a.extend(q)
print(*a)