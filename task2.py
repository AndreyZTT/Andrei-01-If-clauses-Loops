"""This program calculates the final amount after applying discounts.

They are based on the user's purchases and the current purchase amount.
"""

purchases = int(input("Накопления: "))
current_purchase = int(input("Текущая сумма покупки: "))
discount = 0  # скидка
final_amount = 0  # окончательная сумма покупки


if purchases < 0 or current_purchase < 0:
    print("Input error")
else:
    if purchases < 500:
        discount = 0
    elif 500 <= purchases <= 999:
        discount = 5
    elif 1000 <= purchases <= 4999:
        discount = 10
    elif purchases >= 5000:
        discount = 15

    if current_purchase > 1000:
        discount += 10
    elif current_purchase > 300:
        discount += 5

    final_amount = current_purchase - (current_purchase * discount / 100)

    print("Итоговая скидка: ", discount, "%")
    print("К оплате: ", final_amount)
