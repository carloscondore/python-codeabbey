cant=int(input())
l1=[]
for i in range(0,cant):
 a,b,c=input().split(" ")
 x=int(a)*int(b)+int(c)
 k=0
 for j in range(0,len(str(x))):
  z=len(str(x))
  m=int(z)-(j+1)
  d=str(x)[:z-m]
  y=int(d) % 10
  k=k+y 
 l1.append(k)
print(*l1)
