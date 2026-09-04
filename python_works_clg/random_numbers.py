import random
n=int(input("enter a number:"))
f=open("random.txt","w")

for i in range(n):
    num=random.randint(1,100)
    f.write(f"{num}\n")

f.close()

f=open('random.txt')
cont=f.read()
print(cont)