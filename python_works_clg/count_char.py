string=input("enter a string:")
char={}
for letter in string:
    
    if letter in char:
        char[letter]+=1
    else:
        char[letter]=1
l=list(char)
l.sort(key=lambda x: char[x],reverse=True)
print(l)
