n=int(input())
r=[]
c=[]
rc=[]
for x in range(n):
    s1=input().split(' ')
    r.append(s1[0])
    c.append(s1[0])
    for y in range(r[x]):
        s1=input().split(' ')
        tm=[]
        for xy in range(c[x]):
            tm.append(s1[xy])
        rc.append(tm)

