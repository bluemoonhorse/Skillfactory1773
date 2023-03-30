# словарь {} список []
per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
deposit = []
# ввод денег
print("Введите размер вклада: ")
money = float(input())

# расчет депозита
for x in per_cent:
    cash = per_cent[x]*money
    deposit.append(cash)
    # проверка заработка
    # print("Банк ", x, "_"*5, cash)

# распечатка депозита по заданию "deposit = [5600, 5900, 4280, 4000] "
print("deposit = ", deposit)
print("_"*60)
# Добавьте в программу поиск максимального значения и его вывод на экран
max_deposit = max(deposit)
# Максимальная сумма, которую вы можете заработать — deposit[i]
print("Максимальная сумма, которую вы можете заработать: ", max_deposit)

# лучший процент и лучшие банки.
# max_percent = max(per_cent.values())
# best_banks = [i for i, j in per_cent.items() if j == max_percent]
# print("Под процент: ", max_percent)
# print("В банках: ", best_banks)


