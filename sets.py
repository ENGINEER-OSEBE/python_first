# print my sets of data
group = {"mike","evans","hope","peace","mercy", 23, 15, False}
ground = {"soil", "concrete","tiles", "glass","grass", 11,87,True,"mike"}
print(group)
print(ground)
#adding
group.add("kemmy")
print(group)
#union
unitas = group.union(ground)
print(unitas)
#intersection
inter = group.intersection(ground)
print(inter)
#difference
diffy = group.difference(ground)
print(diffy)
diff = group.difference(unitas)
print(diff)
if group > ground:
    print("group is super set of ground")
else:
    print("ground is super set of group")
#clear
group.clear()
print(group)