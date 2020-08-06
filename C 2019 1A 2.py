n=int(input())
nn=[]
w=[]
for x in range(n):
    nn.append(int(input()))
    tm=[]
    for y in range(nn[x]):
        tm.append(input())
    w.append(tm)

def sub(ss,wd):
    if ss in wd:
        if wd[wd.index(ss):]==ss:
            return 1
    return -1
for x in range(n):
    ss=[]
    sw=[]
    n=0
    for y in range(nn[x]):
        if w[x][y] in sw:
            pass
        else:
            for xy in range(len(w[x][y])):
                for i in range(nn[x]):
                    if i==y:
                        pass
                    else:
                        if not(w[x][y][xy:] in ss):
                            if (w[x][y][xy:] in w[x][i]) and sub(w[x][y][xy:],w[x][i])==1:
                                ss.append(w[x][y][xy:])
                                sw.append(w[x][y])
                                sw.append(w[x][i])
                                #print(ss)
                                #print(sw)
                                n+=2
    print('Case #'+str(x+1)+': '+str(n))
                        
                        
        
