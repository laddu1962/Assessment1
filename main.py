# recuperar la criatura = reclaim the creature

player_class = 0
inventory_weapons = []
inventory_items = []
inventory1 =["ID","Wallet","Keys","Pen"]


# beginning of the game and the start text
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

# the character selection for the player through number input
    while True:
        choice = int(input("Which human are you going to choose, type the number? "))
        if choice == 1:
            player_class = 1
            break
        elif choice == 2:
            player_class = 2
            break
        elif choice == 3:
            player_class = 3
            break
        else:
            print("not valid")
        continue

# telling the player which character they chose, three character types
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
# riddles made using while, giving the player as many guesses as they need. This riddle is for the soldier.
    if choice == 1:
        while True:
            answer = "war"
# call back the number from the input to decide which riddle the player will get
            guess = input("Soldier fight it but never changes? ")
            if guess == answer:
                print("gate opened")
                scene3()
            else:
                print("try again...")
# riddles for the agent option
    if choice == 2:
        while True:
            answer = "newspaper"

            guess = input("What is black, white and read all over? ")
            if guess == answer:
                print("gate opened")
                scene3()
            else:
                print("try again...")
# riddle for the scientist option
    if choice == 3:
        while True:
            answer = "ice"

            guess = input("How do you spell hard water with three letters?")
            if guess == answer:
                print("gate opened")
                scene3()
            else:
                print("try again...")


def scene3():
    print("""
You enter area 51, but there is another barrier in front of you
You have to solve 3 questions in order to enter the main building!
         
         """)
# safe cracker
    import random
    safe_code = []
# in order to progress to the next part player need to solve three division question in a row
    while len(safe_code) < 3:
        code = random.randint(3,12)
        if code not in safe_code:
            safe_code.append(code)
# the division question will vary as it can ba any number from 3-12, at random,
    # only repeats a number if the answer before was incorrect
    codes_cracked = 0
# if it is the right input these methods will carry out
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
# it is a letter then this will print
            except ValueError:
                print("That is not the number")
                break
# if zero is put in the input this will print
            except ZeroDivisionError:
                print("Can't divide by zero")
# what's printed when crack the code
    else:
        print("You have opened the door")
# are the code is cracked you will be taken into the building, this is when you are asked about directions
    print("""
You have entered the main building.
You can go right or left...
""")  # simple input for the player decided which direction they want to take
    answer = input("Where do want to go?  ")
    if answer == "right":
        scene4_right()
    elif answer == "left":
        scene4_left()

# different scenes for different directions
def scene4_right():
    print("""To your right is the laboratory,
but the door is locked. The only thing left on the 
right is an equipment locker.""")
    answer = input("Do you want to inspect the equipment room? ")

    if answer == 'yes':
        print("""You open the equipment locker. Within the locker is:
1. hazmat suit, 2. keys, 3. taser, 4. plasma gun, 5. vest, 6. hard drive

you can choose ONE item!
            """) # there are two lists thus a longer list.append
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
    elif answer == "no":
        print("""Now the only way you can go is left.
You turn around and start walking...""")
        scene4_left()
# you type in the number for the specific item you want and that number is then used to append items to you inventory
        pockets = print(inventory_items and inventory_weapons)
# there are two list one for weapons and one for non weapons for the final scene
    print("""Now the only way you can go is left.
    You turn around and start walking...""")
    scene4_left()


def scene4_left():

    print("""You have to appproach to guards. You have to be very cautious
with your actions and words, as your cover could be easily blown!
    
Do you wish to
option 1: approach to the guard first
option 2: walk straight into the room
    """)
    answer = input("which option do you choose?")
# the player gets two options and this a trick question, to rise suspicion
    if answer == "1":
        print("The guards just say hello and open the door for you.")
        scene5()
# if option 2 is selected then the player's inventory/ pockets will be printed.
    elif answer == "2":
        print("""
The 2 guards ask you stop and ask you why 
you didn't approach them first.
As it is there job to open the door for you?
Guard: 'Why are you not following protocol?'""")
        print("You to divert attention from the guards, check you pockets")
        print(inventory1)  # giving the player multiple choices to get out of the situation
        choice = input("chose an item ").lower()
        if choice == "id":
                print("guard: Alright you can go through")
        elif "wallet" or "keys" or "pen" in choice:
                print("Why are you showing us this?! ")
                print("It's fine don't walk right in next time!")
        scene5()


def scene5():
    print("""
You have entered the testing room 1604
The testing room is filled with all sorts equipment.
In the room is a chair, table and a safe.
Also ahead of you is another room which has a sign
that says 'OPS' """)
# this is the next room the player enters, again giving them two options
    answer = input("Do you want to inpsect anything in the room? yes or no? ")
# the player is asked if they want to inspect anything
    if answer == 'yes':
        print("""There are only a few things in the testing is an 
empty table, chair and a safe.""")
        answer2 = input("Do you want to inspect the safe? yes or no? ")
