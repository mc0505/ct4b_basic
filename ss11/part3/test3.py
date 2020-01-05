a = [
    {
        "name" : "HP",
        "quantity" :"20"
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
u1={
    "name":"Fujitsu",
    "quantity":15
}
u2={
    "name":"Alienware",
    "quantity":5
}
u = [u1,u2]
a.extend(u)
print(a)