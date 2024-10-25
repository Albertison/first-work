import math

a = []
b = []
s = -9.2
while s <= 8:
    s = s + 1.2
    a.append(round(s, 2))
for i in a:
    y = ((10 * math.sin(i)) / i) + (2 ** 3)
    b.append(round(y, 2))
print(f'x = {a}')
print(f'y = {b}')