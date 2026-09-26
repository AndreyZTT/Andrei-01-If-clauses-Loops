
"""This program calculates the average of 5 subject marks.

It assigns a letter grade based on the average score.
"""

print("Please enter your marks (0-100) for 5 subjects:")

mark1 = int(input("Enter mark 1: "))
mark2 = int(input("Enter mark 2: "))
mark3 = int(input("Enter mark 3: "))
mark4 = int(input("Enter mark 4: "))
mark5 = int(input("Enter mark 5: "))

for mark in [mark1, mark2, mark3, mark4, mark5]:
    if mark < 0 or mark > 100:
        print("Input error")
        break
else:

    average = (mark1 + mark2 + mark3 + mark4 + mark5) / 5
    score = ""

    if average < 60:
        score = "F"
    elif 60 <= average <= 79:
        score = "D"
    elif 80 <= average <= 89:
        score = "C"
    elif 90 <= average <= 94:
        score = "B"
    elif 95 <= average <= 100:
        score = "A"

    print(score)
