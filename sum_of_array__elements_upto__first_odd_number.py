n=int(input())
l=list(map(int,input().split()))
sum=0
for i in l:
    if i%2==1:
        break
    sum+=i
print(sum)