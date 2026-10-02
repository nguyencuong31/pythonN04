s1,v1=map(float,input("Chặng 1: ").split())
s2,v2=map(float,input("Chặng 2: ").split())
s3,v3=map(float,input("Chặng 3: ").split())
S=s1+s2+s3
T=S/v1+v2+v3
Vtb=(v1+v2+v3)/3
print("Tổng:",S,"km",",",T,"giờ",",","TB",round(Vtb,2),"km/h")
