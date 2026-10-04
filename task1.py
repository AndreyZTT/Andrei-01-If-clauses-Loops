"""This program takes an integer input representing the number of mushrooms.

It outputs the correct form of the word "гриб" in Russian, based on the
rules of Russian grammar for singular and plural forms.
"""

GenitiveSingular = "а"  # окончание для родительного падежа единственного числа
GenitivePlural = "ов"  # окончание для родительного падежа множественного числа


mushrooms = int(input("Enter the number of mushrooms: "))
last_digit = mushrooms % 10  # последняя цифра числа
last_two_digits = mushrooms % 100  # последние 2 цифры для проверки чисел 11-14

if mushrooms < 0:
    print("Input error")
else:
    if last_digit == 1 and last_two_digits != 11:
        print(mushrooms, "гриб")
    elif last_digit in [2, 3, 4] and last_two_digits not in [12, 13, 14]:
        print(mushrooms, "гриб" + GenitiveSingular)
    else:
        print(mushrooms, "гриб" + GenitivePlural)
