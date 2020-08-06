import string
n=int(input())
mn=[]
mc=[]
ct=[]
def vn(n) : 
    if (n <= 1) : 
        return False
    if (n <= 3) : 
        return True
    if (n % 2 == 0 or n % 3 == 0): 
        return False
  
    i = 5
    while(i * i <= n) : 
        if (n % i == 0 or n % (i + 2) == 0) : 
            return False
        i = i + 6
  
    return True
def factors(n):    
    result = set()
    for i in range(1, int(n ** 0.5) + 1):
        div, mod = divmod(n, i)
        if mod == 0:
            result |= {i, div}
    return result
for x in range(n):
    s1=str(input())
    s1=s1.split(' ')
    mn.append(int(s1[0]))
    mc.append(int(s1[1]))
    temp=[]
    s2=input()
    s2=s2.split(' ')
    for y in range(mc[x]):
        temp.append(int(s2[y]))
    ct.append(temp)
def getf(n,nn):
    a=-1
    b=-1
    x=list(factors(n))
    for y in x:
        if y==n or y==1:
            pass
        elif vn(y)==True and y<=nn:
            if a==-1:
                a=y
            else:
                b=y
    if b==-1:
        b=a
    return a,b
for x in range(n):
    nd=[]
    no=[]
    a=-1
    b=-1
    c=-1
    d=-1
    for z in range(mc[x]):
        y=ct[x][z]
        if z==0:
            a,b=getf(y,mn[x])
        elif z==1:
            c,d=getf(y,mn[x])
            if a==c:
                nd.append(b)
                nd.append(a)
                nd.append(d)
                c=d
            elif a==d:
                nd.append(b)
                nd.append(a)
                nd.append(c)
            elif b==d:
                nd.append(a)
                nd.append(b)
                nd.append(c)
            else:
                nd.append(a)
                nd.append(b)
                nd.append(d)
                c=d
        else:
            a,b=getf(y,mn[x])
            if a==c:
                nd.append(b)
                c=b
            elif b==c:
                nd.append(a)
                c=a
    if c==-1 and d==-1:
        nd.append(a)
        nd.append(b)
    for y in nd:
        if y in no:
            pass
        else:
            no.append(y)
    no.sort()
    st='Case #'+str(x+1)+': '
    for y in nd:
        st+=string.ascii_uppercase[no.index(y)]
    print(st)
                
            
        
        
        
        


        

