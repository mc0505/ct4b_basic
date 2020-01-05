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
y=0
while True:
    u = list(input("Hãy nhập tên máy và số lượng máy cách nhau bằng dấu (:): ").split(":"))
    if len(u)>0 and u[1].isdigit()==True:
        for i in range(len(a)):
            if u[0]==a[i]["name"]:
                a[i]["quantity"]=u[1]
                print(a)
            else:
                q = {
                    "name" : u[0],
                    "quantity" :u[1]
                }
                a.append(q)
                print(a)
                break
        break
    else:
        print("Try again!")