tien=int(input("Số tiền:"))
to_500=tien// 500
to_200=(tien%500)// 200
to_100=((tien%500)%200)//100
print("Số tờ 500:", to_500)
print("Số tờ 200:", to_200)
print("Số tờ 100:", to_100)
