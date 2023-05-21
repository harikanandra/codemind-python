x=int(input())
x = str(x)
if x[0] == '-':
    a = int('-' + x[-1:0:-1])
    if a >= -2147483648 and a<= 2147483647:
        print(a)
else:
    a = int(x[::-1])
    if a >= -2147483648 and a<= 2147483647:
        print(a)
    else:
        print(0)