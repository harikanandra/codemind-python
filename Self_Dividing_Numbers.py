n=int(input())
m=int(input())
L = []
for i in range(n,m+1):
    d = list(str(i))
    m = len(d)
    if '0' in d:
    	continue
    j = 0
    while j < m and i%int(d[j]) == 0:
    	j += 1
    if j == m:
    	    L.append(i)
x=" ".join(map(str,L))
print(x)