import random

p1=input("Hello human1! Please enter your name:")
p2=input("Hello human2! Please enter your name:")
print("Here are your boxes!")

print(f"""
 +-----------+  +-----------+
 |   RED     |  |   GOLD    |
 |   BOX     |  |   BOX     |
 +-----------+  +-----------+
""")
print(p1[:13].center(13),p2[:13].center(13))

carrotFirst=""
if random.choice((1,2))==1:
    carrotFirst=True
else:
    carrotFirst=False

print("Please tell the the second player to close their eyes")
input("Press enter when the second player has closed their eyes:")
print()

if carrotFirst:
    print(f"""

        V  V
        |  |
    +-----------+
    |   |  |    |
    |           |
    +-----------+  +-----------+
    |   RED     |  |   GOLD    |
    |   BOX     |  |   BOX     |
    +-----------+  +-----------+
    """)
    print(p1[:13].center(13),p2[:13].center(13))


else:
    print(f"""
    +-----------+
    |           |
    |           |
    +-----------+  +-----------+
    |   RED     |  |   GOLD    |
    |   BOX     |  |   BOX     |
    +-----------+  +-----------+
    """)
    print(p1[:13].center(13),p2[:13].center(13))


input(f"{p1}! If you had a look press enter:")

print("\n"*100)
print("Tell the second player to open their eyes:")
input("Press enter when the second player opens their eyes:")
print()

print("""
Tell one of the two options:
1. The carrot is in your box
2. The carrot is not in your box
""")

while True:
    response=input((f"{p2}, Would you like to swap (Y/N)?"))
    if not(response.upper()=="Y" or response.upper()=="N"):
        print("Please enter a valid response:")
    else:
         break

firstbox = "RED "
secondbox = "GOLD"
if response.upper() == "Y":
    carrotFirst = not carrotFirst
    firstbox, secondbox = secondbox, firstbox

print("Here are the contents of your boxes:")
if carrotFirst:
    print(f"""
        V  V
        |  |
    +-----------+  +-----------+
    |   |  |    |  |           |
    |           |  |           |
    +-----------+  +-----------+
    |   {firstbox}    |  |   {secondbox}  |
    |   BOX     |  |   BOX     |
    +-----------+  +-----------+
    """)
    print(p1[:13].center(13),p2[:13].center(13))

    print()
    print(f"Congrats {p1}, you are a winner baby!")

else:
    print(f"""
                            V  V
                            |  |
        +-----------+  +-----------+
        |           |  |    |  |   |
        |           |  |           |
        +-----------+  +-----------+
        |   {firstbox}    |  |   {secondbox}  |
        |   BOX     |  |   BOX     |
        +-----------+  +-----------+
        """)
    print(p1[:13].center(13),p2[:13].center(13))
    
    print()
    print(f"Congrats {p2}, you are a winner baby!")
     