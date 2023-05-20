n=int(input())
a=list(map(int,input().split()))
z=a.count(0)
i=-1
for i in range(z):
    a[i]=0
for j in range(n-z):
    i+=1
    a[i]=1
for i in range(n):
    print(a[i],end=' ')