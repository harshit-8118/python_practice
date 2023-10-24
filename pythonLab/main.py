''' testing 1 on modules '''

# import calculator as cc

# print(cc.add(4, 5))
# print(cc.mul(4, 5))
# print(cc.div(40, 3))
# print(cc.sub(3, 5))

# a = cc.A()
# print(type(a))
# print(cc.constant)


# from calculator import (add, sub) #filter import
 
# # print(globals())
# print(add(5, 16))
# print(sub(5, 16))


'''     testing 2 on modules    '''

'''    ex-1     '''
# import Math
# print(Math)

'''    ex-2     '''
# from Math import (
#     simple as si, 
#     complex as cc
# )

# print(si.add(5, 33))
# print(si.mul(53, 5))
# print(cc.square(5))
# print(cc.cube(4))


'''     ex-3    '''
# from Math.simple import *
# from Math.complex import *

# print(add(5, 2))
# print(div(45, 4))
# print(square(5))
# print(cube(6))


'''     ex-4    '''

# after adding __all__ = ['simple', 'complex'] to __init__.py file
from Math import *
print(simple.add(5, 23))
print(complex.square(5))

