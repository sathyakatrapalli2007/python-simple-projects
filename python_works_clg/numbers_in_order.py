numbers=[]
while True:
    n=int(input("Enter a positive number, hit negative to stop:"))
    if n<0:
        break
    numbers.append(n)

for i in numbers:
    print(i)
print("sum",sum(numbers))