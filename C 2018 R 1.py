from itertools import combinations

n=int(input())
r=[]
c=[]
h=[]
v=[]
d=[]
nc=0
for x in range(1,n+1):
    s1=input().split(' ')
    r.append(int(s1[0]))
    c.append(int(s1[1]))
    h.append(int(s1[2]))
    v.append(int(s1[3]))
    for y in range(1,r[x-1]+1):
        s2=input()
        d.append(s2)
        for xy in range(len(s2)):
            if s2[xy]=='@':
                nc+=1
#print(d,r)
        

def div(nc,h,v):
    if nc%(h+1)*(v+1)==0:
        return 1
    else:
        return -1

def count_compare(data_array,cutlist): 
    x=0
    c=0
    y=cutlist[c]
    no_chips=[]
    while True:
        temp=0
        for i in range(x,y):
            for ii in data_array[i]:
                if ii=='@':
                    temp+=1
        no_chips.append(temp)
        if (c+1)==len(cutlist):
            break
        else:
            x=y
            c+=1
            y=cutlist[c]
            
    q=no_chips[0]
    for i in no_chips:
        if i==q:
            pass
        else:
            print('-1')
            return -1
    print('1')
    return 1
            

def hcv(data_array,hcuts,numbarray,maxr):
    comb=combinations(numbarray,hcuts)
    for i in list(comb):
        #Here we are having the possible combinations of all the horizontal cuts
        temp=list(i)
        temp.append(maxr)
        result=count_compare(data_array,temp)
        if result==1:
            print('1')
            return 1
        else:
            pass
    print('-1')
    return -1

count=0
count2=0
for i in range(1,n+1):
    count2=count2+r[i-1]
    data_array=d[count:count2]
    print(data_array)
    count=count+r[i-1]
    result=div(nc,h[i-1],v[i-1])
    if result==1:
        tlist=[]
        for x in range(1,r[i-1]):
            tlist.append(int(x))
        result=hcv(data_array,h[i-1],tlist,r[i-1])
        if result==1:
            print('possible')
    else:
        print('n')

        
        


        
