import random

print("Welcome to the seven valleys!")
print("\x1B[3m      'An exposition of the mysteries enshrined in the stages of ascent \n      for them that seek "
      "to journey unto God, the Almighty, the Ever-Forgiving' \x1B[0m")
print("You are a wayfarer seeking to journey from the abode of dust to the heavenly homeland.")
print("The hosts of self and desire are following fast on your tail!")
print("Traverse the seven valleys and attain reunion with your Beloved before they catch you!")
print("You fill up your canteen from the crystal springs of divine power and set out.")
done = False
valleys = ("search", "love", "knowledge", "unity", "contentment", "wonderment", "true poverty and absolute nothingness")
search = love = knowledge = unity = wonderment = contentment = wonderment = nothingness = False
distance_travelled = 0
thirst = 0
tiredness = 0
distance_self_desire = -20
drinks_left = 3
while done == False:
    input("Press enter to continue")
    print("What will you do?")
    print("d. Drink from your canteen")
    print("r. Run on towards the Kingdom")
    print("w. Walk in the ways of Thy Lord")
    print("p. Pause and rest")
    print("s. Status check")
    print("q. Quit")
    answer = input()
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
            print("You quenched your thirst.")

    if thirst > 6:
        print("Your thirst became too great and you gave in to the hosts of self and desire!")
        done = True
    elif thirst > 4:
        print("You are getting thirsty!")

    if tiredness > 8 and done == False:
        print("You are so tired you can't go on")
        done = True
    elif tiredness > 5:
        print("You are getting tired!")

    if distance_travelled-distance_self_desire < 0:
        print("The hosts of self and desire consumed you!")
        done = True
    elif distance_travelled-distance_self_desire < 15:
        print("The hosts of self and desire are getting close!")

    if distance_travelled > 200 and done == False:
        print("You traversed the seven valleys and entered the heavenly homeland")
        print("\x1B[3m      'Peace be upon him who concludeth this exalted journey  "
              "\n      and followeth the way of truth by the lights of guidance.' \x1B[0m")
        print()
        print("Now go read the Seven Valleys!")
        done = True
    elif distance_travelled > 175 and done == False and nothingness == False:
        print("!!!\nYou entered the valley of",valleys[6], "\n!!!")
        print("\x1B[3m      'This is the station wherein the multiplicity of all things perisheth in the wayfarer;  "
              "\n      and the divine Countenance, dawning above the horizon of eternity, riseth out of the darkness' \x1B[0m")
        nothingness = True
    elif distance_travelled > 150 and done == False and wonderment == False:
        print("!!!\nYou entered the valley of",valleys[5], "\n!!!")
        print(
            "\x1B[3m      'At every moment, he beholdeth a wondrous world and a new creation, \n      and goeth from astonishment to astonishment, and is lost in awe  "
            "\n      before the new handiwork of Him Who is the sovereign Lord of all.' \x1B[0m")
        wonderment = True
    elif distance_travelled > 125 and done == False and contentment == False:
        print("!!!\nYou entered the valley of",valleys[4], "\n!!!")
        print(
            "\x1B[3m      'He burneth away the veils of want, and with inward and outward eye \n      perceiveth within and without all things  "
            "\n      the day of “God will satisfy everyone out of His abundance.”' \x1B[0m")
        contentment = True
    elif distance_travelled > 100 and done == False and unity == False:
        print("!!!\nYou entered the valley of",valleys[3], "\n!!!")
        print("\x1B[3m      'In this station he pierceth the veils of plurality,  \n      fleeth the realms of the flesh, and ascendeth unto the heaven of unity. "
            "\n      With the ear of God he heareth; "
              "\n      with the eye of God he beholdeth the mysteries of divine creation.' \x1B[0m")
        unity = True
    elif distance_travelled > 75 and done == False and knowledge == False:
        print("!!!\nYou entered the valley of",valleys[2], "\n!!!")
        print(
            "\x1B[3m      'Gazing with the eye of absolute insight,  \n      wayfarer in this valley seeth in God’s creation "
            "\n      neither contradiction nor incongruity.' \x1B[0m")
        knowledge = True
    elif distance_travelled > 50 and done == False and love == False:
        print("!!!\nYou entered the valley of",valleys[1], "\n!!!")
        print("\x1B[3m      'The steed of this valley is pain,  \n      and if there be no pain this journey will "
              "never end.' \x1B[0m")
        love = True
    elif distance_travelled > 25 and done == False and search == False:
        print("!!!\nYou entered the valley of",valleys[0], "\n!!!")
        print("\x1B[3m      'The steed of this valley is patience;  \n      without patience the wayfarer on this "
              "journey \n      will reach nowhere and attain no goal.' \x1B[0m")
        search = True
    if random.random() < 1/20:
        print("You found a crystal spring of the love of God and refilled your canteen!")
        thirst = 0
        tiredness = 0
        drinks_left = 5




