#! python3
""
import pandas as pd
import numpy as np



class Skill:
    skill_table = []

    def __init__(self):
        # initialization
        self.name = ''
        self.mp_cost = 0
        self.DamageModifier = 0
        self.Commentary = ''


    def load_from_file(self):
        Skill.skill_table = pd.read_excel("C:\Workspace\Python\RPG\Value setting.xlsx", sheet_name = 'skill_list') #  "data" are all sheets as a dictionary


    def skill_table_show(self):
        print(Skill.skill_table)

        print('------------------------')

        print(Skill.skill_table.loc[Skill.skill_table['ID'] == 'Normal_Attack', 'Name'])   #搜尋ID欄位內是揮砍的資料並顯示她的Name

        print('------------------------')

        print(Skill.skill_table.loc[Skill.skill_table['ID'] == 'Normal_Attack', ['ID', 'Name','Type', 'mp_cost', 'DamageModifier', 'Commentary']]) #搜尋ID欄位內是揮砍的資料並顯示她的所有資料

        print('------------------------')

    def skill_normal_attack(self):

        normal_attack = []
        normal_attack = Skill.skill_table.loc[Skill.skill_table['ID'] == 'Normal_Attack', ['ID', 'Name','Type', 'mp_cost', 'DamageModifier', 'Commentary']]  #搜尋ID欄位內是''Normal_Attack''的資料並傳給'normal_attack'
        

        name = str(normal_attack.loc[0, 'Name']) 
        mp_cost = int(normal_attack.loc[0, 'mp_cost'])
        DamageModifier = int(normal_attack.loc[0, 'DamageModifier'])
        Commentary = str(normal_attack.loc[0, 'Commentary'])

        #print('name = {}, mp_cost = {}, DamageModifier = {}, Commentary = {}'.format(name, mp_cost, DamageModifier, Commentary))


    def skill_Slash(self):

        Slash = []
        Slash = Skill.skill_table.loc[Skill.skill_table['ID'] == 'Slash', ['ID', 'Name','Type', 'mp_cost', 'DamageModifier', 'Commentary']]  #搜尋ID欄位內是''Slash''的資料並傳給'skill_Slash'
 

        name = str(Slash.loc[1, 'Name']) 
        mp_cost = int(Slash.loc[1, 'mp_cost'])
        DamageModifier = int(Slash.loc[1, 'DamageModifier'])
        Commentary = str(Slash.loc[1, 'Commentary'])

        #print('name = {}, mp_cost = {}, DamageModifier = {}, Commentary = {}'.format(name, mp_cost, DamageModifier, Commentary))
        

    def skill_jump_hit(self):

            jump_hit = []
            jump_hit = Skill.skill_table.loc[Skill.skill_table['ID'] == 'jump_hit', ['ID', 'Name','Type', 'mp_cost', 'DamageModifier', 'Commentary']]  #搜尋ID欄位內是''jump_hit''的資料並傳給'skill_jump_hit'
    

            name = str(jump_hit.loc[2, 'Name']) 
            mp_cost = int(jump_hit.loc[2, 'mp_cost'])
            DamageModifier = int(jump_hit.loc[2, 'DamageModifier'])
            Commentary = str(jump_hit.loc[2, 'Commentary'])

            print('name = {}, mp_cost = {}, DamageModifier = {}, Commentary = {}'.format(name, mp_cost, DamageModifier, Commentary))
            






def main():
    skill_test = Skill()
    skill_test.load_from_file()
    #skill_test.skill_table_show()
    #skill_test.skill_normal_attack()
    #skill_test.skill_Slash()
    #skill_test.skill_jump_hit()

if __name__ == "__main__":
    main()