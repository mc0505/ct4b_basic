score =[45, 67, 56, 78]
score.sort(reverse = True)
for index, item in enumerate(score, start =1):
    print(index, item, sep =". ")

score.extend(list(map(int, input("Nhập điểm cao mới: ").split())))
score.sort(reverse = True)
for index, item in enumerate(score, start =1):

    print(index, item, sep =". ")