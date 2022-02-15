#eight_lbs = input('weight (lbs): ')
#weight_kg = int(weight_lbs) * 0.45
#print(weight_kg)
"""weight=int(input("weight:"))
units=input("(L) bs or (K)g: ")
if units.upper()=="L":
    converted=weight *0.45
    print(f"you are {converted} kilos")
else:
    converted=weight // 0.45
    print(f"you are {converted}pound")"""
w=int(input("weight: "))
units=input("(L)bs or (k)g:")
if units.upper()== "L":
    converted=w *0.45
    print(f"you are {converted}kilos")
else:
    converted=w / 0.45
    print(f"you are  {converted}pounds")