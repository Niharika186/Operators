'''Arithmetic Operators'''
# a,b=(int(x) for x in input('values of a and b: ').split())
# print(a+b) # Addition  # 5
# print(a-b) # Subtraction # -1
# print(a*b) # Multiplication # 6
# print(a/b) # Division # 0.6
# print(a%b) # Module # 2
# print(a**b) # Exponent or Power # 8

'''Floor Division'''
# a=6//4
# print(a) # 1
# b=6/4 
# print(b) # 1.5
# c=6//4.0
# print(c) # 1.0
# d=6.0/4
# print(d) # 1.5
# e=6.0//4
# print(e) # 1.0

'''Assignment Operators'''
# a=4
# a+=a
# print(a) # a=a+a a=4+4=8
# a-=a
# print(a) # a=a-a a=4-4=0
# a*=a
# print(a) # a=a*a a=4*4=16
# a/=a
# print(a) # a=a/a a=4/4=1.0
# a%=a
# print(a) # a=a%a a=4%4=0
# a**=a

# print(a) # a=a**a a=4**4=256
# a=int(input())  # 2
# print(a) # 2
# print(f'the value of a is {a}')  # the value of a is 2
# a+=2
# print('the value of a after a+=a is {}'.format(a)) # 4
# a-=3    
# print('the value of a after a-=a is {}'.format(a)) # -1
# a*=4
# print('the value of a after a*=a is {}'.format(a)) # 8
# a/=a
# print('the value of a after a/=a is {}',format(a)) # 1.0


'''Relational Operators'''
# a=int(input('the value of a: ')) # 2
# b=int(input('the value of b: ')) # 3
# print(f'the value of {a} < {b} is {a<b}') # True
# print(f'the value of {a} > {b} is {a>b}') # False
# print(f'the value of {a} <= {b} is {a<=b}') # True
# print(f'the value of {a} => {b} is {a>=b}') # False
# print(f'the value of {a} == {b} is {a==b}') # False
# print(f'the value of {a} != {b} is {a!=b}') # True

'''Logical Operators-specify with words'''
# a=int(input('the value of a: ')) # 2
# b=int(input('the value of b: ')) # 3
# print('the value of a<b and a>b is {}'.format(a<b and a>b)) # False
# print('the value of a>b and a<b is {}'.format(a>b and a<b)) # False
# print('the value of a!=b and a==b is {}'.format(a!=b and a==b)) # False
# print('the value of a<b or a>b is {}'.format(a<b or a>b)) # True
# print('the value of a>b or a<b is {}'.format(a>b or a<b)) # True
# print('the value of a!=b or a==b is {}'.format(a!=b or a==b)) # True
# print('opposite of {}=={} is {}'.format(a,b,not a==b)) # True
# print('opposite of {}!={} is {}'.format(a,b,not a!=b)) # False


'''Bitwise Operators-specify with symbols'''
# a=int(input('the value of a: ')) # 2
# b=int(input('the value of b: ')) # 3
# print('the value of {} & {} is {}'.format(a,b,a&b)) # 2
# print('the value of {} | {} is {}'.format(a,b,a|b)) # 3

"""Note: The formula for Negation (~) is -(value+1)    """
# print("The value of ~{} is {}".format(a,~a)) # -3
# print("The value of ~{} is {}".format(b,~b)) # -4


'''Identity Operator'''
# a = 20
# b = 20
# print(id(a)) # 1586463376208
# print(id(b)) # 1586463376208

# if ( a is b ):
#    print ("a and b have same identity") # a and b have same identity
# else:
#    print ("a and b do not have same identity")

# if ( id(a) == id(b) ):
#    print ("a and b have same identity") # a and b have same identity
# else:
#    print ("a and b do not have same identity")

# a=4
# print(type(a) is int) # True
# print(type(a) is not float) # True
# print(type(a) is str) # False
# b=5.6
# print(type(b) is int) # False
# print(type(b) is float) # True
# print(type(b) is str) # False
# c='hello'
# print(type(c) is int) # False
# print(type(c) is not float) # True
# print(type(c) is str) # True


'''Membership Operator'''
# a={'2','4','6','8','10','12','14','16','18'}
# print('1' not in a) # True
# print('2' in a) # True
# print('3' not in a) # True
# print('4' in a) # True
# print('5' in a) # False
# print('6' in a) # True

'''Shift Operator (>>Right /2  and << Left *2)'''
# a=30
# print(a>>1) # 15
# print(a>>2) # 7
# print(a>>3) # 3
# print(a>>4) # 1
# b=2
# print(b<<1) # 4
# print(b<<2) # 8
# print(b<<3) # 16


