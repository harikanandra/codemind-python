n=int(input())
f=0
s=1
t=f+s
print(f,end=' ')
print(s,end=' ')
print(t,end=' ')
for i in range(2,n-1):
    f=s
    s=t
    t=f+s
    print(t ,end=' ')