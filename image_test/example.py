

class Human():

    # 靜態變數 (類似全域變數，所有物件共通的值)
    number = 0          # 世界上有多少人    
    people_list = []    # 人口名單

    def __init__(self, name, age=0):
        # 成員變數 (每一個物件可以有不同值)
        self.name = name
        self.age = age
        self.weight = 10        # 剛出生的體重

    def eat(self):
        # 吃東西變胖
        self.weight += 1        

    def print_status(self):
        # (成員函式) 印出這個人的狀態
        print("name = {}, age = {}, weight = {}".format(self.name, self.age, self.weight))

    def print_all_status():
        print(human_object.name)

        # (靜態函式) 印出所有人類的狀態
        for people in Human.people_list:
            people.baby_born("name")

    def baby_born(name):
        # (靜態函式) 誕生一個人
        new_baby = Human(name)
        Human.number += 1                       # 人口+1
        Human.people_list.append(new_baby)      # 加入人口列表

def main():

    human = Human()
    Human.print_all_status(100)

    Human.baby_born("Jerry")
    Human.print_all_status()

    print("=================================")
    
    Human.baby_born("Jimmy")
    Human.print_all_status()


if __name__ == "__main__":
    main()