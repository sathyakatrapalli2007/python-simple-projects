import random,sys,time

#check if the user has bext package
try:
    import bext
except ImportError:
    print("You do not have the bext package")
    print("Please install it")
    sys.exit()

#define constants
WIDTH,HEIGHT=bext.size()
WIDTH=WIDTH-1
colors=['red', 'green', 'yellow', 'blue', 'magenta', 'cyan', 'white']
UP_RIGHT="ur"
DOWN_RIGHT="dr"
UP_LEFT="ul"
DOWN_LEFT="dl" 
DIRECTIONS=(UP_LEFT,UP_RIGHT,DOWN_LEFT,DOWN_RIGHT)

NO_OF_LOGOS=5
PAUSE_AMOUNT=0.2

#Making dictionary keys into variables
COLOR="color"
X="x"
Y="y"
DIRECTION="direction"

def main():
    """Main function"""
    bext.clear()
    #creating logos
    logos=[]
    for _ in range(NO_OF_LOGOS):
        logos.append({
            COLOR:random.choice(colors),
            X:random.randint(0,WIDTH-3),
            Y:random.randint(0,HEIGHT-1),
            DIRECTION:random.choice(DIRECTIONS)
        })

        #making sure that the x coordinate is even
        if logos[-1][X]%2==1:
            logos[-1][X]-=1

    corner_touch=0
    while True:
        #starting the loop 
        for logo in logos:
            original_direction=logo[DIRECTION]
            bext.goto(logo[X],logo[Y])
            print("   ",end=" ") #erase the old logo
            if logo[X]==0 and logo[Y]==0:
                corner_touch+=1
                logo[DIRECTION]=DOWN_RIGHT
            elif logo[X]==WIDTH-3 and logo[Y]==0:
                corner_touch+=1
                logo[DIRECTION]=DOWN_LEFT
            elif logo[X]==0 and logo[Y]==HEIGHT-1:
                corner_touch+=1
                logo[DIRECTION]=UP_RIGHT
            elif logo[X]==WIDTH-3 and logo[Y]==HEIGHT-1:
                corner_touch+=1
                logo[DIRECTION]=UP_LEFT

            #checking the left edge
            if logo[X]==0 and logo[DIRECTION]==UP_LEFT:
                logo[DIRECTION]=UP_RIGHT
            elif logo[X]==0 and logo[DIRECTION]==DOWN_LEFT:
                logo[DIRECTION]=DOWN_RIGHT

            #checking the right edge
            if logo[X]==WIDTH-3 and logo[DIRECTION]==UP_RIGHT:
                logo[DIRECTION]=UP_LEFT
            elif logo[X]==WIDTH-3 and logo[DIRECTION]==DOWN_RIGHT:
                logo[DIRECTION]=DOWN_LEFT

            #checking the top edge
            if logo[Y]==0 and logo[DIRECTION]==UP_RIGHT:
                logo[DIRECTION]=DOWN_RIGHT
            elif logo[Y]==0 and logo[DIRECTION]==UP_LEFT:
                logo[DIRECTION]=DOWN_LEFT

            #checking the bottom edge
            if logo[Y]==HEIGHT-1 and logo[DIRECTION]==DOWN_RIGHT:
                logo[DIRECTION]=UP_RIGHT
            elif logo[Y]==HEIGHT-1 and logo[DIRECTION]==DOWN_LEFT:
                logo[DIRECTION]=UP_LEFT

            #updating the locations
            #the width is twice as height
            if logo[DIRECTION]==UP_LEFT:
                logo[X]-=2
                logo[Y]-=1
            elif logo[DIRECTION]==UP_RIGHT:
                logo[X]+=2
                logo[Y]-=1
            elif logo[DIRECTION]==DOWN_RIGHT:
                logo[X]+=2
                logo[Y]+=1
            elif logo[DIRECTION]==DOWN_LEFT:
                logo[X]-=2
                logo[Y]+=1

            if logo[DIRECTION]!=original_direction:
                logo[COLOR]=random.choice(colors)

            #draw the logos
            bext.goto(logo[X],logo[Y])
            bext.fg(logo[COLOR])
            print("DVD",end="")
            

        #display the corner bounce
        bext.goto(0,0)
        bext.fg("white")
        print("NUMBER OF CORNER BOUNCES:",corner_touch,end="")
        
        bext.goto(0,0)
        sys.stdout.flush()
        time.sleep(PAUSE_AMOUNT)


if __name__=="__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Thank you for using the program")
        sys.exit()
