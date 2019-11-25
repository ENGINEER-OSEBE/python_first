
is_morning = False
is_evening = False

if is_morning and is_evening :
    print("give liam tea")
elif is_morning and not(is_evening):
    print("give him milk")
elif is_evening and not(is_morning):
    print("give him food and water.")
else:
    print("give him food it is nether\nmorning nor evening.")

print("i leave my house")
is_cloudy = True
if is_cloudy:
     print("i bring my umbrella if is_cloudy.")
else :
     print("i bring sun glasses.")
print("i am at a restaurant")
i_want_meat = False
i_want_pasta = False
if i_want_meat:
    print("Order a steak")
elif i_want_pasta and not(i_want_meat):
    print("order spaghetti and meatballs")
else:
    print("order a salad if i dont want either meat or spaghetti")

def comparisons(a,b,c):
    if a==b and a == c:
        return a
    elif a==b and a!=c:
        return b
    else:
       return c


print ( comparisons("dog","dog ","cat"))






