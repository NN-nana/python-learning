# 1 first task

# text = input()

# if text.count('f') == 1:
#     print(text.find('f'))

# elif text.count('f') >= 2:
#     print(text.find('f'), text.rfind('f'))

# else:
#     print('NO')

# 2 second task
# text = input()

# x = 0 
# y = 0

# for c in text:
#     if text.count(c) >= x:
#         x = text.count(c)
#         y = c

# print(y)

# 3 three task
# text = input()

# min_char = 1000
# sub = ''

# for c in text:
#     if text.count(c) <= min_char:
#         min_char = text.count(c)
#         sub = c
# print(sub)

# 4 four task
# n = int(input())

# max_number = float('-inf')       # float('-inf') — минус бесконечность (для продвинутых)
# # best_number = 0 

# for i in range(n):
#     num = int(input())
#     if num >= max_number:
#         max_number = num

# print(max_number)

# 5 fifth task

# text = input()
# words = text.split()

# max_lenght = 0
# longest_word = ""

# for word in words:
#     if len(word) >= max_lenght:
#         max_lenght = len(word)
#         longest_word = word

# print(longest_word)

# 6 sixth task
# n = int(input())

# max_sum = 0
# best_number = 0

# for i in range(n):
#     number = int(input())

#     digit_sum = 0
#     temp = number
#     while temp > 0:
#         digit_sum += temp % 10
#         temp //= 10

#     if digit_sum > max_sum:
#         max_sum = digit_sum
#         best_number = number 

# print(best_number)

# the seventh task

# text = input()
# words = text.split()

# max_length = 0
# best_word = ''

# for word in words:
#     if word.startswith('а'):
#         if len(word) >= max_length:
#             max_length = len(word)
#             best_word = word


# print(best_word)


# the eighth task

# n = int(input())

# max_num = 0
# min_num = 1000 

# for i in range(n):
#     num = int(input())
#     if num > max_num:
#         if num < min_num:   
#         min_num = num
#         max_num = num

# print(max_num, min_num)



