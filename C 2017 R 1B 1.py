n=int(input())
d=[]
nn=[]
k=[]
s=[]
for x in range(n):
    s1=input().split(' ')
    d.append(int(s1[0]))
    nn.append(int(s1[1]))
    tm1=[]
    tm2=[]
    for y in range(nn[x]):
        s1=input().split(' ')
        tm1.append(int(s1[0]))
        tm2.append(int(s1[1]))
    k.append(tm1)
    s.append(tm2)

for x in range(n):
    tm=0
    for y in range(nn[x]):
        tm2=(d[x]-k[x][y])/s[x][y]
        if tm2>tm:
            tm=tm2
    an=d[x]/tm
    print('Case #'+str(x+1)+': '+str(an))
