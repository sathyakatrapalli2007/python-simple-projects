def equal(a,b):
    if len(a)==len(b):
        count=0
        for i in range(len(a)):
            if a[i]!=b[i]:
                count+=1
        return count==1
    return abs(len(a)-len(b))==1

def nearly_equal(a,b):
    if equal(a,b):
        if len(a)==len(b):
            return True

        if len(a)<len(b):
            a,b=b,a

        for i in range(len(a)):
            if a[:i]+a[i+1:]==b:
                return True

    return False

a=input("Enter first string: ")
b=input("Enter second string: ")

if nearly_equal(a,b):
    print("nearly equal")
else:
    print("not nearly equal")