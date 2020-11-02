#! python3
#玩家職業

class creature():

    def __init__(self, name):
        self.name = name    
        self.LV = 1
        self.HP = 0
        self.MP = 0
        self.STR = 0
        self.INT = 0
        self.MATK = 0
        self.DEF = 0
        self.SPD = 0
        self.EXPTotalValue = 1 * self.LV
        self.EXPOwnValue = 0


    def new_creature(self):
        self.LV = 1
        self.self.EXPTotalValue = 1 * self.LV

        pass
    
    def creature_upgrade(self):
        if self.LV < 6 :
            self.LV = self.LV + 0
            self.HP = self.HP + 0
            self.MP = self.MP + 0
            self.STR = self.STR + 0
            self.INT = self.INT + 0
            self.DEF = self.DEF + 0
            self.MATK = self.MATK + 0
            self.SPD = self.SPD +0
        
        elif self.LV >= 6:
            print("等級已經最大")
    

    def LeveUP(self, GetEXP):

        leve_up = 'No'

        self.EXPOwnValue = self.EXPOwnValue + GetEXP

        if self.EXPOwnValue >= self.EXPTotalValue:

            self.EXPOwnValue = self.EXPOwnValue - self.EXPTotalValue
            leve_up = 'yes'


        return self.EXPOwnValue,  leve_up


    

    def show_status(self):
       print("name = {}, LV = {},  HP = {}, MP = {}, STR = {}, INT = {}, DEF = {}, MATK = {}, SPD = {}\n".format(self.name,self.LV, self.HP, self.MP, self.STR, self.INT, self.DEF, self.MATK, self.SPD))
        

def main():
    pass


if __name__ == "__main__":
    main()
