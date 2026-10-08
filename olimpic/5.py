D,R,K,L=map(int,input().split())
Chu_vi=(D+R)*2
Coc=Chu_vi//K
Thuc_te=L//K
print((Coc+Thuc_te- 1)//Thuc_te)
