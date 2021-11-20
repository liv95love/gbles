profit = int(input("Введите выручку фирмы: "))
cost = int(input("Ввести затраты: "))
if profit > cost:
    a = profit - cost
    b = a / profit
    print(f"Отличная работа. У вас {a} прибыли")
    worker = int(input("Количество сотрудников:"))
    print(f" {a / worker} для одного сотрудника")
elif profit == cost:
    print("Неплохо")
else:
    print("Плохо")
