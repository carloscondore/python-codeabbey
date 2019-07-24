z=0.00
cant=int(input())
l1=[]
l2=[]
def redondea(x,y):
 z=float(x)/float(y)
 z=round(z)
 return z
for i in range(0,cant):
 x=0
 l1=input()
 a,b=l1.split(" ")
 x=redondea(a,b)
 l2.append(x)
print (*l2)
