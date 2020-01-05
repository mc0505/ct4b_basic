bl =[
    {
        "name":"Huy",
        "role":"Waiter",
        "hours":12,
        "salary per hour":0.8,
    },
    {
        "name":"Tung",
        "role":"Cook",
        "hours":24,
        "salary per hour":1.5,
    },
    {
        "name":"M.Duc",
        "role":"Manager",
        "hours":20,
        "salary per hour":2,
    },
    {
        "name":"Don",
        "role":"Waiter",
        "hours":12,
        "salary per hour":0.9,
    },
    {
        "name":"H.Duc",
        "role":"Waiter",
        "hours":14,
        "salary per hour":0.7,
    }
]
a =[]
i = 0 
while i <4:
    u = bl[i]["hours"] * bl[i]["salary per hour"] * 30
    a.append(u)
    i +=1
print("Tổng số tiền mà chi nhánh phải trả cho toàn bộ các nhân viên là",sum(a))