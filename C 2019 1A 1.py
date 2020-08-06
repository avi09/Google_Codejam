n=int(input())
r=[]
c=[]
for x in range(n):
    s1=input().split(' ')
    r.append(int(s1[0]))
    c.append(int(s1[1]))

def chns(x1,y1,x2,y2):
    
    if x1==x2:
        return -1
    elif y1==y2:
        return -1
    elif x1+y1==x2+y2:
        return -1
    elif x1-y1==x2-y2:
        return -1
    else:
        return 1
def trav(r,c,n,cr,tr,tc,m=[[0,0]]):
    print(r+1,c+1)
    if cr==n:
        return m
    else:
        for x in range(tr):
            for y in range(tc):
                if chns(r,c,x,y)==1 and not([x,y] in m):
                    print(r+1,c+1,x+1,y+1)
                    tm=[x,y]
                    m.append(tm)
                    trav(x,y,n,cr+1,tr,tc,m)
                    
                    
for x in range(n):
    m=trav(0,0,r[x]*c[x],0,r[x],c[x])
    if len(m)==r[x]*c[x]:
        print('Case #'+str(x+1)+': POSSIBLE')
        for x in range(len(m)):
            print(str(m[x][0]+1)+' '+str(m[x][1]+1))
    elif r[x]==0 or c[x]==0:
        print('Case #'+str(x+1)+': POSSIBLE')
    else:
        print('Case #'+str(x+1)+': IMPOSSIBLE')
            
        
                    
            
            
    
