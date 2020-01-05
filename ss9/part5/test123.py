dstr = ["ST", "BĐ", "BTL", "CG", "ĐĐ", "HBT"]
ppl = [150300,247100,333300,266800,420900,318000]
i= ppl.index(max(ppl))
print("Quận",dstr[i],"chứa số dân lớn nhất là",max(ppl))
u= ppl.index(min(ppl))
print("Quận",dstr[u],"chứa số dân ít nhất là",min(ppl))