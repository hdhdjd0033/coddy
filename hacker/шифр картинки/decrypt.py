from PIL import Image
from re import findall

def stega_decrypt():
    a = []
    keys = []
    img = Image.open(input("Название картинки:"))
    pix = img.load()
    f = open('keys.txt', 'r')
    y = str([line.strip() for line in f]) # Выделяем строки из файла

    for i in range(len(findall(r'\((\d+)\,', y))):
        keys.append((int(findall(r'\((\d+)\,', y)[i]), int(findall(r'\,\s(\d+)\)', y)[i])))
    for key in keys:
        a.append(pix[tuple(key)][1])
    return ''.join([chr(elem) for elem in a])


print("Ваше сообщение: ", stega_decrypt())
input()