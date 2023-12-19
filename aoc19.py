import copy
folder_path = 'C:\\Users\\yimqi\\Desktop\\CS_MA\\AOC23\\Input.txt'
P1=P2=0
g= {}
z = 0
ma = {'x':0,'m':1,'a':2,'s':3}
with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):
        if z:
            v=[]
            for u in line[1:-2].split(","):
                a,b = u.split('=')
                v.append(int(b))
            w = 'in'
            while True:
                if w=='R':
                    break
                if w=='A':
                    P1+=(sum(v))
                    break
                for k in g[w]:
                    a,b,c,d = [i for i in k]
                    if b==2:
                        if v[a]>c:
                            w = d
                            break
                    elif b==1:
                        if v[a]<c:
                            w = d
                            break
                    else:
                        w=d
                        break
                
        else:
            if len(line)<2:
                z = 1
                continue
            i,n = line.split("{")
            if i not in g:
                g[i]=[]
            for r in n.split(","):
                if ":" in r:
                    ab,c = r.split(":")
                    if '<' in ab:
                        a, b = ab.split("<")
                        g[i].append((ma[a],1,int(b),c))
                    else:
                        a, b = ab.split(">")
                        g[i].append((ma[a],2,int(b),c))
                else:
                    g[i].append((-1,0,0,r[:-2]))
print(P1)
ranges = {'in':[[[1,4000],[1,4000],[1,4000],[1,4000]]]}

w = 'in'
q = [w]
while len(q):
    w = q[0]
    q = q[1:]
    
    if w=='R':
        continue
    if w=='A':
        continue
    x = w
    for k in g[w]:
        a,b,c,d = [i for i in k]
        if d not in ranges:
            ranges[d]=[]
        j = copy.deepcopy(ranges[w])
        j2 = copy.deepcopy(ranges[w])
        q.append(d)
        if b==2:
            for r in range(len(j)):
                j[r][a][0] = c+1
                j2[r][a][1] = c
                ranges[d].append(j[r])
                ranges[w][r]=j2[r]
        elif b==1:
            for r in range(len(j)):
                j[r][a][1] = c-1
                j2[r][a][0] = c
                ranges[d].append(j[r])
                ranges[w][r]=j2[r]
        else:
            for i in copy.deepcopy(ranges[w]):
                ranges[d].append(i)
            ranges[w] = []
for g in ranges['A']:
    n = 1
    for u in g:
        n *= (u[1]+1-u[0])
    P2+=n
print(P2)