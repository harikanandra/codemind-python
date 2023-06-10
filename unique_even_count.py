n=int(input())
l=set(map(int,input().split()))
sum=0
for i in l:
    if i%2==0:
        sum+=1
print(sum)