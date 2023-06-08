n=int(input())
for i in range(1,n+1):
    a=int(input())
    b=list(map(int,input().split()))
    e=sorted(b)
    if b==e:
        print("0")
    else:
        print(max(b)-min(b))