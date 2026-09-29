# text = input()
# cnt_plus = 0
# cnt_zve = 0


# for c in text:
#     if c.count('+'):
#           cnt_plus += c.count('+')
#     if c.count('*'): 
#         cnt_zve += c.count('*')


# print('Символ + встречается', cnt_plus, 'раз')
# print('Символ * встречается', cnt_zve, 'раз')



# text = input().lower()

# vowels = 'ауоыиэяюе'
# consnants = 'бвгджзйклмнпрстфхцчшщ'
# cnt_vow = 0
# cnt_cons = 0

# for c in text:
#     if c in vowels:
#         cnt_vow += 1
#     elif c in consnants:
#         cnt_cons += 1

# print('Количество гласных букв равно', cnt_vow)
# print('Количество согласных букв равно', cnt_cons)


# Накручиваем стоимость ответа ⬆️


# text = input()
# cnt_sms = 0
# new_cnt_sms = 0
# eng_alpha = 'eyopaxcETOPAHXCBM'
# rus_alpha = 'еуорахсЕТОРАНХСВМ'

# for c in text:
#     cnt_sms += ord(c) * 3

# new_text = text
# for i in range(len(eng_alpha)):
#     if eng_alpha[i] in text:
#         new_text = new_text.replace(eng_alpha[i], rus_alpha[i])
    
# for k in new_text:
#     new_cnt_sms += ord(k)*3

# print(f'Старая стоимость: {cnt_sms}🐝\nНовая стоимость: {new_cnt_sms}🐝')
