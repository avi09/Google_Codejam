n=int(input())
m=[]
s=[]
w=[]
for x in range(n):
    s1=input().split(' ')
    m.append(int(s1[0]))
    s.append(int(s1[1]))
    temp=[]
    for y in range(m[x]):
        s1=input()
        temp.append(s1)
    w.append(temp)

an=''
f=0
def find(tc,no_words,ch,cn,wd=''):
    global f,an
    if cn==-1:
        if wd in w[tc]:
            return
        else:
            an=wd
            f=1
            return
    else:
        for x in range(no_words):
            find(tc,no_words,ch,cn-1,wd+w[tc][x][cn])
            if f==1:
                return
        

for x in range(n):
    an='-'
    f=0
    find(x,m[x],s[x],s[x]-1)
    print('Case #'+str(x+1)+': '+an)

        
