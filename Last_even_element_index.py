n=int(input())
m=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    if m[i]%2==0:
        print(i)
        break
    