#! python3
""
import pandas as pd
import numpy as np



class skill:


    skill_table = []
    skill_table = pd.read_excel("C:\Workspace\Python\RPG\Value setting.xlsx", sheet_name = 'skill_list') #  "data" are all sheets as a dictionary




    def __init__(self):
        # initializationSS

    
        self.name = ''
        self.mp_cost = 0
        self.DamageModifier = 0
        self.Commentary = ''
        self.skill_use_table = {}  #使用技能時用來觸發技能的字典陣列

        




    def load_from_file(self):
        Skill.skill_table = pd.read_excel("C:\Workspace\Python\RPG\Value setting.xlsx", sheet_name = 'skill_list') #  "data" are all sheets as a dictionary



        

class normal_attack(skill):
    
    def __init__(self):   
        super(normal_attack, self).__init__()

        normal_attack_list = []
        normal_attack_list = skill.skill_table.loc[skill.skill_table['ID'] == 'Normal_Attack', ['ID', 'Name','Type', 'mp_cost', 'DamageModifier', 'Commentary']]  #搜尋ID欄位內是''Normal_Attack''的資料並傳給'normal_attack'
    
        self.name = str(normal_attack_list.loc[0, 'Name']) 
        self.mp_cost = int(normal_attack_list.loc[0, 'mp_cost'])
        self.DamageModifier = int(normal_attack_list.loc[0, 'DamageModifier'])
        self.Commentary = str(normal_attack_list.loc[0, 'Commentary'])

    def skill_show_status(self):

        print('name = {} mp_cost = {} DamageModifier = {} Commentary = {}'.format(self.name, self.mp_cost, self.DamageModifier, self.Commentary))


    def skill_use(self, player_STR):
        
        Attack_power = player_STR * self.DamageModifier

        return Attack_power




class slash(skill):
    
    def __init__(self):   
        super(slash, self).__init__()

        slash_list = []
        slash_list = skill.skill_table.loc[skill.skill_table['ID'] == 'slash', ['ID', 'Name','Type', 'mp_cost', 'DamageModifier', 'Commentary']]  #搜尋ID欄位內是''Slash''的資料並傳給'skill_Slash'
    
        self.name = str(slash_list.loc[1, 'Name']) 
        self.mp_cost = int(slash_list.loc[1, 'mp_cost'])
        self.DamageModifier = int(slash_list.loc[1, 'DamageModifier'])
        self.Commentary = str(slash_list.loc[1, 'Commentary'])

    def skill_show_status(self):

        print('name = {} mp_cost = {} DamageModifier = {} Commentary = {}'.format(self.name, self.mp_cost, self.DamageModifier, self.Commentary))


    def skill_use(self, player_STR):
        
        Attack_power = player_STR * self.DamageModifier

        return Attack_power





class jump_hit(skill):
    
    def __init__(self):   
        super(jump_hit, self).__init__()

        jump_hit_list = []
        jump_hit_list = skill.skill_table.loc[skill.skill_table['ID'] == 'jump_hit', ['ID', 'Name','Type', 'mp_cost', 'DamageModifier', 'Commentary']]  #搜尋ID欄位內是''jump_hit''的資料並傳給'skill_Slash'
    
        self.name = str(jump_hit_list.loc[2, 'Name']) 
        self.mp_cost = int(jump_hit_list.loc[2, 'mp_cost'])
        self.DamageModifier = int(jump_hit_list.loc[2, 'DamageModifier'])
        self.Commentary = str(jump_hit_list.loc[2, 'Commentary'])

    def skill_show_status(self):

        print('name = {} mp_cost = {} DamageModifier = {} Commentary = {}'.format(self.name, self.mp_cost, self.DamageModifier, self.Commentary))


    def skill_use(self, player_STR):
        
        Attack_power = player_STR * self.DamageModifier

        return Attack_power



class skill_action():


 
    skill_table = {
        'normal_attack' : normal_attack,
        'slash' : slash,
        'jump_hit' : jump_hit,
    }


    def skill_to_use(self, monster_HP, monster_DEF, player_attack_power):
        monster_HP = monster_HP - (player_attack_power - monster_DEF)

        return monster_HP





def main():


    slash_skill_test = skill()
    slash_skill_test.Initialize()
    slash_skill_test.Initialize[slash]()

if __name__ == "__main__":
    main()