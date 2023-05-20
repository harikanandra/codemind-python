n=int(input())
a=list(map(int,input().split()))
li=[]
for i in range(n):
    if a[i]%2!=0:
        li.append(a[i])
for i in range(n):
    if a[i]%2==0:
        li.append(a[i])
print(" ".join(map(str,li)))