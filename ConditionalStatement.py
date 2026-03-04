#simple if
age = 18

if age >= 18:
    print("You are an adult")

#if else
age = 16

if age >= 18:
    print("Adult")
else:
    print("Minor")


#else if ladder
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 70:
    print("Grade B")
else:
    print("Grade C")

#logical operator
age = 25
isStudent = True

if age < 30 and isStudent:
    print("Eligible for discount")

#ternary operator
age = 20
result = "Adult" if age >= 18 else "Minor"
print(result)
