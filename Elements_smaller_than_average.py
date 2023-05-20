n=int(input())
a=list(map(int,input().split()))
sum,c=0,0
for i in range(n):
    sum+=a[i]
avg=sum//n
for i in range(n):
    if a[i]<=avg:
        c+=1
print(c)