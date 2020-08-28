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

    # 將功能模組化可以讓程式碼更好維護，檢查重複的部分邏輯較複雜，因此獨立出一個函式
    def check_no_repeat(number):     # 這邊也可以不用傳入參數，直接使用上層的guess_number
        for i in range(len(number)):
            # 對每個數字都去檢查後面的數字是否有相同的字元存在
            if number[i] in number[i+1:]:       # NOTE: 陣列中的冒號使用方式可以注意一下 (Python才有這類用法)
                # 一旦發現有相同，就可以直接傳回錯誤，不需要將迴圈跑完
                return False
        # 沒有檢查到相同時，程式碼才有可能進入這裡
        return True


    # 原while迴圈的檢查項目缺少了相同數字的檢查，另外 guess_number == 'Number repeat' 這段顯然是錯誤的用法
    # # while len(guess_number) != 4 or guess_number[0] == '0' or guess_number == 'Number repeat' or guess_number.isnumeric() == False:
    while len(guess_number) != 4 or guess_number[0] == '0' or guess_number == 'Number repeat' or guess_number.isnumeric() == False or check_no_repeat(guess_number) == False:
        if guess_number[0] == '0':
            guess_number = str(input("請重新輸入~~開頭不能為0!! \n" + "1.第一個數字不能為零! \n" + "2.請不要輸入重複的數字 \n" + "3.請輸入四位數(0-9)："))
        elif guess_number.isnumeric() == False:
            guess_number = str(input("請重新輸入~~請使用數字輸入!! \n" + "1.第一個數字不能為零! \n" + "2.請不要輸入重複的數字 \n" + "3.請輸入四位數(0-9)："))
        elif len(guess_number) != 4:  # 延續while的檢查項目
            guess_number = str(input("請重新輸入~~請輸入四位數喔!! \n" + "1.第一個數字不能為零! \n" + "2.請不要輸入重複的數字 \n" + "3.請輸入四位數(0-9)："))
        elif check_no_repeat(guess_number) == False: # 延續while的檢查項目
            guess_number = str(input("請重新輸入~~請不要輸入重複的數字喔!! \n" + "1.第一個數字不能為零! \n" + "2.請不要輸入重複的數字 \n" + "3.請輸入四位數(0-9)："))
        else:
            # 有時候，可以加一些這類程式碼來確保程式運行是正確的，顯然邏輯正確的情況下是不可能進入這裡的
            raise Exception("這不會發生")
        
        # 這段只會檢查到連續兩個數字相同，而且檢查到錯誤的時候，也不會要求使用者重新輸入
        # # for i in range(len(guess_number) - 1):
        # #     if guess_number[i] == guess_number[i+1]:
        # #         guess_number = str(input("請重新輸入~~請不要輸入重複的數字喔!! \n" + "1.第一個數字不能為零! \n" + "2.請不要輸入重複的數字 \n" + "3.請輸入四位數(0-9)："))
        # #         guess_number = 'Number repeat'

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
                # # random_number = str(random.randint(1, 9))  # 這裡應該是0~9?
                random_number = str(random.randint(0, 9))
        
            result_number = str(result_number) + str(random_number)

    return result_number

def main():
    anwser = generator()
    print('The anwser ：　'+ str(anwser))

    guess_number = guess_number_check(str(input('請輸入四位不已0開頭，也不重複的數字(0-9)')))
    
    # judgement_victory_conditions = ''  # 第一次完全沒有給玩家機會，沒跑judgement就直接宣告他錯
    judgement_victory_conditions = judgement(guess_number, anwser)  # 第一次輸入的數字也要檢查才對

    while (judgement_victory_conditions != 'win'):
        guess_number = str(input('猜錯瞜~~ 請在猜一次 <3 (0-9)'))
        guess_number = guess_number_check(guess_number)

        judgement_victory_conditions = judgement(guess_number, anwser)

    print('you win')

if __name__ == '__main__':
    main()