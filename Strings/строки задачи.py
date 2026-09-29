# Упражнение 1. Создайте строку, состоящую из первого, среднего и последнего символо

# str1 = "James"

# first_char = str1[0]

# # Get middle character
# # Calculate index by dividing length by 2
# res = len(str1) 
# middle_index = int(res // 2)    # Поскольку индексы должны быть целыми числами, мы делим длину на единицу, чтобы найти центральную точку. Для «Джеймса» (длина 5) 5/2 равно 2,5, что обрезает значение до индекса 2 (символ «m»).
# mid_char = str1[middle_index]
# last_char = str1[-1]
# res_str = first_char + mid_char + last_char

# print(res_str)

#2 Упражнение 2. Создайте строку, состоящую из трех средних символов

# str1 = "JhonDipPeta"

# middle_index = int(len(str1) // 2)
# new_str1 = str1[middle_index -1:middle_index+2]


# print(new_str1)

# Упражнение 3. Добавьте новую строку в середину заданной строки
# s1 = "Ault"
# s2 = "Kelly"

# new_s1 = int(len(s1)//2)
# new_s2 = s1[0:new_s1] + s2 + s1[new_s1:]

# print(new_s2)

# Упражнение 4. Создайте новую строку, состоящую из первого, среднего и последнего символов каждой входной строки.
# s1 = "America" 
# s2 = "Japan"

# first_chr_s1 = s1[0]
# first_chr_s2 = s2[0]

# mid_chr_s1 = s1[int(len(s1)//2)]
# mid_chr_s2 = s2[int(len(s2)//2)]

# last_chr_s1 = s1[-1]
# last_chr_s2 = s2[-1]

# new_s = (first_chr_s1 + first_chr_s2) + (mid_chr_s1 + mid_chr_s2) + (last_chr_s1 + last_chr_s2)
# print(new_s)

# 5 Упражнение 5. Переверните заданную строку
# str1 = "PYnative"
# print(str1[::-1])

# Упражнение 6. Найдите последнюю позицию заданной подстроки
# str1 = "Emma is a data scientist who knows Python. Emma works at google."
# print(str1.find('Emma'))

# Упражнение 7. Разделите строку по дефисам
# str1 = "Emma-is-a-data-scientist"
# sub_str1 = str1.split('-')

# for s in sub_str1:
#     print(s)

# Упражнение 8. Найдите все вхождения подстроки в заданной строке, не учитывая регистр.
# str1 = "Welcome to USA. usa awesome, isn't it?"
# str1 = str1.lower()

# print(str1.count('usa'))

# Упражнение 10. Счетчик гласных
# str1 = "Hello World"
# glas  ='aaeiouAEIOU'
# count = 0

# for c in str1:
#     if c in glas:
#         count += 1

# print(count)

# Упражнение 11. Проверка префиксов/суффиксов
# str1 = "https://google.com"
# flag = True
# if str1.startswith('https') and str1.endswith('.com'):
#     flag = True
# else:
#     flag = False

# print(flag)

# Упражнение 12. Случай обмена
# str1 = "PyThOn"
# print(str1.swapcase())

#Упражнение 13. Удалите пробелы
# str1 = " P y t h o n "
# print(str1.replace(' ',''))

# Упражнение 14. Удаление N-го символа
# str1 = "Python" 
# i = 2
# first_part = str1[:i]
# last_part = str1[i+1:]

# res = first_part + last_part
# print("After removing index", i, ":", res)

# Упражнение 15. Разделение строк

# str1 = "username@company.com"
# res = str1.partition("@")

# print("Original String:", str1)
# print("Partitioned Result:", res)

# print("Username:", res[0])

# Упражнение 16. Извлечение расширения файла.
# file_name = "report_final_v2.pdf"
# first_part = file_name.split('.')[-1]
# print(first_part)

# Упражнение 17. Первая строчная буква
# str1 = "PyNaTive"

# lower = ''
# upper = ''
# for chr in str1:
#     if chr.islower():
#         lower += chr
#     else:
#         upper += chr

# print(lower+upper)

# Упражнение 18. Подсчитайте все буквы, цифры и специальные символы в заданной строке.
# str1 = "P@#yn26at^&i5ve"
# alpha = 0
# digit = 0
# symbol = 0 

# for c in str1:
#     if c.isalpha():
#         alpha += 1
#     elif c.isdigit():
#         digit += 1
#     else:
#         symbol += 1

# print(f'Общее количество символов, цифр и знаков: Символов = {alpha}, Цифр = {digit}, Знаков = {symbol}')

# Упражнение 19. Создайте строку смешанного типа, используя чередующиеся символы.
# s1 = "Abc"
# s2 = "Xyz"

# s1_length = len(s1)
# s2_length = len(s2)

# max_length = max(s1_length, s2_length)

# ХЗ КАК РЕЛШАТЬ 

# Упражнение 20. Вычислите сумму и среднее арифметическое цифр, содержащихся в строке.
# str1 = "PYnative29@#8496"
# total = 0
# count = 0

# for c in str1:
#     if c.isdigit():
#         total += int(c)
#         count += 1

# avg = total / count

# print(total, avg)

# Упражнение 21. Подсчитайте количество вхождений всех символов в строке.
# str1 = "apple"
# char_dict = dict()

# for c in str1:
#     if c in char_dict:
#         char_dict[c] += 1
#     else:
#         char_dict[c] = 1

# print(char_dict)

# Упражнение 22. Удалите пустые строки из списка строк.
# str_list = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# print("Original list of strings:", str_list)

# new_str_list = list(filter(None, str_list))
# print(new_str_list)
    
# Упражнение 23. Удалите специальные символы/знаки препинания из строки.

# str1 = "/*Jon is @developer & musician!!"
# new_str = ''
# for c in str1:
#     if c.isalnum() or c.isspace():
#         new_str += c
# print(new_str)

# Две половинки 🌶️
# str1 = input()

# len_str1 = int(len(str1)//2)

# if len(str1) % 2 != 0:
#     len_str1 += 1

#     first_part = str1[:len_str1]
#     two_part = str1[len_str1:]

#     print(two_part+first_part)

# elif len(str1) % 2 == 0:
#     first_part = str1[0:len_str1]
#     two_part = str1[len_str1:]
    
#     print(two_part+first_part)





# Плохие комментарии 😈
  

# first_min = 'jav'
# two_midl = ''
# three_max = ''

# cnt1 = len()
# cnt2 = 0
# cnt3 = 0

# for i in range(3):
#     word = input()

#     for chr in word:




