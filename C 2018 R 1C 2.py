n=int(input())
na=[]
w=[]
mw=[]
for x in range(n):
    s1=int(input())
    na.append(s1)
    s1=input().split(' ')
    tm=[]
    for y in range(na[x]):
        tm.append(int(s1[y]))
    w.append(tm)

for x in range(n):
    an=0
    f=0
    tm=[]
    for y in range(na[x]):
        tm.append(6*w[x][y])
    mw.append(tm)
    for y in range(na[x]-1,-1,-1):
        for xy in range(y+1,na[x]):
            if mw[x][xy]-w[x][y]>=0:
                mw[x][xy]=mw[x][xy]-w[x][y]
            else:
                f=1
                break
        #print(mw[x],y)
        if f==1:
            break
        an+=1
    print('Case #'+str(x+1)+': '+str(an))
        
        
    
