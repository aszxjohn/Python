import sys

from test_2 import test_30

from test_2 import str_to_class


class test():
    
    def __init__(self):   
        print('class over')


    def print_yo(self):
        print("yo")






a = test_30.print_yo

b = str_to_class(a)

b.print_yo

