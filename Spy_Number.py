n=int(input())
r=0
s=1
while n>0:
    r=r+(n%10)
    s=s*(n%10)
    n//=10
if r==s:
    print("Spy Number")
else:
    print("Not Spy Number")