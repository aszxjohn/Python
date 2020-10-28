#! python 3

def str_to_class(classname):
    return getattr(sys.modules[__name__], classname)


class test_30():

    def __init__(self):   
        print('class over:test_30')

    
    def print_yo(self):
        print("yo_2")
