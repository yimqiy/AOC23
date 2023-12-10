import re
import numpy as np
def get_nos(script):
    # Identify contiguous numbers and their positions
    l = list(re.findall(r'[A-Z]+', script))
    return l
def find_node(target,dirn):
    for a in l:
        if a!=[]:
            if a[0]==target:
                return a[dirn]

N=0
folder_path = 'C:\\Users\\yimqi\\Desktop\\Input.txt'

l=[]
dirs = []
As = []
with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):
        if not ln:
            for a in line:
                dirs.append(2 if a=='R' else 1)
        else:
            l.append(get_nos(line))
            try:
                if l[-1][0][2]=='A':
                    As.append(l[-1][0])
            except:
                continue
g = 'AAA'
s=0
N=[]
for g in As:
    n=0
    while g[2] != 'Z':
        if s==len(dirs)-1:
            s=0
            
        g=find_node(g,dirs[s])
        #print(g,s,dirs[s])
        s+=1
        n+=1
    N.append(n)
print(np.lcm.reduce([N]))