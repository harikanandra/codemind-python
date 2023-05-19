n=int(input())
r,s=0,0
p=1
while n>0:
    r=n%10
    s=s+r
    p=p*r
    n=n//10
if p==s:
    print("Spy Number")
else:
    print("Not Spy Number")