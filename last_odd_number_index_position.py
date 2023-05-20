n=int(input())
s=list(map(int,input().split()))
for i in range(n-1,-1,-1):
    if s[i]%2!=0:
        print(i)
        break