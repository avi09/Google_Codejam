tc=int(input())
d=[]
ins=[]
for x in range(1,tc+1):
    s=str(input())
    d.append(int(s.split(' ')[0]))
    ins.append(str(s.split(' ')[1]))

def compute(ins):
    ins=str(ins)
    s=0
    c=1
    for x in range(len(ins)):
        if ins[x]=='S':
            s=s+c
        else:
            c=c*2
    return s
            
n=0
def ms(d,ins):
    global n
    c=compute(ins)
    if c<=d:
        return 
    else:
        x=0
        f=0
        while f==0:
            if ins[x]=='C' and ins[x+1]=='S':
                ins1=''
                f2=0
                y=0
                while y<len(ins):
                    if y==x:
                        ins1+='S'
                        ins1+='C'
                        f2=1
                        y=y+2
                    else:
                        ins1+=ins[y]
                        y=y+1
                    
                ins=ins1
                n+=1
                f=1
            x+=1
        ms(d,ins)
        
for y in range(1,tc+1):

    so=0
    for x in ins[y-1]:
        if x=='S':
            so+=1
    if so>d[y-1]:
        print('Case #'+str(y)+': IMPOSSIBLE')
    else:
        n=0
        ms(d[y-1],ins[y-1])
        print('Case #'+str(y)+': '+str(n))
    
