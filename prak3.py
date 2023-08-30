from operator import *
a = 1
b = 5.0
print('a = {}'.format(a))
print('b = {}'.format(b))
for func in (lt, le, eq, ne, ge, gt):
    print ('{}(a, b): {}'.format(func.__name__, func(a, b))) 

#lt = lebih kecil
#le lebih kecil dari atau setara dengan
#eq =setara dengan
#ne=tidak setara dengan
#ge = lebih besar dari atau setara dengan
#gt =lebih besar dari