n=int(input())
nn=[]
a=[]
q=[]
ingr=[]

for x in range(n):
    s1=input().split(' ')
    nn.append(int(s1[0]))
    a.append(int(s1[1]))
    s1=input(' ').split(' ')
    tm=[]
    for y in range(nn[x]):
        tm.append(int(s1[y]))
    q.append(tm)
    for y in range(nn[x]):
        s1=input().split(' ')
        tm=[]
        for xy in range(a[x]):
            tm.append(int(s1[xy]))
        ingr.append(tm)


        
