a,b,c = map(int, input().split())
if a == b and b == c and c == a:
    print("Tam giac Deu")
elif a == b or a == c or b == c:
    print("Tam giac Can")
elif a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a :
    print("Tam giac Vuong")
else:
    print("Tam giac Thuong")
    
