keys = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten']
values = ['ноль', 'один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять']
num_translate = dict(zip(keys, values))

print(dict(filter(lambda x: x[1] != None, num_translate.items())))