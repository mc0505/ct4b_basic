score =[45, 67, 56, 78]
score.sort(reverse = True)
so_lan_nhap_diem = 0
for index, item in enumerate(score, start =1):
    print(index, item, sep =". ")
while so_lan_nhap_diem < 5:
    u = score.extend(list(map(int, input("Nhập điểm cao mới: ").split())))
    score.sort(reverse = True)
    a = [score[0],score[1],score[2],score[3],score[4]]
    for index, item in enumerate(a, start =1):
        
        print(index, item, sep =". ")
    so_lan_nhap_diem += 1