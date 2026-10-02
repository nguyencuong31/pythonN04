N=int(input())
Ngay=N//86400
Gio=(N%86400)//3600
Phut=((N%86400)%3600)//60
Giay=((N%86400)%3600)%60
print(Ngay,Gio,Phut,Giay, sep=":")
