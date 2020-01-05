a = {
    "name":["HP","Dell","Macbook","ASUS"],
    "quantity" :[20,50,12,30]
}
i = a["name"].index("Dell")
u = a["name"].index("Macbook")
a["quantity"][i]=60
a["quantity"][u]=2
print(a)