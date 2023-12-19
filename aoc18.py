
folder_path = 'C:\\Users\\yimqi\\Desktop\\CS_MA\\AOC23\\Input.txt'
with open(folder_path, 'r') as file:
    x=y=0
    xx=yy=0
    h1=[]
    h2=[]
    for line in file:
        a, b, c = line.split(" ")
        g = {'R':(1,0),'D':(0,1),'L':(-1,0),'U':(0,-1)}
        x += int(b)*g[a][0]
        y += int(b)*g[a][1]
        b = int(c[2:-3],base=16)
        a = int(c[-3])
        g=list(g.values())
        xx += int(b)*g[a][0]
        yy += int(b)*g[a][1]
        h1.append((x,y))
        h2.append((xx,yy))

for v in [h1,h2]:
    area = 0
    for i in range(len(v)):
        x1, y1 = v[i]
        x2, y2 = v[(i + 1) % len(v)]
        area += x1 * y2 - x2 * y1
        if y2 > y1:
            area += 2*(y2-y1)
        if x1 > x2:
            area += 2*(x1-x2)
    area += 2
    area = abs(area) // 2
    print(area)