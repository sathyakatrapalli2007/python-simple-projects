n=int(input("enter a number:"))
f1,f2=0,1
print(f1)
print(f2)
for i in range(n-2):
    f=f1+f2
    print(f)
    f1=f2
    f2=f
    
