"""
Group Name: Group 1
Group Members: Andrew Shields, Ashley Tessitore, Zahria Benjamin

Purpose: Using the provided syllabus at JMU, we calculate a
student's grade before the final exam and the final exam grade
needed to earn an A, B, C, or D in the course.
"""

import matplotlib.pyplot as plt


def final_grade(earned, final_weight, target):
    """
    Purpose: Find the final exam grade needed to reach a target overall grade.

    Variables:
        earned (float): course points earned before the final
        final_weight (float): points the final exam is worth (20)
        target (float): desired overall grade as a number

    Returns:
        float: required final exam grade in percent (0 if negative)
    """
    needed = (target - earned) / final_weight * 100
    return max(needed, 0)


# Introduction
print("This program calculates your MATH 232 grade before the final exam")
print("and the final exam grade you need for an A, B, C, or D.")
print("Enter your current averages.\n")

# Breakdown of the course
cat_names = ["Participation", "Achieve HW", "Written HW", "Exams", "Final Exam"]
cat_weights = [15, 15, 10, 40, 20]
for i in range(5):
    print(f'{cat_names[i]}: {cat_weights[i]}%')

plt.pie(percentages, labels=names)
plt.title("MATH 232 Grade Breakdown")
plt.show()

# Inputs
achieve = float(input("\nAchieve homework average: "))
written = float(input("Written homework average: "))
exams = float(input("Exam average: "))
polls = float(input("Poll and Piazza average: "))
absences = int(input("Number of absences: "))

# Attendance: first 2 absences free, then -20 points each (minimum 0)
if absences <= 2:
    attendance = 100
else:
    attendance = max(100 - 20 * (absences - 2), 0)
print("Attendance grade:", attendance)

# Pre-final grade
participation = (attendance + polls) / 2
earned = 0.15 * participation + 0.15 * achieve + 0.10 * written + 0.40 * exams
print(f"Points earned: {earned:.1f} out of 80")
print(f"Grade before the final: {earned / 80 * 100}%\n")

# Final exam needed
letters = ["A", "B", "C", "D"]
needed = [final_grade(earned, 20, 90),
          final_grade(earned, 20, 88),
          final_grade(earned, 20, 70),
          final_grade(earned, 20, 60)]

for i in range(4):
    if needed[i] > 100:
        print(f"{letters[i]}: you would need {needed[i]:.2f}% on the final. That is not possible, so aim for the next grade!")
    else:
        print(f"{letters[i]}: you need {needed[i]:.2f}% on the final.")

plt.bar(letters, needed)
plt.axhline(100, linestyle="--", label="Max possible (100%)")
plt.xlabel("Desired course grade")
plt.ylabel("Required final exam grade (%)")
plt.title("Final Exam Grade Needed")
plt.legend()
plt.show()
