a ={
    "name":"Harry Potter: The Deadly Hallows",
    "Date of release":"2007",
    "author": "J. K. Rolling",
    "Cast": ["Daniel Radcliffe","Emma Watson","Rupert Grint", "Tom Felton"]
}
a["publisher"] = "Bloomsbury Publishing"
print("Who acted as Harry Potter?")
for index, item in enumerate(a["Cast"]):

    print(index, item,sep = ". ")

while True:
    x = int(input("Place your number next to the answer here: "))
    if x == a["Cast"].index("Daniel Radcliffe"):
        print("Hura!!")
        break
    else:
        print("Try again!")