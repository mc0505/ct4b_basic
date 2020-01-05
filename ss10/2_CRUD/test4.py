fm = {
    "name" : "The Blind Side",
    "descrpition":"An orphan who eventually realize the meaning or familyhood",
    "type of film": "drama",
}
while True:
    k = input("Nhập vào 1 key vào dict của bạn: ")
    v  =input("Nhập value vào key đó: ")
    if len(k) > 0 and len(v)>0:
        fm[k] = v
        print(fm)
        break
    else:
        print("Thử lại!")