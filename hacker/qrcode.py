import segno

# Генерация простого QR-кода
qrcode = segno.make_qr("Hello")

qrcode.save(
    "qrcode.png", # Название и тип файла
    scale=5, # Размер картинки (модификатор размера)
    border = 10, # Размер границы
    light = "lightblue", # Цвет фона (color)
    dark = (192, 57, 43), # Цвет QR-кода (RGB)
    quiet_zone = "#eeeeee", # Цвет обводки (HEX)
    #data_dark = (44, 62, 80), # Цвет темных участков данных
    #data_light = (142, 68, 173) # Цвет светлых участков данных

) # Сохранение картинки

# Создание QR-кода с поддержкой micro QR (экономия места)
qrcode_micro = segno.make("Micro QR", micro=True)
qrcode_micro.save("micro_qrcode.png", scale=10, border=1)

# Создание QR-кода с собственным фоном.
qrcode_art = segno.make('Jack the Dog!', error='h')
qrcode_art.to_artistic(background='qr.gif', target='qrcode_art.gif', scale=5)

print("QR-коды успешно сгенерированы и сохранены.")
