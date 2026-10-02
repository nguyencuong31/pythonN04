so_dien=float(input("Nhap so dien: "))
KWH_dau= min(so_dien, 50)
KWH_con_lai= max(0, so_dien - 50)
Tong_tien_dien= (KWH_dau*1678)+(KWH_con_lai*2014)
print(Tong_tien_dien,"d")

