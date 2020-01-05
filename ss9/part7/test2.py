score =[45, 67, 56, 78]
for index, item in enumerate(score, start =1):
    print(index, item,sep =". ")

score.extend(list(input("Nhập điểm cao mới: ").split()))
for index, item in enumerate(score, start =1):
    print(index, item, sep =". ")