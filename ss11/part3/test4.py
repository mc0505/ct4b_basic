a = [
    {
        "name" : "HP",
        "quantity" :20
    },
    {
        "name": " Dell ",
        "quantity":50
    },
    {
        "name":"Macbook",
        "quantity":12
    },
    {
        "name":"ASUS",
        "quantity": 30
    }
]
i = 0
while i < 4:
    for k,v in a[i].items():
        print(k,":",v)
    i+=1