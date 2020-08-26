#Collatz序列：這是一個不管你輸入怎麼樣的數字都能變成一的算式，
#如果數字是偶數則直接除以2，若是奇數則乘3+1

def collatz(Number):
    if Number ==1:      #先判段這數字是否是1，是的話跳返回數字結束迴圈
        return Number
    else:               #判斷Number是偶數奇數，在討入不同的算式，使他遞迴
        if Number % 2 == 0:
            print(Number)
            return collatz(Number // 2)
        else:
            print(Number)
            return collatz(Number*3 + 1)



PlayerNumber = input('請輸入一個數字： ')
PlayerNumber = int(PlayerNumber)
#請玩家輸入一個數字，並將他轉成INT格式

PlayerNumber=collatz(PlayerNumber)
#玩家輸入的數字放入函數


print(PlayerNumber)
#將回傳的數字列印出來
