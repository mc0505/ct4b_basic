a = {
    "name" :["Huy", "Tung", "M.Duc"],
    "role" : ["Waiter, Cook, Manager"],
    "hours" :[12,24,20],
    "Salary per hour": [ 0.8, 1.5, 2],
}
print(a)


name1 = ["Don", "H.Duc"]
role1 = ["Waiter", "Waiter"]
hours1 = [12,14]
s1= [0.9,0.7]
a["name"].extend(name1)
a["role"].extend(role1)
a["hours"].extend(hours1)
a["Salary per hour"].extend(s1)
print(a)