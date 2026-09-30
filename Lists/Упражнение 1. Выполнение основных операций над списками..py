#  Напишите скрипт для выполнения следующих трех операций над заданным списком.

# Получите доступ к третьему элементу списка.
# Длина списка: Выведите общее количество элементов
# Проверьте, пуст ли список.

sample_list = [10, 20, 30, 40, 50]

# a) Access Elements
print(f"Third element: {sample_list[2]}")

# b) List Length
print(f"Length of list: {len(sample_list)}")

# c) Check if Empty
is_empty = len(sample_list) == 0
print(f"Is the list empty? {is_empty}")