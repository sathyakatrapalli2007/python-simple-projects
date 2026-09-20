from datetime import date,timedelta
#initialising constants
YEAR=2026

MONTHS=("JANUARY","FEBRAUARY","MARCH","APRIL","MAY","JUNE","JULY","AUGUST",
        "SEPTEMBER","OCTOBER","NOVEMBER","DECEMBER")

HOLIDAYS={
date(YEAR,1,1):"NEW YEAR",
date(YEAR,1,26):"REPUBLIC DAY",
date(YEAR,2,14):"VALENTINE'S DAY",
date(YEAR,3,8):"INTERNATIONAL WOMEN'S DAY",
date(YEAR,4,1):"APRIL FOOL'S DAY",
date(YEAR,5,1):"LABOUR DAY",
date(YEAR,5,20):"BIRTHDAY",
date(YEAR,1,1):"NEW YEAR",
date(YEAR,6,21):"YOGA DAY",
date(YEAR,8,15):"INDEPENDENCE DAY",
date(YEAR,9,5):"TEACHER'S DAY",
date(YEAR,10,2):"GANDHI JAYANTI",
date(YEAR,10,31):"HALLOWEEN",
date(YEAR,11,14):"CHILDREN'S DAY",
date(YEAR,12,25):"CHRISTMAS",
}

#initiating loop to get valid year
while True:
    year=input("Enter a year")
    if year.isdecimal() and int(year)>0:
        year=int(year)
        break

    print("Please enter a valid year: ")

#initiating a loop to get a valid month
while True:
    month=input("Enter a vaid month(1-12):")
    if month.isdecimal():
        if 1<=int(month)<=12:
            month=int(month)
            break

    print("Please enter a valid month: ")

def getCalendar():
    #stores the multiline string text
    cal_text=""
    #display the year and month
    cal_text+=" "*34+str(year)+" "+MONTHS[month-1]+"\n"
    #display the weekdays
    cal_text+="...Sunday.....Monday....Tuesday...Wednesday...Thursday....Friday....Saturday..\n"
    week_end="+----------"*7+"+\n"
    cal_text+=week_end

    #get the current date
    currentDate=date(year,month,1)

    #get the date when it is a sunday
    while currentDate.weekday() != 6:
        currentDate-=timedelta(days=1)

    #start adding the dates
    while True:
        #create a new row for each week
        week_row=""
        for i in range(7):
            week_row+="|"+str(currentDate.day).ljust(10) 
            currentDate+=timedelta(days=1)
        #for saturday add a newline
        week_row+="|\n"
        cal_text+=week_row

        #creates the empty spaces with events
        for i in range(3):
            for j in range(7,0,-1):
                #grab the event. the days are rewinded as the cureent date is a week advance
                event=HOLIDAYS.get(date(YEAR,currentDate.month,currentDate.day)-timedelta(days=j),-1)
                #fill if present else leave empty space
                if event!=-1:
                    try:
                        cal_text+="|"+event.split()[i].ljust(10)
                    except IndexError:
                        cal_text+="|          "
                else:
                    cal_text+="|          "
            cal_text+="|\n"

        #the border after each week
        cal_text+=week_end

        #break if the month is done
        if currentDate.month!=month:
            break

    return cal_text

print(getCalendar())
