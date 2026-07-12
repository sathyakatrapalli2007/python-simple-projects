import random
print("I am thinking of a 3-digit number. Try to guess what it is.")
print("Here are some clues:")
print("""When I say: That means:
         Pico        One digit is correct but in the wrong position.
         Fermi       One digit is correct and in the right position.
         Bagels      No digit is correct.
""")

def guess_number(NUM_DIGITS):
    number=''
    numbers=[0,1,2,3,4,5,6,7,8,9]
    random.shuffle(numbers)
    for i in range(NUM_DIGITS):
        number+=str(numbers[i])
    return number

def main():
    answer="yes"
    while answer=='yes':
        MAX_GUESSES=10
        NUM_DIGITS=3
        num=guess_number(NUM_DIGITS)
        print("I have thought up a number.")
        print(f"You have {MAX_GUESSES} guesses to get it.")
        for guess in range(1,MAX_GUESSES+1): 
            user_guess=input(f"Guess#{guess}: ")
            if len(user_guess)==NUM_DIGITS and user_guess.isdigit():
                user_guess=int(user_guess)
                clues=clue_check(num,user_guess)
                crct=correct_answer_check(clues)
                if crct:
                    print("You got it!")
                    print("Correct number is",num)
                    break
                elif not crct and guess<MAX_GUESSES:
                    print(" ".join(clues))
                    print(f"Guesses left: {MAX_GUESSES-guess}")
                else:
                    print("Out of guess!!")
                    print("Correct number is",num)
            else:
                print("enter a number of three digits")
                    
        answer=input("Do you want to play again? (yes or no)")
    print("Thanks for playing")
    
def clue_check(num,user_guess):
    clues=[]
    user_guess_list=list(str(user_guess))
    num_list=list(num)
    for i in range(3):
        if user_guess_list[i]==num_list[i]:
            clues.append("Fermi")
        elif user_guess_list[i] in num_list:
            clues.append("Pico")
    if not clues:
        clues.append("Bagels")
    clues.sort()
    return clues

def correct_answer_check(clues):
    correct_answer=['Fermi','Fermi','Fermi']
    return clues==correct_answer

main()