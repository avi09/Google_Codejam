n=int(input())
t=[]
tl=[]
v=[]
gb=0
for x in range(n):
    s=input().split(' ')
    t.append(int(s[0]))
    tl.append(int(s[1]))
    s=input().split(' ')
    s2=[]
    for y in s:
        s2.append(int(y))
    v.append(s2)

def intr(x,y):
    a=(x/y)*100
    a=round(a)
    return a

def process(t,tl,v,r=-1):
    global gb
    if r==0:
        y=0
        for x in v:
            y+=x
        temp=0
        for x in v:
            temp+=intr(x,y)
            if temp>gb:
                gb=temp
        return
    elif r==-1:
        y=0
        for x in v:
            y+=x
        r=t-y
        for x in range(len(v)+1):
            if x<len(v):
                v[x]+=1
                process(t,tl,v,r-1)
                v[x]-=1
            else:
                v.append(1)
                process(t,tl,v,r-1)
            
        #return
    else:
        for x in range(len(v)):
            v[x]+=1
            process(t,tl,v,r-1)
            v[x]-=1
        #return
        
            
        
for x in range(n):
    process(t[x],tl[x],v[x])
    print('Case #'+str(x+1)+': '+str(gb))
    gb=0
    
