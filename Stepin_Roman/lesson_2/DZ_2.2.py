weather = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
weather_1 = ''
for i in weather:
    if i[-1].isdigit():
        item_1 = ''
        plus = ''
        if int(i) >= 17:
            i = f'"{i}"'
        for a in i:
            if a.isdigit():
                item_1 = item_1 + a
            else:
                plus = a
        num = int(item_1)
        if num < 10:  # добавили к значениям 0
            i = f'"{plus}0{item_1}"'
    weather_1 += i + ' '
print(weather_1)