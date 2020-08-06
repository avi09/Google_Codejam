ins='sccssc'
x=0
n=0
f=0
while f==0:
    if ins[x]=='c' and ins[x+1]=='s':
        ins1=''
        for y in range(len(ins)):
            if y==x:
                ins1+='s'
                ins1+='c'
            elif y==(x+1):
                h=1
            else:
                ins1+=ins[y]
        ins=ins1
        n+=1
        f=1
    x+=1

print(ins)
