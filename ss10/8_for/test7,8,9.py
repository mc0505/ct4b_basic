a ={
    "name":"Harry Potter: The Deadly Hallows",
    "Date of release":"2007",
    "author": "J. K. Rolling",
    "Cast": ["Daniel Radcliffe","Emma Watson","Rupert Grint", "Tom Felton"]
}
print(a["Cast"][1])
for index, item in enumerate(a["Cast"], start=1):
    print(index,item)
for k,v in a.items():
    print(k, v)