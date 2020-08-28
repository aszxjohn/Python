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
def guess_number_check(guess_number):

    while len(guess_number) != 4 or guess_number[0] == '0' or guess_number == 'Number repeat' or guess_number.isnumeric() == False:
        if guess_number[0] == '0':
            guess_number = str(input("請重新輸入~~開頭不能為0!! \n" + "1.第一個數字不能為零! \n" + "2.請不要輸入重複的數字 \n" + "3.請輸入四位數(0-9)："))
        elif guess_number.isnumeric() == False:
            guess_number = str(input("請重新輸入~~請使用數字輸入!! \n" + "1.第一個數字不能為零! \n" + "2.請不要輸入重複的數字 \n" + "3.請輸入四位數(0-9)："))
        else:
            guess_number = str(input("請重新輸入~~請輸入四位數喔!! \n" + "1.第一個數字不能為零! \n" + "2.請不要輸入重複的數字 \n" + "3.請輸入四位數(0-9)："))
        
        for i in range(len(guess_number) - 1):
            if guess_number[i] == guess_number[i+1]:
                guess_number = str(input("請重新輸入~~請不要輸入重複的數字喔!! \n" + "1.第一個數字不能為零! \n" + "2.請不要輸入重複的數字 \n" + "3.請輸入四位數(0-9)："))
                guess_number = 'Number repeat'

    return guess_number
       

def judgement(guess_number, anwser):
    A = 0
    B = 0
    
    for x in range(0, 4):
        if guess_number[x] == anwser[x]:
            A = A + 1
        elif guess_number[x] in anwser:
            B = B + 1

    if A == 4:
        return 'win'
    else:
        print(str(A) + 'A '+ str(B) + 'B')
    

def generator():
    result_number = '0'
    random_number = ''

    while(result_number[0] == '0'):
        result_number = ''
        for i in range(0, 4):
            random_number = str(random.randint(0, 9))

            while(random_number in result_number):
                random_number = str(random.randint(1, 9))
        
            result_number = str(result_number) + str(random_number)

    return result_number

def main():
    anwser = generator()
    print('The anwser ：　'+ str(anwser))

    guess_number = guess_number_check(str(input('請輸入四位不已0開頭，也不重複的數字(0-9)')))
    judgement_victory_conditions = ''

    while (judgement_victory_conditions != 'win'):
        guess_number = str(input('猜錯瞜~~ 請在猜一次 <3 (0-9)'))
        guess_number = guess_number_check(guess_number)

        judgement_victory_conditions = judgement(guess_number, anwser)

    print('you win')

if __name__ == '__main__':
    main()