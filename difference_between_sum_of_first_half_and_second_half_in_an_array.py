n=int(input())
l=list(map(int,input().split()))
li=[]
s=[]
for i in range(n//2):
    li.append(l[i])
for j in range(n//2,n):
    s.append(l[j])
a=sum(li)
b=sum(s)
print(abs(a-b))