import math

a = []
b = []
for i in range(1, 19, 1):
    a.append(i)
for r in a:
    y = (math.sin(r) / ((15 ** 3) + (math.sqrt(r)))) + 14
    b.append(round(y, 8))
print(f'x = {a}')
print(f'y = {b}')