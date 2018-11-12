
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 1]
b=[]
for element in a:
    if element < 22:
        b.append(element)
        print(str(element))

print(b)