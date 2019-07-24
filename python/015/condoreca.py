l1=[]
l1=input().split(" ")
cant=len(l1)
a=0
b=0
minimo=0
maximo=0
a=int(l1[0])
for i in range(0,cant):
 b=int(l1[i])
 if b<minimo:
  minimo=b
 elif b>maximo:
  maximo=b
 a==b
print (maximo,minimo)
