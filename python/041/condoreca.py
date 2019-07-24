cant=int(input())
l1=[]
l2=[]
for i in range(0,cant):
    x=0
    l1=input()
    a,b,c=l1.split(" ")
    if (int(a)>int(b) and int(a)<int(c)) or (int(a)>int(c) and int(a)<int(b)):
        x=int(a)
    elif (int(b)>int(a) and int(b)<int(c)) or (int(b)>int(c) and int(b)<int(a)):
        x=int(b)
    else:
        x=int(c)
    l2.append(x)
print (*l2)
