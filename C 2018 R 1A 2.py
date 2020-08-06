n=int(input())
r=[]
b=[]
c=[]
m=[]
s=[]
p=[]
for x in range(n):
    s1=input().split(' ')
    r.append(s1[0])
    b.append(s1[1])
    c.append(s1[2])
    for y in range(c[x]):
        s1=input().split(' ')
        m.append(s1[0])
        s.append(s1[1])
        p.append(s1[2])

count1=0
count2=0

for x in range(n):
    count2=count2+c[x]
    mtemp=[]
    stemp=[]
    ptemp=[]
    for y in range(count1,count2):
        mtemp.append(m[y])
        stemp.append(s[y])
        ptemp.append(p[y])
    for y in range(r[x]):
        
        
