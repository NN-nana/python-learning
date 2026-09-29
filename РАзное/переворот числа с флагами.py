n = int(input())

#1. Переворачиваем число  
reversed_num = 0
temp = n 
while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

# 2. Проверяем, идут ли цифры по возрастанию
flag = True
prev = 0    # ← предыдущая цифра (начинаем с 0, т.к. цифры >= 0)

while reversed_num > 0:
    digit = reversed_num % 10
    if digit < prev:    # ← если текущая МЕНЬШЕ предыдущей
        flag = False
    prev = digit        # ← запоминаем текущую как "предыдущую"
    reversed_num //= 10
if flag:
    print('YES')
else:
    print('NO')
