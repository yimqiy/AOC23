import sys
sys.setrecursionlimit(10000)
folder_path = 'C:\\Users\\yimqi\\Desktop\\CS_MA\\AOC23\\Input.txt'
M = []
with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):
        #assert# that the input is a single-width path
        M.append(line)
#assert#
S = (1,0)
E = {}
d = ((1,0,'.>'),(0,1,'.v'),(-1,0,'.<'),(0,-1,'.^'))
V = {}
W = 0
V = [[0]*141 for i in range(141)]
def dfs(s,l,c):
    x,y = s
    V[x][y] = 1
    lp = 0
    nb = 0
    lnb = 0
    if y>=ln:
        V[x][y] = 0
        return l,(x,y),l
    p = 0
    pp = []
    for i, dd in enumerate(d):
        if (i+2)%4==c: continue
        xx,yy = x+dd[0],y+dd[1]
        if M[yy][xx] != '#':
            p += 1
        if M[yy][xx] in dd[2]:
            if V[xx][yy]: continue
            ll,nb,lnb = dfs((xx,yy),l+1,i)
            pp.append([(x,y),nb,abs(l-lnb)])
            if ll > lp:
                lp = ll
    if p>1:
        for a,b,w in pp:
            if b not in E:
                E[b]=set()
            if a not in E:
                E[a]=set()
            E[b].add((a,w))
            E[a].add((b,w))
        nb = (x,y)
        lnb = l
    V[x][y]=0
    return lp,nb,lnb
p1,p2a,p2b = dfs(S,0,1)
print(p1)

def dfs_g(s,l):
    x,y = s
    V[x][y] = 1
    lp = 0
    if y>=ln:
        V[x][y] = 0
        return l
    for nb in E[s]:
        xx,yy = nb[0]
        if V[xx][yy]: continue
        ll = dfs_g(nb[0],l+nb[1])
        if ll > lp:
            lp = ll
    V[x][y]=0
    return lp
print(dfs_g(p2a,p2b))