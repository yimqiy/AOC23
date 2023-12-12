folder_path = 'C:\\Users\\yimqi\\Desktop\\Input.txt'
stars=[]
frow = [1]*152
fcol = [1]*152
with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):
        for x, char in enumerate(line):
            if char == '#':
                stars.append([ln, x])
                fcol[x] = 0
                frow[ln] = 0

for i in stars:
    i[0]+=sum(frow[1:i[0]])*999999
    i[1]+=sum(fcol[1:i[1]])*999999
N=0
for i in range(len(stars)):
    for j in range(i):
        N+=abs(stars[i][1]-stars[j][1])+abs(stars[i][0]-stars[j][0])
print(N)