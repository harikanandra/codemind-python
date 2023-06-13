num =int(input())  
sqrt_num = num // 2  
while sqrt_num * sqrt_num > num:  
    sqrt_num = (sqrt_num + num // sqrt_num) // 2  
if sqrt_num * sqrt_num == num:  
    print("True")  
else:  
    print("False")  