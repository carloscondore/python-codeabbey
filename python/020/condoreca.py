l2=[]
cantidad=input()
vocales=["a","e","i","o","u","y"]
for c in range(0,int(cantidad)):
 x=0
 l1=input()
 for i in range(0,6):
  x=x+l1.count(vocales[i],0,len(l1))
 l2.append(x)
print(*l2)


