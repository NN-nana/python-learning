n = int(input())
flag = True

while n > 0:
    digit = n % 10
    if digit % 2 != 0:
        glag = False 
    n //= 10

if flag:
    print('YES')
else:
    print('NO')