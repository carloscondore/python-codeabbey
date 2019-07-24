z=0.00
cant=input()
l1=[]
l2=[]
def masa(p,h):
 z = float(p) / float(h)**2
 return z
for i in range(0,int(cant)):
 x=0.00
 adata=input()
 p,h=adata.split(" ")
 x=masa(p,h)
 if x>=30.0:
  y="obese"
 elif x<30.0 and x>=25.0:
  y="over"
 elif x<25 and x>=18.5:
  y="normal"
 else:
  y="under" 
 l2.append(y)
print (*l2)
