cant=int(input())
l1=[]
l2=[]
for i in range(0,cant):
    x=0
    l1=input()
    a,b=l1.split(" ")
    if int(a)<int(b):
        l2.append(a)
    else:
        l2.append(b)
print (*l2)
