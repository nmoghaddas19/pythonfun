score = 0
total_questions = 6
# question 1
print("Question 1/", total_questions)
print("What is the capital city of Argentina?")
print("a. Bogota")
print("b. Caracas")
print("c. Quito")
print("d. Lima")
answer = input("Answer:")
if answer.lower() == "d" or answer.lower() == "lima":
    print("No, that's the capital of Peru!")
elif answer.lower() == "c" or answer.lower() == "quito":
    print("No, that's the capital of Ecuador!")
elif answer.lower() == "b" or answer.lower() == "caracas":
    print("No, that's the capital of Venzuela!")
elif answer.lower() == "a" or answer.lower() == "bogota":
    print("Yes, that's right!")
    score = score + 1

# question 2
input("Press enter to see the next question")
print("Question 2/", total_questions)
print("What is 7^3?")
answer = float(input("Answer:"))
if answer == 343:
    print("Yes, that's right!")
    score = score + 1
else:
    print("No, its 343!")

# question 3
input("Press enter to see the next question")
print("Question 3/", total_questions)
print("Which type of flower did 'Abdu'l-Baha give to Leroy Ioas?")
print("a. Red rose")
print("b. White rose")
print("c. Red carnation")
print("d. White carnation")
answer = input("Answer:")
if answer.lower() == "a" or answer.lower() == "red rose":
    print("No, it was a white carnation!")
elif answer.lower() == "b" or answer.lower() == "white rose":
    print("No, it was a white carnation!")
elif answer.lower() == "c" or answer.lower() == "red carnation":
    print("No, it was a white carnation")
elif answer.lower() == "d" or answer.lower() == "white carnation":
    print("Yes, that's right!")
    score = score + 1

# question 4
input("Press enter to see the next question")
print("Question 4/", total_questions)
print("Fill in the blank:")
print("God, verily, loveth those women and men who show forth ___.")
print("a. Truthfulness")
print("b. Righteousness")
print("c. Patience")
print("d. Love")
answer = input("Answer:")
if answer.lower() == "a" or answer.lower() == "truthfulness":
    print("No, it's patience!")
elif answer.lower() == "b" or answer.lower() == "righteousness":
    print("No, it's patience!")
elif answer.lower() == "d" or answer.lower() == "love":
    print("No, it was a white carnation")
elif answer.lower() == "c" or answer.lower() == "patience":
    print("Yes, that's right!")
    score = score + 1

# question 5
input("Press enter to see the next question")
print("Question 5/", total_questions)
print("Fill in the blank:")
print("Be ye as the ___ of one hand, the members of one body.")
print("a. Veins")
print("b. Fingers")
print("c. Skin")
print("d. Bones")
answer = input("Answer:")
if answer.lower() == "a" or answer.lower() == "veins":
    print("No, it's patience!")
elif answer.lower() == "c" or answer.lower() == "skin":
    print("No, it's patience!")
elif answer.lower() == "d" or answer.lower() == "bones":
    print("No, it was a white carnation")
elif answer.lower() == "b" or answer.lower() == "fingers":
    print("Yes, that's right!")
    score = score + 1

# question 6
input("Press enter to see the next question")
print("Question 6/", total_questions)
print("This statement is false")
print("a. True")
print("b. False")
print("c. Both?")
print("d. Neither")
answer = input("Answer:")
if answer.lower() == "a" or answer.lower() == "true":
    print("It can't be true because if its true that the statement is false then its false")
elif answer.lower() == "b" or answer.lower() == "false":
    print("It can't be false because if its false that the statement is false then its true")
elif answer.lower() == "c" or answer.lower() == "both" or answer.lower() == "both?":
    print("Something can't be true and false at the same time!")
elif answer.lower() == "b" or answer.lower() == "neither":
    print("Yes, that's the only possibility")
    score = score + 1

# end of quiz
input("That's the end of the quiz! Press enter to see your score")
print("Your final score was", 100*score/total_questions, "%")


