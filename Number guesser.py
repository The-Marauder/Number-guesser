from random import randint
print("Welcome to the number guessing game,within a set number of tries and you win.(tries scale the higher the range is)")
userinputrange = int(input('Choose a number for the higher limit(lower limit will always be 1) :'))
number = randint(1,userinputrange)
userinput = 0
originaltracker = 0
if userinputrange <= 30 :
    countdown = 3
elif userinputrange <=50 :
    countdown = 4
elif userinputrange <= 100 :
    countdown = 5
elif userinputrange <= 200 :
    countdown = 6
elif userinputrange <= 500 :
    countdown = 7
elif userinputrange <= 1000 :
    countdown = 9
else :
    countdown = 14
originaltracker = countdown

while userinput != number or countdown > 0 :
    userinput = int(input("Enter a guess."))
    if(number > userinput) :
        print("Your guess was lower.")
    elif(number< userinput) :
        print("Your guess was higher.")
    elif(number == userinput) :
        print("You guessed correctly!")
        countdown = originaltracker - countdown
        print(f'You guessed it in {countdown} tries!')
        countdown = 0
    countdown -=1
    
    
    