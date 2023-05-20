n=int(input())
a=list(map(int,input().split()))
s,b=0,0
for i in range(n):
    s+=a[i]
print(s)