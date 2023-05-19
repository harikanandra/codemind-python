import math
p,r,t=map(int,input().split())
a=p*math.pow((1+(r/100)),t)
print(format(a,".2f"))