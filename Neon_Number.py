n=int(input())
s=0
d=n*n
while d!=0:
    r=d%10
    d//=10
    s+=r
if s==n:
    print("Neon Number")
else:
    print("Not Neon Number")