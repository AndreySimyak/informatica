numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

index_skipped_item = 4 # Находим пропущенный элемент списка.

count_of_numbers = len(numbers) # Считаем число элементов списка.
sum_of_numbers = sum(numbers[:index_skipped_item]) + sum(numbers[index_skipped_item+1:]) # Считаем сумму элементов списка без пропущенного.
average_of_numbers = sum_of_numbers / count_of_numbers # Считаем среднее арифметическое.

numbers[index_skipped_item] = average_of_numbers # Заменяем пропущенный элемент на ср. арифметическое.
print("Измененный список:", numbers)
