#! python3
import random


"""
電腦會以亂數產生一個不重複的四位數字讓你來猜。

你輸入數字之後，電腦會比對數字，並輸出結果。

結果的格式是 『？A？B』，A代表位置及數值都相同，B表示只有數值相同但位置不同。

例如答案是1234，而你猜1789，結果就是1A0B。
因為只有1位置及數值都對了，789這三個數都沒猜對。

如果猜2189，結果就是0A2B，2和1數值都對，但位置錯誤。

根據每次猜的結果，就可以慢慢推算出答案。

除了運氣之外，實力也很重要哦！

本遊戲沒有次數上限讓你猜到贏， 加油！！

"""
def GuessTheNumber_function(GuessTheNumberFunction_Number):

    while (len(GuessTheNumberFunction_Number) != 4 or GuessTheNumberFunction_Number[0] == '0' or GuessTheNumberFunction_Number == 'Number repeat' or GuessTheNumberFunction_Number.isnumeric() == False  ):
        if GuessTheNumberFunction_Number[0] == '0':
            GuessTheNumberFunction_Number = str(input("請重新輸入~~開頭不能為0!! \n"+"1.第一個數字不能為零! \n"+"2.請不要輸入重複的數字 \n"+"3.請輸入四位數(0-9)："))
        elif GuessTheNumberFunction_Number.isnumeric() == False:
            GuessTheNumberFunction_Number = str(input("請重新輸入~~請使用數字輸入!! \n"+"1.第一個數字不能為零! \n"+"2.請不要輸入重複的數字 \n"+"3.請輸入四位數(0-9)："))
        else:
            GuessTheNumberFunction_Number = str(input("請重新輸入~~請輸入四位數喔!! \n"+"1.第一個數字不能為零! \n"+"2.請不要輸入重複的數字 \n"+"3.請輸入四位數(0-9)："))
        
        for z in range(len(GuessTheNumberFunction_Number)-1):
            if GuessTheNumberFunction_Number[z] == GuessTheNumberFunction_Number[z+1]:
                GuessTheNumberFunction_Number = str(input("請重新輸入~~請不要輸入重複的數字喔!! \n"+"1.第一個數字不能為零! \n"+"2.請不要輸入重複的數字 \n"+"3.請輸入四位數(0-9)："))
                GuessTheNumberFunction_Number = 'Number repeat'
    if  GuessTheNumberFunction_Number.isnumeric():
        GuessTheNumberFunction_Number = str(input("請重新輸入~~請使用數字輸入!! \n"+"1.第一個數字不能為零! \n"+"2.請不要輸入重複的數字 \n"+"3.請輸入四位數(0-9)："))

    return GuessTheNumberFunction_Number

       

def Judgment(GuessTheNumber_Judgment,TitleNumber_Judgment):
    A = 0
    B = 0
    
    for x in range(0,4):
        if GuessTheNumber_Judgment[x] == TitleNumber_Judgment[x]:
            A = A+1
        elif GuessTheNumber_Judgment[x] in TitleNumber_Judgment:
            B = B+1


    if A == 4:
        return 'win'
    else:
        print(str(A) + 'A '+str(B) + 'B')
    

def Generator():
    
    TitleNumber = '0'
    randomNumber = ''

    while(TitleNumber[0] == '0'):
        TitleNumber = ''
        for i in range(0,4):
            randomNumber = str(random.randint(0,9))

            while(randomNumber in TitleNumber):
                randomNumber = str(random.randint(1,9))
        
            TitleNumber = str(TitleNumber) + str(randomNumber)


    return TitleNumber






TitleNumber = Generator()
print('TitleNumber ：　'+ str(TitleNumber))

GuessTheNumber = GuessTheNumber_function(str(input('請輸入四位不已0開頭，也不重複的數字(0-9)')))
Judgment_VictoryConditions = ''

while (Judgment_VictoryConditions != 'win'):

    
    GuessTheNumber = str(input('猜錯瞜~~ 請在猜一次 <3 (0-9)'))
    GuessTheNumber = GuessTheNumber_function(GuessTheNumber)


    Judgment_VictoryConditions = Judgment(GuessTheNumber,TitleNumber)




print('you win')