list_1 = ["Sport",  "Lol", "Bts"]
list_2 = ["Death note", "Netflix"]
list_1.extend(list_2)
for i, item in enumerate(list_1, start =1):
    print(i, item ,sep= ". ")
    