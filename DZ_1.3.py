#a = int(input('введите число от 0 до 100'))
for a in range(1,101):
    if a == 1:
        print(1, 'процент')
    elif a >= 5 and a < 20:
        print(a, 'процентов')
    elif a > 1 and a < 5:
        print(a,'процента')
    elif a > 20 and a % 10 == 1:
        print(a,'процент')
    elif a > 20 and a % 10 > 1 and a % 10 < 4:
        print(a,'процента')
    elif a >20 and a % 10 == 0:
        print(a,'процентов')
    elif a > 20 and a % 10 > 4 and a % 10 < 9:
        print(a,'процентов')