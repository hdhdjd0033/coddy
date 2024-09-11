alfavit_RU = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
smeshenie = int(input('Шаг шифровки'))
message = input("Сообщение для шифровки: ").upper()
itog = ''

for i in message:
    mesto = alfavit_RU.find(i)
    new_mesto = mesto + smeshenie
    if i in alfavit_RU:
        itog += alfavit_RU[new_mesto]
    else:
        itog += i

print(itog)
