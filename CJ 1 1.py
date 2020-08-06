n=int(input())
a=[]
for x in range(n):
    a.append(int(input()))

for x in range(n):
    q=0
    r=a[x]
    for q in range(a[x]):
        r=a[x]-q
        ch=0
        for y in str(q):
            if y=='4':
                ch=1
                break
        if ch==1:
            pass
        else:
            for y in str(r):
                if y=='4':
                    ch=1
                    break
        
        if ch==1:
            pass
        else:
            print('Case #'+str(x+1)+': '+str(r)+' '+str(q))
            break

