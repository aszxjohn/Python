#! python3
import random
import enum


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

class CheckType(enum.IntEnum):  
    BEGIN = 0,              # 特殊值 保留給特殊用途

    NO_ZERO_HEAD = 1,       # 開頭不為0
    NUMBER_ONLY = 2,        # 必須是數字
    FOUR_DIGITS = 3,        # 4位數
    NO_REPEAT = 4,          # 不能重複
    
    PASS = 255              # 特殊值 保留給特殊用途

def guess_number_check(guess_number):
    '''此函式負責檢查輸入字串是否合法，若不合法則傳回失敗的檢查項目'''
    
    # 先定義好不同檢查
    def check_no_zero_head(number):
        return number[0] != '0'         # 開頭不為零為True

    def check_number_only(number):
        return number.isnumeric()

    def check_four_digits(number):
        return len(number) == 4

    def check_no_repeat(number):
        for i in range(len(number)):
            if number[i] in number[i+1:]:
                # 一檢查出重複就跳出函式傳回False
                return False
        # 都沒有重複的話才會離開迴圈執行到這
        return True

    # 依序檢查各個項目，如果有錯誤就回傳 (NOTE: 如果有多個錯誤，則只會回傳最早檢查到的那個)
    if not check_no_zero_head(guess_number):
        return CheckType.NO_ZERO_HEAD

    elif not check_number_only(guess_number):
        return CheckType.NUMBER_ONLY

    elif not check_four_digits(guess_number):
        return CheckType.FOUR_DIGITS

    elif not check_no_repeat(guess_number):
        return CheckType.NO_REPEAT

    return CheckType.PASS

def get_legal_input():
    '''直接向玩家取得一個合法的輸入並回傳'''

    # 將所有可能的訊息整理起來，可以方便管理
    INPUT_MESSAGE = [
        '請輸入四位不已0開頭，也不重複的數字(0-9)',
        '請重新輸入~~開頭不能為0!!\n請輸入四位不已0開頭，也不重複的數字(0-9)',
        '請重新輸入~~請使用數字輸入!!\n請輸入四位不已0開頭，也不重複的數字(0-9)',
        '請重新輸入~~請輸入四位數喔!!\n請輸入四位不已0開頭，也不重複的數字(0-9)',
        '請重新輸入~~請不要輸入重複的數字喔!!\n請輸入四位不已0開頭，也不重複的數字(0-9)'
    ]

    check_result = CheckType.BEGIN   # 設定為起始狀態
    input_number = ''  # 初始化變數

    # 重複要求玩家輸入直到玩家輸入合法的數字
    while check_result != CheckType.PASS:
        input_number = str(input(INPUT_MESSAGE[int(check_result)]))
        check_result = guess_number_check(input_number)

    return input_number


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
                random_number = str(random.randint(0, 9))
        
            result_number = str(result_number) + str(random_number)

    return result_number

def main():
    anwser = generator()
    print('The anwser ：　'+ str(anwser))

    #guess_number = guess_number_check(str(input('請輸入四位不已0開頭，也不重複的數字(0-9)')))
    
    #judgement_victory_conditions = judgement(guess_number, anwser)  # 第一次輸入的數字也要檢查才對

    judgement_victory_conditions = '' # 初始化參數
    while (judgement_victory_conditions != 'win'):
        #guess_number = str(input('猜錯瞜~~ 請在猜一次 <3 (0-9)'))
        #guess_number = guess_number_check(guess_number)
        guess_number = get_legal_input()    # 取得合法的輸入
        judgement_victory_conditions = judgement(guess_number, anwser)  # 判斷結果

    print('you win')

if __name__ == '__main__':
    main()