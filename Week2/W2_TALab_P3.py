distance = float(input())

if distance <= 1:
    print("80.0")
elif distance > 1 and distance <= 3:
    print("120.0")
else:
    print((distance - 3) * 30 + 120)