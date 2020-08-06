n=int(input())
nn=[]
k=[]
c=[]
d=[]
for x in range(n):
    s1=input().split(' ')
    nn.append(int(s1[0]))
    k.append(int(s1[1]))
    s1=input().split(' ')
    tm=[]
    for y in range(nn[x]):
        tm.append(int(s1[y]))
    c.append(tm)
    tm=[]
    s1=input().split(' ')
    for y in range(nn[x]):
        tm.append(int(s1[y]))
    d.append(tm)

t=0
for x in range(n):
    tm1=[]
    an=0
    f=0
    for y in range(nn[x]):
        for xy in range(nn[x]):
            a=min(y,xy)
            b=max(y,xy)
            #print(a,b)
            if not([a,b] in tm1):
                f=0
                cm=-1
                dm=-1
                for i in range(a,b+1):
                    if c[x][i]>cm:
                        cm=c[x][i]
                for i in range(a,b+1):
                    if d[x][i]>dm:
                        dm=d[x][i]
                if abs(cm-dm)<=k[x]:
                    pass
                else:
                    f=1
                if f==0:
                    tm1.append([a,b])
                    an+=1
                    
    #print(tm1)
    print('Case #'+str(x+1)+': '+str(an))
