#  Задача 1: "Подсчёт пробелов"

# text = 'Hello world Python'
# print(text.count(' '))

# the end



# 🟡 Задача 2: "Подсчёт подстрок"
# text = input()

# print(text.count('abc'))
# the end

# 🔴 Задача 3: "Гласные и согласные"
text = input()

vowels = 'аеёиоуыэюяАЕЁИОУЫЭЮЯaeiouAEIOU'
consonants = 'бвгджзйклмнпрстфхцчшщъьБВГДЖЗЙКЛМНПРСТФХЦЧШЩЪЬbcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ'

vowel_count = 0
for i in vowels:
    vowel_count += text.count(i)

consonant_count = 0
for i in consonants:
   consonant_count += text.count((i))

print(vowel_count)
print(consonant_count)

# НЕ СЧИТАЕТ

# 🟢 Задача 4: "Начинается с 'http'"
# text = input()

# if text.startswith(("http://", "https://")):
#     print('YES')
# else:
#     print('NO')

# 🟡 Задача 5: "Заканчивается на '.py'"
# text = input()

# if text.endswith((".py")):
#     print('YES')
# else:
#     print('NO')

# 🔴 Задача 6: "Доменное имя"
# text = input()

# if text.endswith((".com", ".ru", ".org")):
#     print('YES')
# else:
#     print('NO')

# Задача 7: "Первое вхождение"
# text = input()
# print(text.find('o'))

# # 🟡 Задача 8: "Последнее вхождение"
# text = input()
# print(text.rfind('o')) 

# # 🔴 Задача 9: "Есть ли подстрока?"

# text = input()
# sub = input()

# if sub.find(text):
#     print('YES')
# else:
#    print('NO')

# 🟢 Задача 10: "Индекс первого вхождения"
# text = input()
# sub = input()

# print(text.index(sub))

# 🟡 Задача 11: "Индекс последнего вхождения"
# text = input()
# sub = input()

# print(text.rindex(sub))

#  Задача 12: "Замена с использованием index"

# # 🟢 Задача 13: "Убрать пробелы"
# text = ' hello world '
# print(text.strip())

# # 🟡 Задача 14: "Убрать только слева"
# text = ' hello '
# print(text.lstrip())

# # 🔴 Задача 15: "Убрать только справа"
# text = ' hello '
# print(text.rstrip())

# 🟢 Задача 16: "Замена букв"
# text = 'apple banana'
# print(text.replace('a', '@'))

# 🟡 Задача 17: "Замена слова"
# text = input()
# print(text.replace("hello", "hi")) 

# 🔴 Задача 18: "Удаление подстроки"
# text = input()
# print(text.replace("abc", ""))