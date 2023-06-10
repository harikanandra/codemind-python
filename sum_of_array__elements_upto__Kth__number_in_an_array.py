n=int(input())
sum=0
l=list(map(int,input().split()))
s=int(input())
for i in range(0,s):
    sum+=l[i]
print(sum)