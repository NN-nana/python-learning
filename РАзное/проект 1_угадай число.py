import random

secret_number = random.randint(1, 100)  # случайное число от 1 до 100 (включительно)

guess = int(input('Угадай число от 1 до 100: '))

while guess != secret_number:
    if guess < secret_number:
        print("Загаданное число больше твоего.")
    elif guess > secret_number:
        print("Загаданное число меньше твоего.")
    guess = int(input('Угадай число от 1 до 100: '))
else:
    print("Поздравляю! Ты угадал!")
    
       
