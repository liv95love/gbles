# a = int(input("Enter start:"))
# b = int(input("Enter finish:"))
# day = 1
# if a > b:
#    print(day)
# while a < b:
#    а = а + (a/10) * a
#    day += 1
# print(day)

a = float(input("Введите результаты пробежки первого дня в км"))
b = float(input("Введите общий желаемый результат в км"))
result_days = 1
result_km = a
while result_km < b:
    c = result_days + 0, 1 * result_days
    result_days += 1
    result_km = a + c
print(f"Вы достигли требуемых показателей на% .d день" % result_days)
