import csv  # Импортируем csv-файл.
import json  # Импортируем json-файл.


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    with open(INPUT_FILENAME) as file:  # Открываем файл с начальными данными.
        line = [row for row in csv.DictReader(file)]
        # C помощью DictReader из csv-строк получаем словари.
        # C помощью цикла for перебираем полученные словари.
        # # Создаем список с помощью встроенного модуля List Comprehension.

        with open(OUTPUT_FILENAME, "w") as f:  # Открываем файл, чтобы запсать результаты в режиме редактированния.
            json.dump(line, f, indent=4)  # С помощью метода dump запишем полученные результаты в json-файл.
            # Делаем отступы равными 4 пробелам.


if __name__ == '__main__':
    # Нужно для проверки.
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
