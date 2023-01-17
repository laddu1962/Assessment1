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
         1. solider 
         2. agent 
         3. scientist
         You have to chose one so you can transform into them,
         meaning you will become on of those humans, each which hold a different 
         rank. 
         
         Your mission is to infiltrate the humans base and reclaim our fellow,
         from their prison. You do this by becoming on of them. They won't see 
         it coming!""")

choice = int(input("Which human are you going to choose, type the number? "))

if choice == 1:
    player_class = 1
elif choice == 2:
    player_class = 2
elif choice == 3:
    player_class = 3
else:
    print("not valid")

def class_selection(x):
    if x == 1:
        print("You have selected solider")
    elif x == 2:
        print("You have selected the agent")
    elif x == 3:
        print("You have selected the scientist")

if player_class != 0:
    class_selection(player_class)




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

