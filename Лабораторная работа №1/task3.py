list_players = ["Маша", "Петя", "Саша", "Оля", "Кирилл", "Коля"]

middle_index = len(list_players) // 2 # Находим индекс середины.

first_team = list_players[:middle_index] # Распределяем игроков по командам с помощью слайсирования.
second_team = list_players[middle_index:]

print(first_team)
print(second_team)
