'''---------------------------函數----------------------------------'''

def hellow(name):
    print('應徵者： ' + name)


hellow('Jating Hong')


'''---------------------------返還函數----------------------------------'''
import random

def ThanSize(PlayerNumber):

    RandomNumber = random.randint(1,100)
    if PlayerNumber == RandomNumber:
        return '平手'
    elif PlayerNumber > RandomNumber:
        return '玩家勝利'
    else:
        return '電腦勝利'


PlayerNumber = input('請輸入數字(1-100)： ')
PlayerNumber = int(PlayerNumber)

printinfo =  ThanSize(PlayerNumber)
print(printinfo)

'''---------------------------返還函數----------------------------------'''