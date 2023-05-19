n=int(input())
c=1
for i in range(1,n):
    if i*i==n:
        print(True)
        c+=1
        break

if i>c and i*i!=n:
    print(False)