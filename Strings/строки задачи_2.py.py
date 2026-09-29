#1 Строковые минимум и максимум


# text = input()

# word_max = text
# word_min = text

# while text != 'КОНЕЦ':
    
#     if text > word_max:
#         word_max = text
#     if text < word_min:
#         word_min = text
    
#     text = input()

# print(f'Минимальная строка ⬇️: {word_min}\nМаксимальная строка ⬆️: {word_max}')



# 🟠 Блок 3. Несколько слов


# for i in range(4):
#     text = input()

#     weight = 0

#     for c in text:
#         weight += ord(c)

#     print(weight)

# 2 Самое тяжёлое из двух слов

# max_weight = 0
# best_word = ''

# for i in range(2):
#     word = input()

#     weight_symbol = 0

#     for c in word:
#         weight_symbol += ord(c)

#     if weight_symbol > max_weight:
#         max_weight = weight_symbol
#         best_word = word

# print(best_word)



# 2/0 Самое тяжёлое из четырех слов

# best_word = ''
# max_weight = 0 

# for i in range(4):
#     word = input()

#     sum_symbol = 0

#     for c in word:
#         sum_symbol += ord(c)

#     if sum_symbol > max_weight:
#         max_weight = sum_symbol
#         best_word = word

# print(best_word)


# 3 while + накопители

# best_word = ''
# max_weight = 0
# word = input()

# while word != 'КОНЕЦ':
#     sum_weight = 0

#     for c in word:
#         sum_weight += ord(c)

#     if sum_weight > max_weight:
#         max_weight = sum_weight
#         best_word = word

#     word = input()

# print(best_word)



# 4 Самый лёгкий и самый тяжёлый символ


# text = input()
# largest_symbol = text[0]
# smallest_symbol = text[0]

# for c in text:
#     if ord(c) > ord(largest_symbol):
#         largest_symbol = c
#     if ord(c) < ord(smallest_symbol):
#         smallest_symbol = c

# print(smallest_symbol, largest_symbol, sep='\n')


# 5 Вывод символов от A до указанной буквы

# symbol = ord(input())

# for i in range(ord('A'), symbol + 1):
#     print(chr(i))


# 6 Следующие 5 символов

# symbol = ord(input())

# for i in range(5):
#     print(chr(symbol + i))

# 7 Сколько символов тяжелее заданного кода?

# text = input()
# unicode_code = int(input())
# count = 0

# for symbol in text:
#     if ord(symbol) > unicode_code:
#       count += 1

# print(count)

# 8 Самое тяжёлое слово до «КОНЕЦ»

# text = input()
# longest_word = ''
# max_weight = 0

# while text != 'КОНЕЦ':
#     sum_symbol = 0

#     for symbol in text:
#         sum_symbol += ord(symbol)

#     if sum_symbol > max_weight:
#         max_weight = sum_symbol
#         longest_word = text

#     text = input()

# print(f'Слово: {longest_word}\nВес: {max_weight}\nКоличество символов: {len(longest_word)}')


#9 Символ на N позиций дальше

# symbol = input()
# n = int(input())

# print(chr(ord(symbol)+n), sep='\n')




#10 Символ на N позиций назад

# symbol = input()
# n = int(input())

# print(chr(ord(symbol)- n))


# №11 Символы между двумя буквами

# symbol_1 = ord(input())
# symbol_2 = ord(input())


# for i in range(symbol_1, symbol_2+1):
#     print(chr(i))

#12 Сдвигаем каждый символ строки

# text = input()
# new_code = 0

# for symbol in text:
#     new_code = ord(symbol) + 1
#     print(chr(new_code), end='')

#13 Сдвиг строки на n

# text = input()
# n = int(input())

# for symbol in text:
#     print(chr(ord(symbol)+n), end='')

#14 Чётный или нечётный Unicode-код

# text = input()

# for symbol in text:
#     if ord(symbol) % 2 ==0:
#         print(chr(ord(symbol)+1), end='')
#     else:
#         print(chr(ord(symbol)-1), end='')

#15 Посчитай символы в диапазоне

text = input()
symbol = input()
symbol_2 = input()
count = 0





count = text[symbol:symbol_2]
print(count)
