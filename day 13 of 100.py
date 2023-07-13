print("Exam Grade Calculator")

print()
print("=======================")

name = input("Enter Your Name?: ")
school = input("Name of School?: ")
examCourse = input("Name of Course?: ")
score = float(input("Enter the possible score?: "))

print()
if score >= 90 and score <= 100:
    grade = "A+"
    message = "\033[037m WOW! That is Excellent!"


elif score >= 80 and score <= 89:
    grade = "A-"
    message = "\033[036m That is Very Good! "

elif score >= 70 and score <= 79:
    grade = "B"
    message = "\033[035m That is Good. Keep it up"

elif score >= 60 and score <= 69:
    grade = "C"
    message = "\033[034m That is a Great Attempt."

elif score >= 50 and score <= 59:
    grade = "D"
    message = "\033[033m That's a good score, though you can do better"

elif score >= 40 and score <= 49:
    grade = "E"
    message = "\033[032m You've got to sit Up. That's Bad!"

elif score <= 40:
    grade = "U"
    message = "\033[031m That is a big fail. Prep for resit."


else:
    print("Unknown score, Try again!")

print()
print("Okay! So you are ", name)
print("You're a student of ", school)
print("You have taken an exam for ", examCourse)
print("This is your score", score, "and")
print("this is your grade ", grade)
print(message)