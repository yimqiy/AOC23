import sys
def diff(str1, str2):
    d = 0
    for char1, char2 in zip(str1, str2):
        if char1 != char2:
            d += 1
            if d > 1: break
    return d

def tee(matrix):
    T = list(zip(*matrix))
    T = [''.join(row) for row in T]
    return T

def findmirror(a,S):
    for i in range(1,len(a)):
        s=sum(diff(p,q) for p,q in list(zip(a[:i][::-1],a[i:])))
        if s==S:
            return i
    return 0
folder_path = 'C:\\Users\\yimqi\\Desktop\\CS_MA\\AOC23\\Input.txt'
P1=P2=0
a = []
with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):
        if len(line)==1:
            P1+=100*findmirror(a,0)+findmirror(tee(a),0)
            P2+=100*findmirror(a,1)+findmirror(tee(a),1)
            a=[]
        else:
            a.append(line[:-1])

P1+=100*findmirror(a,0)+findmirror(tee(a),0)
P2+=100*findmirror(a,1)+findmirror(tee(a),1)
print(P1,P2)
