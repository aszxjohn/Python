

####################################################################################################################################

class SkillBase:
    skill_table = []

    def Initialize():
        skill_table = {
            "Whirl Wind":WhirlWind,
            "Firebolt":Firebolt,
            "Lightning Storm":LightningStorm
        }
    
    def __init__(self, name, mana_cost, damage_multiplier):
        # initialization (static data)
        self.name = name
        self.mp_cost = mana_cost
        self.damage_modifier = damage_multiplier

    def use_skill(self, caster, targets):
        # Implement skill here
        pass
    
####################################################################################################################################

class WhirlWind(SkillBase):
    def __init__(self, name):
        super().__init__(name=name, mana_cost=30, damage_multiplier=2.3)

    def use_skill(self, caster, targets):
        caster.use_mana(self.mana_cost)
        # Put all damage logic in the same place (The one who is suffering damage would be a good place)
        targets[0].suffer_damage(caster.atk * self.damage_multiplier)

class Firebolt(SkillBase):
    def __init__(self, name):
        super().__init__(name=name, mana_cost=15, damage_multiplier=1.2)

    def use_skill(self, caster, targets):
        caster.use_mana(self.mana_cost)
        # Put all damage logic in the same place (The one who is suffering damage would be a good place)
        targets[0].suffer_damage(caster.atk * self.damage_multiplier)

class LightningStorm(SkillBase):
    def __init__(self, name):
        super().__init__(name=name, mana_cost=40, damage_multiplier=1.8)

    def use_skill(self, caster, targets):
        caster.use_mana(self.mana_cost)
        # Put all damage logic in the same place (The one who is suffering damage would be a good place)
        for target in targets:
            target.suffer_damage(caster.atk * self.damage_multiplier)

####################################################################################################################################

class Actor:
    
    def __init__(self):
        self.skill_list = {}  # empty skill list

    def _learn_skill(self, skill_name):   # Add a '_' in begin means it's a private function, others shouldn't call it.
        skill_object = SkillBase.skill_table[skill_name](skill_name)       # Add '()' to instaniate an object instance (require a name)
        self.skill_list[skill_name] = skill_object

    def use_skill(self, skill_name, targets):
        self.skill_list[skill_name].use_skill(self, targets)

    def use_mana(self):
        # bla bla...
        pass

class Mage(Actor):
    
    def __init__(self):
        # Assume Mage would have Firebolt and Lightning Storm
        self._learn_skill("Firebolt")
        self._learn_skill("Lightning Storm")

####################################################################################################################################


if __name__ == "__main__":

    it_is_a_mage = Mage()
    it_is_a_monster = Monster()     
    it_is_another_monster = Monster()

    # Mage cast Firebolt to a monster
    it_is_a_mage.use_skill("Firebolt", [it_is_a_monster])
    
    # Mage cast Lightning Storm to 2 monsters
    it_is_a_mage.use_skill("Lightning Storm", [it_is_a_monster, it_is_another_monster])



