n = int(input("Hãy nhập 1 số: "))
if n%2==0 :
    for i in range(n-1,0,-2):
        print(i)
else:
    for i in range (n,0,-2):
        print(i)