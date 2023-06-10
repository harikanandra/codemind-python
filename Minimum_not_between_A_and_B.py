n=int(input())
l=list(map(int,input().split()))
a,b=map(int,input().split())
li=[]
for i in l:
    if i>=a and i<=b:
        pass
    else:
        li.append(i)
if li==[]:
    print("-1")
else:
    print(min(li))