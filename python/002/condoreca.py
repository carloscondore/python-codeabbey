x=0
ai=int(input())
no=input().split(" ")

if ai==len(no):
    for n in no:
        x=x+int(n)
    print(x)
elif ai>len(no):
    print("cantidad de numeros en lista es inferior")
elif ai<len(no):
    print("cantidad de numeros en lista es superior")
else :
    print("debe ingresar numeros en lista")
