#! python3
#怪物

from creature import creature

class Monster_Skeleton_Shield_Soldier(creature):
    
    def __init__(self, name):   
        super(Monster_Skeleton_Shield_Soldier, self).__init__(name = '骷髏劍盾兵')

    def New_creature(self):

        self.LV = 1
        self.HP = 12
        self.STR = 15
        self.DEF = 7
        self.MATK = 7
        self.SPD = 2
    
    def creature_upgrade(self):
        if self.LV < 6 :
            self.LV = self.LV + 1
            self.HP = self.HP + 18
            self.STR = self.STR + 7
            self.DEF = self.DEF + 6
            self.MATK = self.MATK + 6
            self.SPD = self.SPD + 3
        elif self.LV >= 6:
            print("等級已經最大")




def main():
    Monster_test = Monster_Skeleton_Shield_Soldier('Monster_test')
    Monster_test.New_creature()
    for i in range(9):
        Monster_test.creature_upgrade()
        Monster_test.show_status()

if __name__ == "__main__":
    main()
