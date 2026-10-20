score = 0
print("Category: Recruitment")
print("Which is not an advantage of internal sourcing recruitment?")
print("A: Time-saving")
print("B: New blood")
print("C: Less Expensive")
print("D: Motivating")

Answer = input("Your choice (A, B, C, or D): ").upper()

if Answer == "B":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is B.")
print("\nCategory: On-Boarding")
print("Which is the main purpose of On-Boarding?")
print("A: To punish employees for their mistakes")
print("B: To help new employees understand their new roles")
print("C: To reduce employee salaries")
print("D: To replace existing employees")

Answer = input("Your choice (A, B, C, or D): ").upper()

if Answer == "B":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is B.")
print("\nCategory: Employee Training and Development")
print("What is the primary purpose of employee training?")
print("A: To improve employee knowledge and skills")
print("B: To increase workplace conflicts")
print("C: To reduce employee communication")
print("D: To eliminate performance reviews")

Answer = input("Your choice (A, B, C, or D): ").upper()

if Answer == "A":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is A.")
print("\nCategory: Employee Training and Development")
print("TNA in regards to employee training stands for?")
print("A: Training Needs Answers")
print("B: Tracking Needs Analysis")
print("C: Training Needs Assessment")
print("D: Tracking Needs Assessment")

Answer = input("Your choice (A, B, C, or D): ").upper()

if Answer == "C":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The correct answer is C.")
print("\nQuiz completed!")
print("Your total score is:", score, "out of 4")

if score == 4:
    print("Excellent!")
elif score >= 2:
    print("Good!")
else:
    print("Try Again!")
