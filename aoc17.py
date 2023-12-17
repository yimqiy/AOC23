from heapq import heappop, heappush
def soln(m,mind,maxd):
    l = {}
    v = set()
    q = [(0, 0, 0, 0, 0),(0, 0, 0, 0, 1)]  # Tuple (hl,no,de, distance, dir)
    while q:
        hl, x, y, d, n = heappop(q)
        c = (x,y)
        if c not in l:
            l[c]=9e9
        l[c] = min(l[c],hl)
        
        if (c,n) in v:
            continue
        if c==(xm-1,ym-1):
            if d>=mind:
                return l[c]
        v.add((c,n))
        hlf=hlr=hll=hl
        r=[(1,0),(0,1),(-1,0),(0,-1)]
        for k in range(1,maxd+1):
            z = (k*r[(n-1)%4][0]+x,k*r[(n-1)%4][1]+y)
            if z[0]>=0 and z[1]>=0 and z[0]<xm and z[1]<ym:
                hll += m[z[1]][z[0]]
                if k>=mind: heappush(q,(hll,z[0],z[1], k, (n-1)%4))

            z = (k*r[(n+1)%4][0]+x,k*r[(n+1)%4][1]+y)
            if z[0]>=0 and z[1]>=0 and z[0]<xm and z[1]<ym:
                hlr += m[z[1]][z[0]]
                if k>=mind: heappush(q,(hlr,z[0],z[1], k, (n+1)%4))  

m=[]
folder_path = 'C:\\Users\\yimqi\\Desktop\\CS_MA\\AOC23\\Input.txt'
with open(folder_path, 'r') as file:
    m=[[*map(int, line[:-1])] for line in file]
ym = len(m)
xm = len(m[0])
print(soln(m,-1,3))
print(soln(m,4,10))