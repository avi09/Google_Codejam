n=int(input())

def process(a,b,n,mid=-1):
    if mid==-1:
        mid=int((a+b+1)/2)
        if mid==a:
            mid+=1
        print(mid,flush=True)
    else:
        if mid==a:
            mid+=1
        print(mid,flush=True)
        
    s=input()
    if s=='CORRECT':
        return
    elif s=='TOO_SMALL':
        a=mid
        mid=int((a+b+1)/2)
        process(a,b,n,mid)
        return
    else:
        b=mid
        mid=int((a+b+1)/2)
        process(a,b,n,mid)
        return
    
for x in range(n):
    h=input().split(' ')
    a=int(h[0])
    b=int(h[1])
    tr=int(input())
    process(a,b,tr)
