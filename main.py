# recuperar la criatura = reclaim the creature

# elements that I want in my text adventure game

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

# password
password = "0174"
usrAttempts = 3


while usrAttempts > 0:
    guess = input("type password")
    if guess == password:
        print("door opened")
        break
    usrAttempts -= 1
else:
    print("not attempts left")


# exercise 5
tarot = { 1: "The Magician", 2: "The High Priestess", 3: "The Empress", 4: "TheEmperor", 5: "The Hierophant", 6: "The Lovers", 7: "The Chariot",
          8: "Strength", 9: "The Hermit", 10: "Wheel of Fortune", 11: "Justice", 12: "The Hanged Man", 13: "Death",
          14: "Temperance", 15: "The Devil", 16: "The Tower", 17: "The Star", 18: "The Moon", 19: "The Sun",
          20: "Judgement", 21: "The World", 22: "The Fool"}

fortune = {}

fortune["past"] = tarot.pop(13)
fortune["present"] = tarot.pop(22)
fortune["future"] = tarot.pop(10)

for k, val in fortune.items():
    print("your", k, "is the", val, "card")

import  random

fortune = {"past": "", "present": "", "future": ""}

for key in fortune.keys():
    remaining_cards = list(tarot.keys())
    choice = remaining_cards[random.randint(0, len(remaining_cards)-1)]
    fortune[key] = tarot.pop(choice)

for key, value in fortune.items():
    print("Your {} is the {} card." .format(key, value))
