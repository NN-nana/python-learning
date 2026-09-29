n = int(input())
flag = False
temp = n 
reversed_num = 0

while temp > 0:
    digit = temp % 10
    reversed_num = reversed_num * 10 + digit
    temp //= 10

while reversed_num > 0:
    digit1 = reversed_num % 10
    if digit1 % 2 == 0:
        print(digit1)
        flag = True
        break
    reversed_num //= 10
if not flag:
    print('НЕТ')
