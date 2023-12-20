import math
folder_path = 'C:\\Users\\yimqi\\Desktop\\CS_MA\\AOC23\\Input.txt'
g= {}
h = {}
M = {}
with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):
        a,b= line.split (' -> ')
        k=a[1:]
        if k not in M: #%
            M[k]=1
        if a[0]=='&':
            M[k]=0
        if k not in g:
            g[k] = []
        for i in b[:-1].split(', '):
            if i not in h:
                h[i] = {}
            h[i][k] = 0
            g[k].append(i)
LCM=[]
def bc(H,L,v):
    q=[('roadcaster',0,'button')]
    while q:
        w,s,inp = q[0]        
        if s:H+=1
        else: L+=1
        q = q[1:]
        if w not in g:
            continue
        if not s and w in ["jg","rh","jm","hf"]:
            LCM.append(v+1)
        if w=="roadcaster":
            s=s
        else:
            if M[w]:
                if not s:
                    if M[w]==1: #on and high
                        s=1
                        M[w]=2
                    else:
                        s=0
                        M[w]=1
                else:
                    continue
            else:
                h[w][inp] = s
                if all(h[w].values()):
                    s=0
                else:
                    s=1
        for i in g[w]:
            q.append((i,s,w))
    return H,L

H=L=0
for v in range(10000):
    H,L=bc(H,L,v)
    if v==999:
        print(H*L)
    if len(LCM)==4:
        print(math.lcm(LCM[0],LCM[1],LCM[2],LCM[3]))
        break