n=int(input())
for i in range(0,n):
    a=input()
    b=any(map(str.isdigit,a))
    if b==True:
        print("Yes")
    else:
        print("No")