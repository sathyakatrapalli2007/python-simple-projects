lists=['cat','cat','dog']
new=[]
for i in lists:
    if i not in new:
        new.append(i)
print(new)