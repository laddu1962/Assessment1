# recuperar la criatura = reclaim the creature
player_class = 0

print("""WAKE UP! WAKE UP! WAKE UP!
         You've been asleep for long enough!
         
         We have a lot of questions to ask!
         If you want to see your friend again, you're going to answer me.
         
         How did you break into Area 51?
         
         The screen fades to black...""")

print("""You wake up in a dark room with three bodies on the floor;
         The bodies:
         1. soldier 
         2. agent 
         3. scientist
         You have to chose one so you can transform into them,
         meaning you will become on of those humans, each which hold a different 
         rank. 
         
         Your mission is to infiltrate the humans base and reclaim our fellow,
         from their prison. You do this by becoming on of them. They won't see 
         it coming!""")

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


print("""Now that's out of the way, make your way
             to Area 51, reclaim our fellow. 
             
             You make your way to the human base,
             in a box created by them, which they call a 'car'
             
             You reach the gate of Area 51, and the soldier at the 
             gate ask you a riddle..""")

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
    print("not attempts left")

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
    print("not attempts left")

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
    print("not attempts left")



# safe cracker
import random

safe_code = []
# populate list
while len(safe_code) < 3:
    code = random.randint(3,12)
    if code not in safe_code:
        safe_code.append(code)

codes_cracked = 0

while codes_cracked < len(safe_code):
    for code in safe_code:
        print("enter number, that divide to %d" % code)
        try:
            guess = input("type 1st number")
            guess1 = input("type 2nd number")
            result = round(guess / guess1)
            if result == code:
                print("code cracked")
                codes_cracked += 1
        except ValueError:
            print("That is not the number")
            break;

else:
    print("You have opened the safe")


print(safe_code)

# Weapons/ items
inventory =["knife","dagger","tentacle sweeper" ]

print("you have defeat the tentacle monster")
print(inventory)

choice = input("choose your weapon! ").lower()

if choice not in inventory:
    print("dead")
    exit()

else:print("you reach down and pull a % from your bag" % choice)

if "tentacle sweeper" in choice:
    print("you have picked the right weapon")

elif "knife" or "dagger" in choice:
    print("the weapon is weak, the monster killed you!")

