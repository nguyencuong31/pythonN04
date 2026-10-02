a,b,c=map(float,input("nhap 3 canh: ").split())
tam_giac=(a+b>c) and (a+c>b) and (b+c>a)
print(tam_giac)
