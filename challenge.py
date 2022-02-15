import numbers


numbers=[5,1,5,1,5]
for x in numbers:
    output=""
    for count in range(x):
        output+="X"
    print(output)