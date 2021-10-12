a = []
for i in range(1, 1000, 2):
    a.append(i**3)
print(a)

sum = 0
for b in a:
    sum_c = 0
    for d in str(b):
        sum_c += int(d)
    if sum_c % 7 == 0:
        sum += 1
print(sum)