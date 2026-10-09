a = int(input())
b = int(input())
n = int(input())
if a + b == n:
    print("+")
elif a - b == n:
    print("-")
elif a * b == n:
    print("*")
elif a / b == n and b != 0:
    print("/")
else:
    print("Sai")
    
