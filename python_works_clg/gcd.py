a=int(input("enter a number:"))
b=int(input("enter another number:"))

while True:
    a,b=b,a%b
    if b==0:
        break

print(a)