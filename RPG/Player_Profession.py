#! python3
#玩家職業與生物
from creature import creature

class swordsman(creature):

    
    def __init__(self, name):   
        super(swordsman, self).__init__(name)

    def new_creature(self):
        self.LV = 1
        self.HP = 70
        self.MP = 50
        self.STR = 8
        self.INT = 2
        self.DEF = 3
        self.MATK = 2
        self.SPD = 5
        self.skill_list = ['normal attack', 'Slash', 'jump hit']

    def creature_upgrade(self):
        if self.LV < 6 :
            self.LV = self.LV + 1
            self.HP = self.HP + 20
            self.MP = self.MP + 5
            self.STR = self.STR + 4
            self.INT = self.INT + 1
            self.DEF = self.DEF + 3
            self.MATK = self.MATK + 2
            self.SPD = self.SPD +2
        elif self.LV >= 6:
            print("等級已經最大")




def main():
    play_1 = swordsman('play_1')
    play_1.new_creature()

    for i in range(0, 9, 1):
        play_1.creature_upgrade()
        play_1.show_status()

if __name__ == "__main__":
    main()
