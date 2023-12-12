import re
#ways to have sets (one indexed) at pos (zero indexed) with length remaining
def solve(pos,sets,length):
    if (pos,sets,length) in a: return a[(pos,sets,length)]
    if pos<0: return (not sets and length<=pos+1)
    n = 0
    #no fill: copy last or complete a new set
    if st[pos] in '?.' and not length: 
            if sets:  n += solve(pos-1,sets-1,l[sets-1])
            n += solve(pos-1,sets,0)
    if st[pos] in '?#' and length:
            n += solve(pos-1,sets,length-1)
    a[(pos,sets,length)] = n
    return n

folder_path = 'C:\\Users\\yimqi\\Desktop\\Input.txt'
P1=P2=0
with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):        
        l=(list(map(int,re.findall(r'-?\d+', line))))
        st = line.split()[0]
        a = {}
        w = solve(len(st)-1,len(l),0)
        P1+=w
        l = l*5
        st = (st+"?")*4 + st + '.'
        a = {}
        w = solve(len(st)-1,len(l),0)
        P2+=w
print(P1,P2)