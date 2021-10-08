cash = int(input())
p_1 = int(input())
p_2 = int(input())

if cash // p_1 > 0:
    pie = 1
    cash -= p_1 * pie
if cash // p_2:
    drink = 1
    cash -= drink * p_2

print(cash)
