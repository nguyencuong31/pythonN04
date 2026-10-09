s = int(input())
if s <= 10:
    print(s * 50000)
elif 10 <= s <= 25:
    print(s*40000)
elif 25 <= s <= 50:
    print(s * 30000)
else:
    print(s * 25000)
