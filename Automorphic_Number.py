n=int(input())
a=str(n)
s=n*n
b=str(s)
if b.endswith(a):
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")