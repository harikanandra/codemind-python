number =input()
reverse=number[::-1]
number_sqr=int(number)**2
reverse_sqr=int(reverse )**2
if int(number_sqr )==int(str(reverse_sqr)[::-1]):
   print(True)
else:
   print(False)