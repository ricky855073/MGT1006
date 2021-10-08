# HW0
# Date: 20210921
# Name: Ricky Hsien-Ming Liu
# ID: R09323056

import sys

n = int(input())
m = int(input())

if (n >= 1) and (n <= 1000):
    if (m >= 1) and (m <= 50):
        TA = n // m
        Teacher = n % m
        print(f'{TA},{Teacher}')
        sys.exit(0)
    else:
        sys.exit(1)
else:
    sys.exit(1)
