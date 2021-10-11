dividend = int(input())

if dividend < 0:
    print("exit")
else:
    divisor = int(input())
    print("error") if divisor == 0 else print(f'{dividend // divisor},{dividend % divisor}')