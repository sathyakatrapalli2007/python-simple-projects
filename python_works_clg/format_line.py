f=open("new.txt","w")
txt="i would rather run away\nwould i run off the world someday\nnobody knows"
f.write(txt)
f.close

f=open("new.txt","r")
index=1
lines=f.readlines()
for line in lines:
    line=line.rstrip()
    print(f"{index}. {line}:")
    index+=1