# the player is limited to a single choice
    elif answer == 'no':
        print("""The only place left to go is the OPS room. """)
        scene6()
# if the player says no to inspecting and to not inspecting the safe the player is taken to the OPS room
    if answer == "yes" and answer2 == "yes":
        print("""You are looking at the safe, it is a 4 digit safe,
take some good guess or try to remember any 4 digit number 
that you've seen.
    """)
# yes to inspecting the safe = player asked ulock the safe via code and code is mentioned before
        password = "1604"
        usrAttempts = 3
# the player will get three attempts to solving the code
        while usrAttempts > 0:
            guess = input("type password")
            if guess == password:
                print("""The safe contains a number of items,:
1.combat knife, 2.space spear , 3.riot shield , 4.general's mug, 5. nuclear lunch codes, 6. laser pen

you can choose ONE item!
                                            """)
                item = input("type a number>>  ")  # from the safe the player can choose more items
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
                print("Now that done, the only place left to go is the OPS room")
                scene6()  # once the player has chosen an item it will take the player to the OPS room
            usrAttempts -= 1
        else:
            print("try again")


# more trick question for the player and to throw in more suspision for the player
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
    
Sorry for wasting your time, have a good day sir""")
    elif answer == "":
        print("""Are you sure, I was just teasing! I'm sure I saw 
Moppy and Bucket guarding the door this morning.
    
You probabily have a lot on your mind, sorry for wasting.
Please go through.
    """)
    scene7()

import random
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
# this is to randomly generate different aliens, so everytime the player checks the computer it randomisess the aliens
    class Enemy:

        weapons = {"dagger": 5, "sword": 10, "lightsaber": 15}

        names = ["Biycuya", "Semboon", "keyskay", "Izen"]
        homelands = ["Mars", "Skyland", "Neenee", "RedHill"]
        ability = ["Time Travel", "The power of the sun", "Regeneration", "Reality Manipulation"]
# through the use of class different alien types are created and printed for the player
        print("""
There's a computer in front of you which could have all the information about the
being on there.""")
        first = input("Do you wish to use the computer?")
# once the player says yes to use the computer the method will run and create 4 differnt alien types
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
# this is where the stored alien types is randomised
    for i in range(4):
        name = Enemy.names[i]
        homeland = random.choice(Enemy.homelands)
        ability = random.choice(Enemy.ability)
        enemy = Enemy(name, homeland, ability)
        enemy.GetRandomWeapon()

        print("{} is from {} with the ability of {}".format(name, homeland, ability))
# once the method runs more text will print
    print("""
The one you're looking isn't here!
The only thing left to do now is to capture a human as we can access their 
memories... 

As you were searching the incubators a scientist comes in.

This is the perfect chance to take a human and use them to your advantage.

You approach the scientist and knock him out!""")
    scene8_b1()


def scene8_b1():
    print("""You can access a human's memories but they will fight back and 
the way they do it differs from species to species. 

In this species you have solve the anagram...""")
    while True:
        answer = "carbon"
# this is anagram the player has to solve and this is doen by the while loop
        guess = input("Decipher 'barcon':  ")
        if guess == answer:
            print("That's one barrier!")
            scene8_b2()
        else:
            print("Hint: It's an element")
# oen the player gets the answer wrong, a hint is given to the player to help


def scene8_b2():
    print("""You were able to take down the first barrier, but there is still
one more!

In order to overcome this barrier you must choose one of item you have collected!.
I item you have wil determine if you can fully access their memories.

As the items you collected from the physical world can be replicated in the mind, in order to fight
""")  # the end of the is where the player's inventory is printed, and then it will decide if player wins or loops
    print(inventory_weapons)
    print(inventory_items)
    choice = input("choose a weapon! ").lower()
    if choice in inventory_weapons:
        scene8_b3()  # if the player had picked up a weapon from the previous spots then the player will win
    elif inventory_weapons == 0:
        print("""
                    you don't have the right items to help you defeat his mind!


                        YOU'RE DEAD!""")
    elif choice not in inventory_weapons:
        print("""
            you don't have the right items to help you defeat his mind!


                YOU'RE DEAD!""")

# if the player chose no items or chose not to go there at all it means no weapons to fight or progess to the end

def scene8_b3():
    print("""
        you have picked the right weapon
        This gives you an advantage while you are in their mind and there
        
        You have successfully accessed their memories. As you look through their 
        memories you try to find your fellow but there seems to be nothing about him!
        
        You wake up...You are in some sort of lab with scientists and agents around you.
        An agent approach you and say 'Thank you!' 
        
        Agent Castle: 'You never broke into area 51 and you don't have fellow captured here.
        You are the one that's captured, we simply wanted to know how your species would break
        into area 51 so we could take the necessary precautions to prevent it!'
        
        Major Ray:'Let's make one thing clear you will never escape area 51 nor will I allow
        anyone to break you out!'""")
    quit()

scene1()
