n = input()
s = len(n)
counter = 0

for i  in range(s):
    if s[i] in (0,1,2,3,4,5,6,7,8,9):
        counter += 1

print(counter)
