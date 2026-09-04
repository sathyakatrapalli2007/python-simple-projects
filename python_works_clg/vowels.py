string=input("Enter a string:")
v=0
c=0
vowels="aeiouAEIOU"
for i in string:
    if i in vowels:
        v+=1
    else:
        c+=1
print("vowels:",v,"cons",c)