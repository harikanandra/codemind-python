a,b=map(int,input().split())
x=max(a,b)
while x>0:
    if x%a==0 and x%b==0:
        print(x)
        break
    x=x+1