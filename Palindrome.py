def palindrome(n):
    r,d=0,0
    s=n
    while n>0:
        r=n%10
        d=d*10+r
        n//=10
    if s==d:
        return d
    else:
        return 0
    
a=int(input())
b=palindrome(a)
if b==a:
    print(True)
else:
    print(False)

