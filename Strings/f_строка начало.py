# text = input()
# cnt_sms = 0                                  #  СТАРАЯ СТОИМОСТЬ 

# for c in text:
#     cnt_sms += ord(c) * 3

# print(f"Текст сообщения:  '{text}'\nСтоимость сообщения: {cnt_sms}🐝")


text = input()
new_text = text.replace('eyopaxcETOPAHXCBM', 'еуорахсЕТОРАНХСВМ')
cnt_sms = 0   

for c in text:
    cnt_sms += ord(c) * 3

print(f"Текст сообщения:  '{text}'\nСтоимость сообщения: {cnt_sms}🐝")



