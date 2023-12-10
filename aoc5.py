import re
def get_nos(script):
    # Identify contiguous numbers and their positions
    l = list(map(int,re.findall(r'\d+', script)))
    return l

def seed_find(n):
    for r in reversed(almanac_rev):
        for j in r:
            if j[0]<=n:
                if j[1]>n:
                    n += j[2]
                    break
    return n
def ground_find(n):
    for r in almanac:
        for j in r:
            if j[0]<=n:
                if j[1]>n:
                    n += j[2]
                    break
    return n
N=0
folder_path = 'C:\\Users\\yimqi\\Desktop\\Input.txt'

seeds = []
almanac = []
almanac_rev = []
points = []
r=-1

with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):
        if not ln:
            l=get_nos(line)
            for i in range(int(len(l)/2)):
                seeds.append((l[2*i], l[2*i+1]))
        else:
            l = get_nos(line)
            if not len(l):
                almanac.append([])
                almanac_rev.append([])
                r +=1
            else:
                almanac[r].append((l[1],l[1]+l[2],l[0]-l[1]))
                almanac_rev[r].append((l[0],l[0]+l[2],l[1]-l[0]))
                z = seed_find(l[0])
                points.append(z)

points.sort()
N = 9e9
for j in range(len(seeds)):
    a,b = seeds[j][0],seeds[j][0]+seeds[j][1]
    print(a,b)
    for i in points:
        if i >= b:
                break
        if i >= a:
            n = ground_find(i)
            N=min(N,n)

print(seeds,N)