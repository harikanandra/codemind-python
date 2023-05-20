n=int(input())
a=list(map(int,input().split()))
sum=0
for i in range(n):
    sum+=a[i]
avg=sum/n;
print("%.2f" %avg)