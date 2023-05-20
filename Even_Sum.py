n=int(input())
a=list(map(int,input().split()))
s,b=0,0
for i in range(n):
    if a[i]%2==0:
        s+=a[i]
print(s)