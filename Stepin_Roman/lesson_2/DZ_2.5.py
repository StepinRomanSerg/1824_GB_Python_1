price = [55.3, 60, 98.7, 147, 35, 90.3, 500, 15.8, 3, 23.5]
b = ''
big_price = []
print(id(price))
#Вывести на экран эти цены через запятую в одну строку, цена должна отображаться в виде <r> руб <kk> коп
# (например «5 руб 04 коп»). Подумать, как из цены получить рубли и копейки,
# как добавить нули, если, например, получилось 7 копеек или 0 копеек (должно быть 07 коп или 00 коп).


for i in price:
    str_num = str(i).split(".")
    r = str_num[0]
    kk = f'{str_num[-1]:0<2}' if len(str_num) > 1 else '00'
    b += (f'"{r} руб. {kk} коп."')
print(b)


#Вывести цены, отсортированные по возрастанию,
# новый список не создавать (доказать, что объект списка после сортировки остался тот же).
price.sort()
for i in price:
    str_num = str(i).split(".")
    r = str_num[0]
    kk = f'{str_num[-1]:0<2}' if len(str_num) > 1 else '00'
    print(f'"{r} руб. {kk} коп."', id(price))


#Создать новый список, содержащий те же цены, но отсортированные по убыванию.
price_rev = price[::-1]
for i in price:
    str_num = str(i).split(".")
    r = str_num[0]
    kk = f'{str_num[-1]:0<2}' if len(str_num) > 1 else '00'
    print(f'"{r} руб. {kk} коп."',id(price_rev), id(price))

#Вывести цены пяти самых дорогих товаров.
# Сможете ли вывести цены этих товаров по возрастанию, написав минимум кода?
big_price.sort()
for i in price:
    if i <= 500 and i >= 60:
        str_num = str(i).split(".")
        r = str_num[0]
        kk = f'{str_num[-1]:0<2}' if len(str_num) > 1 else '00'
        print(f'"{r} руб. {kk} коп."')
