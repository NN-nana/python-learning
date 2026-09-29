n = int(input())
reversed_num = 0

while n > 0:
    digit = n % 10
    reversed_num = reversed_num * 10 + digit
    n //= 10

flag = False

while reversed_num > 0:
    first_digit = reversed_num % 10
    if first_digit > 5:
        print(first_digit)
        flag = True
        break
    reversed_num //= 10

if not flag:
    print('НЕТ')
    
