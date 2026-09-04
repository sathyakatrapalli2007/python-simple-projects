import random
import sys

#defining symbols corresponding to each suite
HEARTS=chr(9829)
DIAMONDS=chr(9830)
SPADES=chr(9824)
CLUBS=chr(9827)

def main():
    """Main Game Loop"""
    #printing the instructions
    print("""
Welome to BlackJack!!!
Rules:
 Try to get as close to 21 without going over.
 Kings, Queens, and Jacks are worth 10 points.
 Aces are worth 1 or 11 points.
 Cards 2 through 10 are worth their face value.
 (H)it to take another card.
 (S)tand to stop taking cards.
 On your first play, you can (D)ouble down to increase your bet
 but must hit exactly one more time before standing.
 In case of a tie, the bet is returned to the player.
 The dealer stops hitting at 17.
 """)
    #Starting the main game loop
    money=5000
    #initialise game loop
    while True:
        if money<=0:
            print("You have no money left")
            break
        bet=AskBet(money)
        #get the shuffled deck
        deck=GetDeck()
        #distribute the cards
        dealer_hands=[deck.pop(),deck.pop()]
        player_hands=[deck.pop(),deck.pop()]

        #if player receives more than 21 they are busted
        if getHandValue(player_hands)>21:
            print("Busted!!")
            break

        #do not show the dealer's hand
        getHands(dealer_hands,player_hands,False)
        #initialise round loop
        while True:
            move=getMove(player_hands,money)
            #Handle player actions
            if move=="d":
                if 2*bet<money:
                    bet=2*bet
                    print(f"Your bet is now increased to {bet}")
            if move=="h" or move=="d":
                new_card=deck.pop()
                card_suite,card_value=new_card
                print(f"You've drawn {card_value} of {card_suite}")
                player_hands.append(new_card)
                getHands(dealer_hands,player_hands,False)
                if getHandValue(player_hands)>21:
                    print("Busted!!")
                    break
            if move=="s" or move=="d":
                getHands(dealer_hands,player_hands,True)
                break

        #make sure that the dealer draws cards until he has atleast 17
        if getHandValue(player_hands)<=21:
            while getHandValue(dealer_hands)<=16:
                dealer_hands.append(deck.pop())

        getHands(dealer_hands,player_hands,True)

        if getHandValue(dealer_hands)>21:
            print("You win!!")
            money+=bet
            print(f"Now you have ${money}")

        elif getHandValue(player_hands)>21:
            print("You lost!!")
            money-=bet
            print(f"Now you have ${money}")  

        elif getHandValue(dealer_hands)==getHandValue(player_hands):
            print("It's a tie")           

        elif getHandValue(dealer_hands)>getHandValue(player_hands):
            print("You lost!!")
            money-=bet
            print(f"Now you have ${money}")

        elif getHandValue(player_hands)>getHandValue(dealer_hands):
            print("You win!!")
            money+=bet
            print(f"Now you have ${money}")


def AskBet(money):
    """Asking the user to bet money"""
    #looping until the user enters the correct bet value
    while True:
        print(f"Money: ${money}")
        bet=input("Enter the bet amount (press QUIT to exit):")
        #checking of the bet amount is decimal and if it is less than money
        if bet.isdecimal():
            bet=int(bet)
            if bet<=money:
                return bet
        elif bet.lower()=="quit":
            print("Thanks for playing!!")
            sys.exit()
        else:
            print(f"You don't have that much money, please choose a value lower than ${money}")

def GetDeck():
    """Creating the deck of cards"""
    deck=[]
    suites=[HEARTS,DIAMONDS,SPADES,CLUBS]
    face_cards=["A","K","Q","J"]
    for suite in suites:
        for card in range(2,11):
            deck.append((suite,card))
        for face_card in face_cards:
            deck.append((suite,face_card))
    #shuffle the deck
    random.shuffle(deck)
    return deck
    
def getHands(dealer_hands,player_hands,show_hands):
    """Check whether to show the dealer hand or not"""
    if not show_hands:
        dealer_hand=[("BACKSIDE",""),dealer_hands[1]]
        print("DEALER:","???")
        displayHands(dealer_hand)
        print("PLAYER",getHandValue(player_hands))
        displayHands(player_hands)
    else:
        print("DEALER:",getHandValue(dealer_hands))
        displayHands(dealer_hands)
        print("PLAYER",getHandValue(player_hands))
        displayHands(player_hands)

def displayHands(hand):
    """Display the hand of the dealer or player"""
    rows=["","","","",""]
    for card_suite,card_number in hand:
        card_number=str(card_number)
        if card_suite=="BACKSIDE":
            rows[0]+=" ___  "
            rows[1]+="|## | "
            rows[2]+="|###| "
            rows[3]+="|_##| "
        else:
            rows[0]+="  ___ "
            rows[1]+=" |{} | ".format(card_number.ljust(2))
            rows[2]+=" | {} | ".format(card_suite)
            rows[3]+=" |_{}| ".format(card_number.rjust(2,"_"))
    for row in rows:
            print(row)

def getHandValue(hands):
    """Calculate the value of the hands"""
    hand_value=0
    for card_suite,card_number in hands:
        if str(card_number).isalpha():
            if card_number in ["K","J","Q"]:
                    hand_value+=10
            elif card_number=="A":
                    hand_value+=1
                    if hand_value+10<21:
                        hand_value+=10
        else:
            if card_number>=2 and card_number<=10:
                hand_value+=card_number
        
    return hand_value
                
def getMove(player_hands,money):
    """Ask the player for the move"""
    #initialise the moves
    while True:
        valid_moves=["(H)it","(S)tand"]
        if len(player_hands)==2 and money>0:
            valid_moves.append("(D)oubleDown")
        print("Valid Moves:")
        movePrompt = ', '.join(valid_moves)
        print(movePrompt)
        move=input("\nEnter your move:")
        if move.lower() in ("h","s"):
            return move
        if move.lower()=="d" and "(D)oubleDown" in valid_moves:
            return move
        
if __name__=="__main__":
    main()


