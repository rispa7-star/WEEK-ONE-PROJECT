import random
score = 0 
interview_questions = [
{
"Category": "Recruitment",
"Question": "Which is not an advantage of internal sorcing recruitment?",
"A" : "Timesaving",
"B": "Newblood",
"C": "Less Expensive",
"D": "Motivating",
 "answer": "B"
},
{
"Category": "On-Boarding",
"Question": "Which is the main purpose of On-Boarding?",
"A": "To punish employees for thier mistakes",
"B": "To help new employees understand their new roles",
"C": "To reduce employee salaries",
"D": "To replace existing employees",
 "answer": "B"
 },
{
"Category": "Employee Training and Development",
"Question": "What is the primary purpose of employee training?",
"A": "To improve employee knowledge and skills",
"B": "To increase workplace conflicts",
"C": "To reduce employee communication",
"D": "To eliminate performance reviews",
 "answer": "A"
},
{
"Question":"TNA in regards to employee training stands for?",
"A": "Training Needs Answers",
"B": "Tracking Needs Analysis",
"C": "Training Needs Assessment",
"D": "Tracking Needs Assessment",
 "answer": "C"
}
]
random.shuffle(interview_questions)
for question in interview_questions:
    print(question["Question"])
    print("A:", question["A"])
    print("B:", question["B"])
    print("C:", question["C"])
    print("D:", question["D"])

Answer = input("Your choice (A, B, C, or D): ").upper()
if Answer == question["answer"]:
        print("Awesome! Correct answer.")
        score = score + 1
else:
        print("Oops! The correct answer is", question["answer"])
