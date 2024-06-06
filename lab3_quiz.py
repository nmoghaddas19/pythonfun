score = 0
total_questions = 3
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

# end of quiz
input("That's the end of the quiz! Press enter to see your score")
print("Your final score was", score*100/total_questions, "%")


