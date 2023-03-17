# welcome message
print("WELCOME TO THE MATH QUIZ")

# score
score = 0

# q1
print("\n1. 1 + 1 = __ ?")
answer1 = input("Answer: ")
if answer1 == "2":
    print("correct")
    score += 1
else:
    print("incorrect")

# q2
print("\n2. 2 + 2 = __ ?")
answer2 = input("Answer: ")
if answer2 == "4":
    print("correct")
    score += 1
else:
    print("incorrect")

# q3
print("\n3. 2 x 1 = __ ?")
answer3 = input("Answer: ")
if answer3 == "2":
    print("correct")
    score += 1
else:
    print("incorrect")

# q4
print("\n4. 3^2 = __ ?")
answer4 = input("Answer: ")
if answer4 == "9":
    print("correct")
    score += 1
else:
    print("incorrect")

# print score + message
percent = score / 4 * 100

print("SCORE:", score, "/ 4", "(", + percent, "%)")
if score <= 2:
    print("you need to study more")
elif score > 2:
    print("good job")
