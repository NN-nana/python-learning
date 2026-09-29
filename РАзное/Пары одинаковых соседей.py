# 1 Пары одинаковых соседей

# text = input()




# 1.1 "Доступ к символу"

# text = input()

# print(text[0:1])
# print(text[-1:])


# 1.2 Второй и предпоследний
# text = input()

# print(text[1])
# print(text[-2])

# 1.3 Символ по номеру
# text = input()
# n = int(input())

# print(text[n])


# 2.1 Каждый символ с номером

# text = input()

# for i in range(len(text)):
#     print(i, text[i])

# 2.2 Каждый символ с номером

# text = input()
# result = ''

# for i in range(len(text)):
#     if i % 2 == 0:
#         result += text[i]


# print(result)
        

# text = input()
# result = ''

# for i in range(len(text)):
#     if i % 3 == 0:
#         result += text[i]

# print(result)

# 2.2 "Только чётные позиции"

# text = input()
# result = ''

# for i in range(len(text)):
#     if i % 2 == 0:
#         result += text[i]

# print(result)


# 2.3 Символы в обратном порядке
# text = input()
# result = ''

# for i in range(len(text) -1, -1, -1):
#     result += text[i]

# print(result)

# Задача 3.1: "Соседи"

# text = input()

# for i in range(len(text)-1):
#     print(text[i] + text[i+1])

# Задача 3.2: "Одинаковые соседи" 
# text = input()
# cnt_para = 0

# for i in range(len(text)-1):
#     if text[i] == text[i+1]:
#         cnt_para += 1

# print(cnt_para)

# 🔴 Задача 3: "Гласные и согласные"

# text = input().lower()
# vovels = 'а, у, о, ы, и, э, я, ю, е'   #нужно убирать пробелы и запятые чтобы не было ошибок 

# consonants = 'б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ'
# cnt_vovel = 0
# cnt_const = 0

# for c in text:
#     if c in vovels:
#         cnt_vovel += 1
#     elif c in consonants:
#         cnt_const += 1


# print('Количество гласных букв равно', cnt_vovel)
# print('Количество согласных букв равно', cnt_const)

# Задача 4: "Удаление цифр"

text = input()
cnt = ''

for c in text:
    if not c.isdigit():
        cnt += c
if c.isdigit():
    
print(cnt)
