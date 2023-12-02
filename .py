# Input: Score obtained by the student
score = float(input("Enter the score: "))

# Decision Making
if score >= 90:
    grade = "A"
elif 80 <= score <= 89:
    grade = "B"
elif 70 <= score <= 79:
    grade = "C"
elif 60 <= score <= 69:
    grade = "D"
else:
    grade = "F"

# Output: Display the grade
print(f"The grade for the score {score} is: {grade}")

90
