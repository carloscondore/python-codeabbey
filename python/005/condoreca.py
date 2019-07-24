cant=int(input())
l1=[]
l2=[]
for i in range(0,cant):
    x=0
    l1=input()
    a,b,c=l1.split(" ")
    l2.append(min(int(a),int(b),int(c)))
print (*l2)
