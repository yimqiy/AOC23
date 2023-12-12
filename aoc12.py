import re
#ways to have sets (one indexed) at pos (zero indexed) with length remaining
def solve(pos,sets,length):
    if a[pos][sets][length]>=0:
        return a[pos][sets][length]
    if pos<0:
        if not sets and  length<=pos+1:
            return 1
        else:
            return 0
    n = 0
    #no fill: copy last or complete a new set
    if st[pos] == '.' or st[pos] == '?': 
        if not length: #. after this
            if sets:
                n += solve(pos-1,sets-1,l[sets-1])
            n += solve(pos-1,sets,0)
    if st[pos] == '#' or st[pos] == '?':
        if length:
            n += solve(pos-1,sets,length-1)
    a[pos][sets][length] = n
    return n
N=0
folder_path = 'C:\\Users\\yimqi\\Desktop\\Input.txt'
p2 = True
l = []
hashes = []
unknowns = []
with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):        
        l=(list(map(int,re.findall(r'-?\d+', line))))
        if p2: l = l*5
        st = line.split()[0]
        if p2:
            st = (st+"?")*4 + st + '.'
        m = max(l)
        a = [[[-1]*(m+1) for j in range(len(l)+1)] for i in range(len(st))]
        w = solve(len(st)-1,len(l),0)
        N+=w
print(N)