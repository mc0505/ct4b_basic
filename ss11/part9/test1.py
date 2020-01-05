a={
    "Name": "Light",
    "Age": 17,
    "Strength": 8,
    "Defense": 10,
    "HP":100,
    "Backpack": ["Shield", "Bread Loaf"],
    "Gold": 100,
    "Level": 2,
}
sk=[
    {
        "Skill": 1,
        "Name": "Tackle",
        "Minimum level": 1,
        "Damage": 5,
        "Hit rate": 0.3
    },
    {
        "Skill": 2,
        "Name": "Quick attack",
        "Minimum level": 2,
        "Damage": 3,
        "Hit rate": 0.5
    },
    {
        "Skill": 3,
        "Name": "Strong Kick",
        "Minimum level": 4,
        "Damage": 9,
        "Hit rate": 0.2
    }
]
i=0
while i<=5:
    u = int(input("Hãy chọn skill bạn muốn dùng:  "))
    if u<=3:
        if u <= a["Level"]:
            print("Skill của bạn tạo",sk[u-1]["Damage"],"sát thương")
            i+=1
            continue
        elif u>= a["Level"]:
            print("Bạn chưa đủ level để thực hiện skill này")
    else: 
        print("Hãy thử chọn lại")