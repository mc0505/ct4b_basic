dstr = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
ppl = [150300,247100,333300,266800,420900,318000]
u = len(ppl)
max = 0 
a =0
i = 0 
while i in range (u):
    if max <ppl[i]:
        max = ppl[i]
    i +=1
print(max)
min = 999999
while a in range (u):
    if min > ppl[a]:
        min = ppl[a]
    a -=1
print(min)


    