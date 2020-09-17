class biological():
    
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP
    

class Swordsman(biological):
   
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP

    def status_print():
       print(self.name, self.HP)

def main():
    Play1 = Swordsman(1, 80)

    Play1.status_print()

if __name__ == "__main__":
    main()
