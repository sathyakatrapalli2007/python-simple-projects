import random
import datetime

def get_birthdays(number_of_birthdays):
    birthdays=[]
    for i in range(number_of_birthdays):
        base_date=datetime.date(2001,1,1)
        date=base_date+datetime.timedelta(random.randint(0,364))
        birthdays.append(date)
    return birthdays

def input_loop():
    while True:
        number=input("How many birthdays shall I generate? (Max 100)")
        if number.isdecimal() and 0<int(number)<100:
            number=int(number)
            return number
        else:
            print("please give a valid number between 1 and 100")
    
def main():
        number=input_loop()
        birthdays=get_birthdays(number)
        display(birthdays)
        same_date=check_same_date(birthdays)
        if same_date:
            print("In this simulation, multiple people have a birthday on",same_date)
        else:
            print(("In this simulation, no people have birthday on same date"))
        run_simulation(number)
   

def display(birthdays):
    formatted_birthdays=[]
    months=('Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec')
    for birthday in birthdays:
        month=months[birthday.month-1]
        day=birthday.day
        formatted_birthday=f"{month} {day}"
        formatted_birthdays.append(formatted_birthday)
    print(",".join(formatted_birthdays))

def check_same_date(birthdays):
    months=('Jan','Feb','Mar','Apr','May','June','July','Aug','Sept','Oct','Nov','Dec')
    for A,birthday_A in enumerate(birthdays):
        for B,birthday_B in enumerate(birthdays[A+1:]):
            if birthday_A==birthday_B:
                return f"{months[birthday_A.month-1]} {birthday_A.day}"
    return None

def run_simulation(number):
    print(f"Generating {number} random birthdays 100,000 times...")
    print("Let's run another 100,000 simulations.")
    count=0
    for i in range(100_000):
        if i%10_000==0:
            print(f"{i} simulations run...")
        birthdays=get_birthdays(number)
        same_date=check_same_date(birthdays)
        if same_date:
            count+=1
    stats(number,count)

def stats(number,count):
    print(f"Out of 100,000 simulations of {number} people, there was a matching birthday in that group {count} times.")
    prob=(count/100_000)*100
    print(f"This means that {number} people have a {prob} % chance of having a matching birthday in their group.")
    print("That's probably more than you would think!")

main()