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
i=0
while i<7:
    if "ASUS" in a[i]["name"]:
        
        print("Giá của",a[i]["name"],"là",a[i]["price"])
        break
    else:
        i+=1
