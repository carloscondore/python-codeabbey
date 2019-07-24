cant=int(input())
l1=[]
for i in range(0,cant):
 a,b,n=input().split(" ")
 cum=0
 x=0
 while x<int(n):
  z=int(a)+int(b)*int(x)
  acum=acum+z
  x=x+1
 l1.append(acum)
print (*l1)
