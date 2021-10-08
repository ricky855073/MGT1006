import sys

cash = 1000 - int(input())

if cash < 0:
	sys.exit(1)

a = cash // 500
b = (cash - 500 * a) // 100
c = (cash - 500 * a - 100 * b) // 50
d = (cash - 500 * a - 100 * b - c * 50) // 10
e = (cash - 500 * a - 100 * b - c * 50 - d * 10) // 5
f = cash - 500 * a - 100 * b - c * 50 - d * 10 - e * 5

print(f'{a} {b} {c} {d} {e} {f}')
sys.exit(0)