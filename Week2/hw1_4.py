x = int(input())
y = int(input())

x_hun = x // 100
x_ten = (x - 100 * x_hun) // 10
x_one = x % 10

y_hun = y // 100
y_ten = (y - 100 * y_hun) // 10
y_one = y % 10

A = 0
B = 0

if x_hun == y_hun:
    A += 1
elif x_hun == y_ten:
    B += 1
elif x_hun == y_one:
    B += 1

if x_ten == y_ten:
    A += 1
elif x_ten == y_hun:
    B += 1
elif x_ten == y_one:
    B += 1

if x_one == y_one:
    A += 1
elif x_one == y_hun:
    B += 1
elif x_one == y_ten:
    B += 1

print(f'{A}A{B}B')
