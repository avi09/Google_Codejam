n=int(input())
a=[]
rr=[]

for x in range(n):
    s1=input().split(' ')
    a.append(int(s1[0]))
    tm=[]
    for y in range(a[x]):
        tm.append(input())
    rr.append(tm)


def win(c1,c2):
    if c1=='S':
        if c2=='R':
            return 2
        elif c2=='S':
            return 0
        else:
            return 1
    if c1=='R':
        if c2=='P':
            return 2
        elif c2=='R':
            return 0
        else:
            return 1
    if c1=='P':
        if c2=='S':
            return 2
        elif c2=='P':
            return 0
        else:
            return 1

def maxc(rr):
    n1=0
    for x in range(len(rr)):
        if len(rr[x])>n:
            n1=len(rr[x])
    return n1
def ch(rr,n):
    if n<len(rr):
        return rr[n]
    else:
        return rr[n%len()]

def gm(rr,mv='',wn=[]):
    for x in range(maxc(rr)):
        for xy in range(len(rr)):
            cc=[]
            if xy in wn:
                pass
            elif ch(rr[xy],x) in cc:
                pass
            else:
                if len(cc)==3:
                    print(-1)
                cc.append(rr[xy][x])
        if len(cc)==2:
            ss=cc[0]+cc[1]
        else:
            ss=cc[0]
        if 'S' in ss and 'R' in ss:
            mv+='R'
        elif 'S' in ss and 'P' in ss:
            mv+='S'
        elif 'P' in ss and 'R' in ss:
            mv+='P'
        elif 'S' in ss:
            mv+='R'
        elif 'R' in ss:
            mv+='P'
        elif 'P' in ss:
            mv+='S'

        for xy in range(len(rr)):
            if win(mv[x],rr[xy][x])==1:
                wn.append(xy)
        if len(wn)==len(rr):
            print(mv)
for x in range(n):
    ab=gm(rr[x])
    if str(ab)=='None':
        print('Case #'+str(x+1)+': IMPOSSIBLE')
    else:
        print('Case #'+str(x+1)+': '+ab)

        
        
