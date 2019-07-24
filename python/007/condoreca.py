z=0.00
f=0.00
adata=[]
l1=[]
l2=[]
def convierte(x):
 z=(float(x)-32)*5/9
 z=round(z)
 return z
adata=input().split(" ")
cant=adata[0]
for i in range(1,int(cant)+1):
 x=0
 f=adata[i]
 x=convierte(f)
 l2.append(x)   
print (*l2)
