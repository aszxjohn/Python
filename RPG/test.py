import sys

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)

class test():
    
    def __init__(self):   
        print('class over')


    def print_yo(self):
        print("yo")


b = test

c = 'test'


print(type(b))

c = str_to_class(c)

test={'a': b, 'c' : c}



#test['a']()
d = test['c']()

d.print_yo()
