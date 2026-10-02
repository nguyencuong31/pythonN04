gia1,sl1=map(float,input("hàng 1: ").split())
gia2,sl2=map(float,input("hàng 2: ").split())
gia3,sl3=map(float,input("hàng 3: ").split())
phi=float(input("Phí vận chuyển:"))
Tong=(gia1*sl1)+(gia2*sl2)+(gia3*sl3)+phi
print(Tong, "đ")
