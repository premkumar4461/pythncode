weight=int(input("weight: "))
units=input("(L)lbs or (K)g: ")
if units.upper()=='L':
    con=weight*0.45
    print(f"you are {con} kilos")
else:
    con=weight/0.45
    print(f"you are {con} pounds")


    