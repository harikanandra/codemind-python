n=int(input())
a=list(map(int,input().split()))
s=[]
c=[]
for i in range(n//2):
    s.append(a[i])
for i in range(n//2,n):
    c.append(a[i])
print(sum(s))
print(sum(c))