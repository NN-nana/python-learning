n = int(input())
reversed_num = 0
temp = n

# 1. Переворачиваем
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10  + digit
    temp //= 10

# 2. Собираем новое число из чётных цифр
result = 0
while reversed_num > 0:
    digit = reversed_num % 10
    if digit % 2 == 0:
        result = result * 10 + digit   # ← приклеиваем
    reversed_num //= 10

print(result)
