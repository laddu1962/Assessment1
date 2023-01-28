# recuperar la criatura = reclaim the creature
player_class = 0
inventory_weapons = []
inventory_items = []
inventory1 =["ID","Wallet","Keys","Pen"]



def scene1():
    start = print("""
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


def scene2():
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


def scene3():
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

    print("""
You have entered the main building.
You can go right or left...
""")
    answer = input("Where do want to go?  ")


def scene4_right():
    print("""To your right is the laboratory,
but the door is locked. The only thing left on the 
right is an equipment locker.""")
    answer = input("Do you want to inspect the equipment room? ")

    if answer == 'yes':
        print("""You open the equipment locker. Within the locker is:
1. hazmat suit, 2. keys, 3. taser, 4. plasma gun, 5. vest, 6. hard drive

you can choose ONE item!
            """)
        item = input("type a number>>  ")
        if item == "1":
            inventory_items.append("hazmat suit")
        elif item == "2":
            inventory_items.append("keys")
        elif item == "3":
            inventory_weapons.append("taser")
        elif item == "4":
            inventory_weapons.append("plasma gun")
        elif item == "5":
            inventory_items.append("vest")
        elif item == "6":
            inventory_items.append("hard drive")

        pockets = print(inventory_items and inventory_weapons)
    print("Now the only way you can go is left.")


def scene4_left():

    print("""You have to appproach to guards. You have to be very cautious
with your actions and words, as your cover could be easily blown!
    
Do you wish to
option 1: approach to the guard first
option 2: walk straight into the room
    """)
    answer = input("which option do you choose?")

    if answer == "option 1":
        print("The guards just say hello and open the door for you.")

    elif answer == "option 2":
        print("""
The guards ask you stop and ask you why 
you didn't approach them first.
As it is there job to open the door for you?
Guard: 'Why are you not following protocol?'""")
        print("You to divert attention from the guards, check you pockets")
        print(inventory1)
        choice = input("chose an item ").lower()
        if choice == "id":
                print("guard: Alright you can go through")
        elif "wallet" or "keys" or "pen" in choice:
                print("Why are you showing us this?! ")
                print("It's fine don't walk right in next time!")

    print("You have entered the testing room 1604")


def scene5():
    print("""
The testing room is filled with all sorts equipment.
In the room is a chair, table and a safe.
Also ahead of you is another room which has a sign
that says 'OPS' """)

    answer = input("Do you want to inpsect anything in the room? ")

    if answer == 'yes':
        print("""There are only a few things in the testing is an 
empty table, chair and a safe.""")
        answer2 = input("Do you want to inspect the safe? ")

    elif answer == 'no':
        print("""The only place left to go is the OPS room.
Do you wish to proceed?
    """)
        answer3 = input("Do you want to proceed the OPS room? ")

    if answer == "yes" and answer2 == "yes":
        print("""You are looking at the safe, it is a 4 digit safe,
take some good guess or try to remember any 4 digit number 
that you've seen.
    """)

        password = "1604"
        usrAttempts = 3

        while usrAttempts > 0:
            guess = input("type password")
            if guess == password:
                print("""The safe contains a number of items,:
                1.combat knife, 2.space spear , 3.riot shield , 4.general's mug, 5. nuclear lunch codes, 6. laser pen

                you can choose ONE item!
                                            """)
                item = input("type a number>>  ")
                if item == "1":
                    inventory_weapons.append("combat knife")
                elif item == "2":
                    inventory_weapons.append("space spear")
                elif item == "3":
                    inventory_items.append("riot shield")
                elif item == "4":
                    inventory_items.append("general's mug")
                elif item == "5":
                    inventory_weapons.append("nuclear launch code")
                elif item == "6":
                    inventory_items.append("laser pen")
                break
            usrAttempts -= 1
        else:
            print("not attempts left")


def scene6():
    print("""You walk to the door and unlock it to find a
guard standing there.  
    
Guard: How many guards were standing at the door before 
Do you wish to""")
    answer = input("type the number? ")

    if answer == "2":
        print("""I'm just teasing you, ofcourse if it is!
Moppy and Bucket are inseparable, always on duty 
together. 
    
Sorry for wasting your time, have a good day sir"""
          )
    elif answer == "1":
        print("""Are you sure, I was just teasing! I'm sure I saw 
Moppy and Bucket guarding the door this morning.
    
You probabily have a lot on your mind, sorry for wasting.
Please go through.
    """)


def scene7():
    OPS = print("""
You are in the OPS room, this room is filled with all sorts of mysterious 
things! Of all the things that could be in a room it was was other aliens,
but all of them in incubators, kept alive by machines. With no signs to 
show if any of them were alive. 

The room is filled with all sorts of machines and a spot in the room in 
the corner for cutting them open. You should look around to see if your 
fellow is in one of these incubators!  

There are 5 incubators and you should search all of them! You never know
what could be in any one of them. 
""")
    class Enemy:

        weapons = {"dagger": 5, "sword": 10, "lightsaber": 15}

        names = ["Biycuya", "Semboon", "keyskay", "Izen"]
        homelands = ["Mars", "Skyland", "Neenee", "RedHill"]
        ability = ["Time Travel", "The power of the sun", "Regeneration", "Reality Manipulation"]

        print("""
There's a computer in front of you which could have all the information about the
being on there.""")
        first = input("Do you wish to use the computer?")
# if first == "yes":
        def __init__(self, name, homeland, ability):
            self.name = name
            self.homeland = homeland
            self.ability = ability

        def Set_Bio(self, bio):
            if not isinstance(bio, str):
                print("bio must be a string")
                return
            self.bio = bio
        def Get_Bio(self):
            return self.bio
        def GetRandomWeapon(self):
            self.weapon = random.choice(list(Enemy.weapons.items()))

    for i in range(4):
        name = Enemy.names[i]
        homeland = random.choice(Enemy.homelands)
        ability = random.choice(Enemy.ability)
        enemy = Enemy(name, homeland, ability)
        enemy.GetRandomWeapon()

        print("{} is from {} with the ability of {}".format(name, homeland, ability))
# print(vars(enemy))
    print("""
The one you're looking isn't here!
The only thing left to do now is to capture a human as we can access their 
memories... 

As you were searching the incubators a scientist comes in.

This is the perfect chance to take a human and use them to your advantage.

You approach the scientist and knock him out!""")


def scene8_b1():
    print("""You can access a human's memories but they will fight back and 
the way they do it differs from species to species. 

In this species you have solve the anagram...""")

    answer = "carbon"
    usrAttempts = 3

    while usrAttempts > 0:
        guess = input("Decipher 'barcon':  ")
        if guess == answer:
            print("That's one barrier!")
            break
        usrAttempts -= 1
    else:
        print("Hint: It's an element")
        print(scene8())


def scene8_b2():
    print("""You were able to take down the first barrier, but there is still
one more!

In order to overcome this barrier you must choose one of items in front of you.
I item you choose wil determine if can access their memories.""")
    print("Everything you have collected to this point will decide if you can takedown the final barrier!"
          "As the items you collected from the pyhsical world can be replicaed in the mind, in order to fight")
    print(inventory)
    choice = input("choose a weapon! ").lower()
    if choice not in inventory:
        print("dead")
        exit()
    else:
        print("you reach down and pull the {} from your bag".format(choice))
    if "taser" or "taser" or "plasma gun" or "combat knife" or "space spear" or "nuclear lunch code" or "laser pen" in choice:
        scene8_b3()
    elif "hazmat suit" or "keys" or "vest" or "hard drive" or "riot shield" or "general's mug" in choice:
        print("""
        the weapon is weak, the monster killed you!""")


def scene8_b3():
    print("""
        you have picked the right weapon
        
        This means that you have weapon that can be used to """)

scene4_right()
scene8_b2()




