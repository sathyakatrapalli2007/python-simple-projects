n=int(input("enter a number:"))
for i in range(1,n+1):
    counter=0
    for j in range(1,i+1):
        if(i%j==0):
            counter=counter+1
    if(counter==2):
        print(i)