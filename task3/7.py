a,b = map(int, input().split())
if a == 0 :
    if b == 0 :
        print("Phuong trinh vo so nghiem")
    else:
        print("Phuong trinh vo nghiem")
else:
    print(-b / a)
    
