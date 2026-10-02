nam=int(input("Nhap nam: "))
nam_nhuan=((nam%4==0)and (nam%100!=0)) or (nam%400==0)
print(nam_nhuan)
