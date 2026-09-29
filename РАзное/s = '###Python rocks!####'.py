
#  Каждый второй предмет 🧦#   Я НЕ ПОНЯЛА КАККАКККК
# n = input()
# n1 = list(n[::2])
# print(n1)

# №2 первая итема списков  
# n = int(input())
# alpha = ('abcde')
# n1 = range(n)
# print(list(alpha[:n]))



# 11.2 Основы работы со списками

#1 numbers = [2, 0, 2, 5]
# letters = ['a', 'b']

# print(len(numbers) + len(letters))
# ответ: 6

#2 
# numbers = [2, 0, 2, 5]

# print(5 in numbers)
# print(20 not in numbers)
# answer: True TRUE

#3 
# numbers = [2, 0, 2, 5]
# print('2' in numbers)
# answer: Falsr

#4 
# browsers = ['Firefox', 'Chrome', 'Safari', 'Yandex']
# print(browsers[3] + ' + ' + browsers[1])
# answer: Yandex + Chrome

#5 
# browsers = ['Firefox', 'Chrome', 'Safari', 'Yandex']
# print(browsers[4])
# answer: IndexError: index out of range

#6
vegetables = ['свекла', 'лук', 'морковь', 'капуста']
vegetables[1] = 'перец'

print(vegetables)
# answer: свекла, перец, морковь, капуста  почему вывел ответ вместе с [' ']

