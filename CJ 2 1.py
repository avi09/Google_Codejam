n=int(input())
dm=[]
mv=[]
for x in range(n):
    dm.append(int(input()))
    mv.append(input())

pd=[]
nd=''
flag=0
def prevmotion(mv,dm):
    a=0
    b=0
    pd.append([a,b])
    count=2*dm-2
    for x in range(count):
        if mv[x]=='E':
            a+=1
        else:
            b+=1
        tm=[a,b]
        pd.append(tm)

xy=''
def sd(a,b,m,mv):
    
    if m==1:
        if (a+1)<=(mv-1):
            tm=[a,b]
            if tm in pd:
                ps=pd.index(tm)
                tm2=[tm[0]+1,tm[1]]
                if int(pd[ps+1][0])==int(tm2[0]) and int(pd[ps+1][1])==int(tm2[1]):
                    return -1
                else:
                    return 1
            else:
                return 1
    if m==2:
        if (b+1)<=(mv-1):
            tm=[a,b]
            if tm in pd:
                ps=pd.index(tm)
                tm2=[tm[0],tm[1]+1]
                if int(pd[ps+1][0])==int(tm2[0]) and int(pd[ps+1][1])==int(tm2[1]):
                    return -1
                else:
                    return 1
            else:
                return 1
            

def motion(mv,a=0,b=0,nd=''):
    global pd,flag,xy
    print(a,b)
    if a==(mv-1) and b==(mv-1):
        xy=nd
        return
    else:
        if sd(a,b,1,mv)==1:
            nd+='E'
            a+=1
            motion(mv,a,b,nd)
        if sd(a,b,2,mv)==1:
            nd+='S'
            b+=1
            motion(mv,a,b,nd)
        return

        
for x in range(n):
    pd=[]
    nd=''
    xy=''
    flag=0
    #prevmotion(mv[x],dm[x])
    #nd=motion(mv=dm[x])
    #print(pd)
    for y in range(len(mv[x])):
        if mv[x][y]=='E':
            xy+='S'
        else:
            xy+='E'
    print('Case #'+str(x+1)+': '+str(xy))
