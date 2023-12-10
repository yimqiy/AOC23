import re
def get_nos(script):
    # Identify contiguous numbers and their positions
    l = list(map(int,re.findall(r'\d+', script)))
    return l
N=0
folder_path = 'C:\\Users\\yimqi\\Desktop\\Input.txt'

seeds = []
almanac = []
almanac_rev = []
points = []
r=-1
l=[[],[]]
with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):
        l[ln] = get_nos(line)

points.sort()
N = 1
for i in range(1):
    a = 215106415051100
    b = 40929790
    for j in range(b):
        if j*(b-j)>a:
            N*=(1+b-2*j)
            break
print(N)