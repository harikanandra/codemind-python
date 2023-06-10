n=int(input())
c=0
l=list(map(int,input().split()))
for i in range(n):
    if i%2==0 and l[i]%2==0:
        c+=1
s=len(l)
if s%2==0:
    a=s//2
else:
    a=(s//2)+1
if c==a:
    print(True)
else:
    print(False)