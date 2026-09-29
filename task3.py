
"""This program calculates the average of 5 subject marks.

It assigns a letter grade based on the average score.
"""

print("Please enter your marks (0-100) for 5 subjects:")

marks = []

for i in range(1, 6):  # цикл для ввода оценок по 5 предметам
    mark = int(input("Enter mark for subject: "))  # изменить при необходимости
    marks.append(mark)

for mark in marks:
    if mark < 0 or mark > 100:
        print("Input error")
        break
else:

    average = sum(marks) / 5
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
