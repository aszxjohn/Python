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
        skill_table = pd.read_excel("C:\Workspace\Python\RPG\Value setting.xlsx", sheet_name = 'skill_list') #  "data" are all sheets as a dictionary
        mp_cost = pd.DataFrame(skill_table, columns = ['mp_cost'])
        print(skill_table)
        print(mp_cost)


    def skill_table_show(self):
        print(skill_table)



skill_test = Skill()
skill_test.load_from_file()
