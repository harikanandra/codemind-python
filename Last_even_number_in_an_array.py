n=int(input())
m=list(map(int,input().split()))
b=m[::-1]
for i in range(n):
    if b[i]%2==0:
        print(b[i])
        break
    