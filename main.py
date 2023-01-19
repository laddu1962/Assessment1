# recuperar la criatura = reclaim the creature
player_class = 0

print("""
WAKE UP! WAKE UP! WAKE UP!
         You've been asleep for long enough!
         We have a lot of questions to ask!
         If you want to see your friend again, you're going to answer me.
         How did you break into Area 51?
         
         The screen fades to black...
         
         You wake up in a dark room with three bodies on the floor;
         The bodies:
         1. soldier 
         2. agent 
         3. scientist
         You have to chose one so you can transform into them,
         meaning you will become on of those humans, each which hold a 
         different rank. 
         
         Your mission is to infiltrate the humans base and reclaim our fellow,
         from their prison. You do this by becoming on of them. They won't see 
         it coming!
         """)


choice = int(input("Which human are you going to choose, type the number? "))

# the character selection for the player
if choice == 1:
    player_class = 1
elif choice == 2:
    player_class = 2
elif choice == 3:
    player_class = 3
else:
    print("not valid")

# telling the player which character they choose
def class_selection(x):
    if x == 1:
        print("You have selected soldier")
    elif x == 2:
        print("You have selected the agent")
    elif x == 3:
        print("You have selected the scientist")

if player_class != 0:
    class_selection(player_class)


print("""
Now that's out of the way, make your way
to Area 51, reclaim our fellow. 
                         
You reach the gate of Area 51, and the soldier at the 
gate ask you a riddle..
             """)

# riddles with 3 attempts
answer = "war"
usrAttempts = 3

if choice == 1:
  while usrAttempts > 0:
    guess = input("Soldier fight it but never changes?")
    if guess == answer:
        print("gate opened")
        break
    usrAttempts -= 1
  else:
    print("he's waking up put him back under")

answer = "newspaper"
usrAttempts = 3

if choice == 2:
  while usrAttempts > 0:
    guess = input("What is black, white and read all over?")
    if guess == answer:
        print("gate opened")
        break
    usrAttempts -= 1
  else:
    print("he's waking up put him back under")

answer = "ice"
usrAttempts = 3

if choice == 3:
  while usrAttempts > 0:
    guess = input("How do you spell hard water with three letters?")
    if guess == answer:
        print("gate opened")
        break
    usrAttempts -= 1
  else:
    print("he's waking up put him back under")

print("""
You enter area 51, but there is another barrier in front of you
You have to solve 3 questions in order to enter the main building!
         
         """)

# safe cracker
import random

safe_code = []

while len(safe_code) < 3:
    code = random.randint(3,12)
    if code not in safe_code:
        safe_code.append(code)

codes_cracked = 0

while codes_cracked < len(safe_code):
    for code in safe_code:
        print("enter number, that divide to %d" % code)
        try:
            guess = float(input("type 1st number"))
            guess1 = float(input("type 2nd number"))
            result = round(guess / guess1)
            if result == code:
                print("correct")
                codes_cracked += 1


        except ValueError:
            print("That is not the number")
            break;

        except ZeroDivisionError:
            print("Can't divide by zero")

else:
    print("You have opened the door")




