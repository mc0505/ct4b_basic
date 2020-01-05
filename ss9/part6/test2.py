dstr = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
ppl = [150300,247100,333300,266800,420900,318000]
dt = [117.43,9.224,43.35,12.04,9.96,10.09]
dens=[]
i = 0
while i<5:
    dens1 = ppl[i]/dt[i]
    dens.append(dens1)
    i+=1
tb = sum(dens)/len(dstr)
print("Mật độ dân cư trung bình là",str(tb))
