account_1 = int(input())
account_2 = int(input())
transfer = int(input())

if (account_1 - transfer) < 0:
	account_2 += account_1
	account_1 = 0
else:
	account_1 -= transfer
	account_2 += transfer

print(account_1, account_2)
