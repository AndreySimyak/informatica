def find_common_participants(str_1, str_2, separator=","):
    list_1 = str_1.split(separator)
    list_2 = str_2.split(separator)
    # Превращаем строки в списки с помощью метода split

    general_participants = list(set(list_1).intersection(list_2))
    # Используем set(), чтобы превратить список в мн-во и метод intersection для нахождения общих участников
    general_participants.sort()  # Сортируем список с помощью метода sort
    return general_participants  # Возвращаем список


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

participants = find_common_participants(participants_first_group, participants_second_group, "|")
print(f"Общие участники групп: {participants}")
