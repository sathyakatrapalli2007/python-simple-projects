try:
    n=int(input("enter a number"))
    if n%2==0:
        print(n)
except IndentationError:
    print("you missed an indent")