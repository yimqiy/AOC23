import re
import numpy as np
def get_nos(script):
    # Identify contiguous numbers and their positions
    l = list(map(int,re.findall(r'-?\d+', script)))
    return l
N=0
folder_path = 'C:\\Users\\yimqi\\Desktop\\Input.txt'
def diffs(seq):
    d = []
    for i in range(len(seq)-1):
        d.append(seq[i+1]-seq[i])
    if all(a == 0 for a in d):
        return 0
    else:
        print(d)
        return d[0]-diffs(d)
l = []
with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):        
        l.append(get_nos(line))
a = [3,0,6,0,9,0]
print(a[-1]+diffs(a))
for a in l:
    print(a)
    N+=a[0]-diffs(a)
print(N)