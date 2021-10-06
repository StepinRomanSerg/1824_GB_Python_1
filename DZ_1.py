duration = int(input('введите количество секунд '))
sec = duration % 60
min = duration // 60 % 60
hour = duration // 3600 % 24
day = duration // 86400
if duration < 60:
    print(sec, 'сек')
elif 60 <= duration and duration < 3600:
    print(min, 'мин', sec, 'сек')
elif 3600 < duration and duration < 86400:
    print(hour, 'час', min, 'мин', sec, 'сек')
elif 86400 <= duration:
    print(day, 'дн', hour, 'час', min, 'мин', sec, 'сек')

