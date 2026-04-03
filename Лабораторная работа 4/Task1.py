import json  # Импортируем json-файл.

def task() -> float:
    with open('input.json') as file:  # Открываем файл для чтенния по умолчанию.
        data_set = json.load(file)
        # C помощью метода load выполняем чтение данных из файла и десериализацию их в объект Python.

    sum_values = sum([(item["score"] * item["weight"]) for item in data_set])
    # Запишем сумму произведений данных словарей по ключам score и weight.
    # Создаем список с помощью встроенного модуля List Comprehension.
    # Используем цикл for для пребора всех значений.
    return round(sum_values, 3)  # Возвращаем значение, округленное до 3 знаков после запятой.


print(task())  # Выводим полученный результат.
