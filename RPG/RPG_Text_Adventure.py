#! python3

#遊戲本體測試

import pandas as pd
import numpy as np

from skill import Skill
from creature import creature 
from Monster import monster_skeleton_shield_soldier
from Player_Profession import swordsman




def game_start():
    play_name = input('初來乍到的旅人阿,請告訴我妳的名字 \n')

    Career_choice_stage = 'Career choice stage'

    while Career_choice_stage == 'Career choice stage':
        
        Player_Profession = input('請選擇職業   swordsman, Wizard, Cleric, Thief \n')
        Player_Profession = Player_Profession.lower()

        if Player_Profession == 'swordsman':
            player = swordsman(play_name)
            player.new_creature()

            Career_choice_stage = 'End of career choice'

        elif Player_Profession == 'wizard':
            print('抱歉沒有這個職業還未實裝請重新選擇')

        elif Player_Profession == 'cleric':
            print('抱歉沒有這個職業還未實裝請重新選擇')

        elif Player_Profession == 'thief':
            print('抱歉沒有這個職業還未實裝請重新選擇')
        
        else:
            print('抱歉沒有這個職業請重新輸入')


    print('腳色建立完成，以下是您的腳色：')
    player.show_status()

    return player



def Monster_summon_Function(player_LV):
    Monster_summon = monster_skeleton_shield_soldier('骷髏劍盾兵')
    Monster_summon.new_creature()

    if Monster_summon.LV < player_LV:
        for i in player_LV:
            Monster_summon.creature_upgrade

    print('你現在碰到一個 \'{}\' 請問你要做甚麼呢?'.format(Monster_summon.name))

    return Monster_summon
                

def fighting_Function(player,Monster_summon):

    fighting = 'In_battle'

    while fighting == 'In_battle':
        
        if Monster_summon.HP > 0 or player.HP < 0 :
            
            Monster_summon.show_status()

            player.show_status()

            play_action = input('1.fighting  2.Run away\n')

            if play_action == 'fighting':

                
                play_action = input('要使用哪個技能呢?   1.{}  2.{}  3.{}\n'.format(player.skill_list[0], player.skill_list[1], player.skill_list[2]))
                




                
            elif play_action == 'Run away':
                print('這功能現在還沒有，而且四周都是魔物請繼續戰鬥')
        
        elif Monster_summon.HP <= 0 or player.HP <= 0 :

            if Monster_summon.HP <= 0 :
                fighting = 'End of the battle'

                print('戰鬥結束--玩家獲勝')


            elif player.HP <= 0:
                fighting = 'End of the battle'

                print('戰鬥結束--玩家輸了')

            else:
                print('不該出現')






def main():

    gamemod = '' # start, end, read_archive

    print('RPG遊戲測\n')

    gamemod = input('start -- 開始遊戲,\nend -- 離開遊戲,\nread_archive -- 讀取進度\n')

    read_archive = ''  #暫時,之後寫存取後就要改掉

    while gamemod == 'start' or gamemod == 'read_archive':
        if read_archive == '':
            player = game_start()
        

        print('騷年!你準備好進入冒險的世界了嗎?\n很好那你就開始無止盡的戰鬥吧!!!\n')
        print('------------------------------------------------------------\n')
        print('----------------------------------------------\n')
        print('-----------------------------\n')
        print('------------------\n')




        while player.LV < 6:
            
            
            Monster_summon = Monster_summon_Function(player.LV)  # 招換一個與玩家同級的怪物


            fighting_Function(player,Monster_summon)

            print('雖然你贏了，但因為附近都是怪物所以請你繼續戰鬥')

            

        
        gamemod = 'end'





if __name__ == "__main__":
    main()
