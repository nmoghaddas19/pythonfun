import random

print("Welcome to the seven valleys!")
print("You are a wayfarer seeking to journey from the abode of dust to the heavenly homeland.")
print("The hosts of self and desire are following fast on your tail!")
print("Traverse the seven valleys and attain reunion with your Beloved before they catch you!")
print("You fill up your canteen from the crystal springs of divine power and set out.")
done = False
distance_travelled = 0
thirst = 0
tiredness = 0
distance_self_desire = -20
drinks_left = 5
while done == False:
    print("d. Drink from your canteen")
    print("r. Run on towards the Kingdom")
    print("w. Walk in the ways of Thy Lord")
    print("p. Pause and rest")
    print("s. Status check")
    print("q. Quit")
    answer = input("What will you do?")
    if answer.lower() == "q" or answer.lower() == "quit":
        done = True
    elif answer.lower() == "s":
        print("Distance travelled:", distance_travelled, "miles")
        print("Drinks left:", drinks_left)
        print("The hosts of self and desire are", distance_travelled - distance_self_desire, "miles behind you")
    elif answer.lower() == "p":
        tiredness = 0
        distance_self_desire = distance_self_desire + random.randrange(7, 15, 1)
        print("You are spiritually rejuvenated and ready to continue your journey")
    elif answer.lower() == "w":
        distance_travelled = distance_travelled + random.randrange(5, 13, 1)
        thirst = thirst + 1
        tiredness = tiredness + 1
        distance_self_desire = distance_self_desire + random.randrange(7, 15, 1)
        print("Distance travelled:", distance_travelled, "miles")
    elif answer.lower() == "r":
        distance_travelled = distance_travelled + random.randrange(10, 21, 1)
        thirst = thirst + 1
        tiredness = tiredness + random.randrange(1,4,1)
        distance_self_desire = distance_self_desire + random.randrange(7, 15, 1)
        print("Distance travelled:", distance_travelled, "miles")
    elif answer.lower() == "d":
        if drinks_left == 0:
            print("You take out your canteen but it's empty!")
        else:
            thirst = 0
            drinks_left = drinks_left - 1

    if thirst > 6:
        print("Your thirst became too great and you gave in to the hosts of self and desire!")
        done = True
    elif thirst > 4:
        print("You are getting thirsty!")

    if tiredness > 8 and done == False:
        print("You are so tired you can't go on")
        done = True
    elif tiredness > 5
        print("You are getting tired!")

    if distance_travelled-distance_self_desire < 0:
        print("The hosts of self and desire consumed you!")
        done = True
    elif distance_travelled-distance_self_desire < 15:
        print("The hosts of self and desire are getting close!")

    if distance_travelled > 200 and done == False:
        print("You traversed the seven valleys and entered the heavenly homeland")

    if random.random() < 1/20:
        print("You found a crystal spring of the love of God and refilled your canteen!")
        thirst = 0
        tiredness = 0
        drinks_left = 5




