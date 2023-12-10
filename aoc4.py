import re
def analyze_nos(script):
    # Identify contiguous numbers and their positions
    parts = script[9:].split(x'|')
    winning = list(map(int,re.findall(r'\d+', parts[0])))
    n=0
    numbers = list(map(int,re.findall(r'\d+', parts[1])))
    for i in numbers:
        if i in winning:
            n += 1
    if 1:
        return n
    if n:
        return 2**(n-1)
    else:
        return 0

N=0
folder_path = 'C:\\Users\\yimqi\\Desktop\\Input.txt'
copies = [1]*190
no = []
with open(folder_path, 'r') as file:
    for ln, line in enumerate(file):
        n = analyze_nos(line)
        no.append(n)
        print(ln)
        for i in range(ln+1,min(199,ln+n+1)):
            copies[i]+=copies[ln]

print(copies,no)
print(sum(copies))

        