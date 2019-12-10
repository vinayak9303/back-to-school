def greatest_num(a,b,c):
    if (a<b<c):
        return c
    elif(a<b>c):
        return b
    elif (a>b>c):
        return a
a,b,c=input("").split(" ")
a=int(a)
b=int(b)
c=int(c)
print(greatest_num(a,b,c))
