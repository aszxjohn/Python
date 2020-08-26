''''--------------------------hellow World----------------------------'''

print('Hello world')

'''------------------------------字串組合------------------------------'''

FistName = 'aszx'
SecondName = 'john'

print(FistName+SecondName)

'''--------------------------字串複製組合-------------------------------'''

print('廣播測試~~'*5)

'''---------------------------自行輸入字串------------------------------'''
MyName = input('請輸入你的名字'+'\n')

if MyName == 'Null' or MyName == " ":
    print('錯誤')
else:
    print(MyName)

'''------------------------------流程控制------------------------------'''

Dick = input('你的手臂多長呢?\n')
Dick = int(Dick)

if Dick <= 5:
    print('這是開玩笑?')
elif Dick > 5 and Dick <= 10:
    print('是嬰兒嗎??')
elif Dick > 10 and Dick <= 15:
    print('你是小學生對不對')
elif Dick > 15 and Dick <= 20:
    print('你的手偏短喔')
elif Dick > 20:
    print('你有正常的手臂呢')

'''------------------------------迴圈練習------------------------------'''
Password = '0'
print('User：Administrator')

while Password != 'P@ssw0rd':
    Password = input('請輸入你的密碼：')


print('登入成功')


'''------------------------------For迴圈匯入模組練習------------------------------'''

import random

print('大樂透號碼')

for i in range(6):
    print(random.randint(1,49))