account_1 = int(input())
account_2 = int(input())
exchange_rate = int(input())
transfer = int(input())

if (account_1 - transfer) < 0:
    account_2 += account_1 * exchange_rate
    account_1 = 0
else:
    account_1 -= transfer
    account_2 += transfer * exchange_rate

print(f'{account_1},{account_2}')
