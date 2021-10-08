import sys

cash = 1000 - int(input())

if cash < 0:
    sys.exit(1)

a = cash // 500
cash -= 500 * a
b = cash // 100
cash -= 100 * b
c = cash // 50
cash -= 50 * c
d = cash // 10
cash -= 10 * d
e = cash // 5
cash -= 5 * e
f = cash // 1

if a > 0:
    print(f'500, {a}', end="")

if b > 0 and a > 0:
    print(f'; 100, {b}', end="")
elif b > 0 and not (a > 0):
    print(f'100, {b}', end="")

if c > 0 and (a > 0 or b > 0):
    print(f'; 50, {c}', end="")
elif c > 0 and not (a > 0 or b > 0):
    print(f'50, {c}', end="")

if d > 0 and (a > 0 or b > 0 or c > 0):
    print(f'; 10, {d}', end="")
elif d > 0 and not (a > 0 or b > 0 or c > 0):
    print(f'10, {d}', end="")

if e > 0 and (a > 0 or b > 0 or c > 0 or d > 0):
    print(f'; 5, {e}', end="")
elif e > 0 and not (a > 0 or b > 0 or c > 0 or d > 0):
    print(f'5, {e}', end="")

if f > 0 and (a > 0 or b > 0 or c > 0 or d > 0 or e > 0):
    print(f'; 1, {f}', end="")
elif f > 0 and not (a > 0 or b > 0 or c > 0 or d > 0 or e > 0):
    print(f'1, {f}', end="")

print()
sys.exit(0)