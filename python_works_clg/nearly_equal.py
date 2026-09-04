def equal(a,b):
    if abs(len(a)-len(b))>1:
        return False
    else:
        return True
    
        count=0
        for i in range(min(len(a),len(b))):
            if a[i]!=b[i]:
                count+=1
        count+=abs(len(a)-len(b))
        return count==1
    return abs(len(a)-len(b))==1
def nearly_equal(a,b):
    if equal(a,b):
        if len(a)==len(b):
            return True
        if len(a)<len(b):
            a,b=b,a
        for i in range(min(len(a),len(b))):
            if a[i]!=b[i]:
                if a[:i]+a[i+1:]==b:
                    return True
    return False
a=input("enter a string (greater length):")
b=input("smaller length:")

if nearly_equal(a,b):
    print("nearly equal")
