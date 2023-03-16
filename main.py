# welcome message
print("WELCOME TO THE MATH QUIZ")

# score
score = 0

# q1
answer1 = input("\n1 + 1 = ")
if answer1 == "2":
    print("correct")
    score += 1
else:
    print("incorrect")

# q2
answer2 = input("2 + 2 = ")
if answer2 == "4":
    print("correct")
    score += 1
else:
    print("incorrect")

# q3
answer3 = input("2 x 1 = ")
if answer3 == "2":
    print("correct")
    score += 1
else:
    print("incorrect")

# q4
answer4 = input("3 x 2 + 2 = ")
if answer4 == "8":
    print("correct")
    score += 1
else:
    print("incorrect")

# print score + message
percent = score / 4 * 100

print("SCORE:", score, "/ 4", percent,)
if score <= 2:
    print("you need to study more")
elif score > 2:
    print("good job")
