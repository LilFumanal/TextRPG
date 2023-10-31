from Character import Character
from Player import Player
from random import *


"""classe fille de Character déffinissant les ennemies"""
class Ennemy(Character):
    def __init__(self, name:str = "gobelins", pv:int = 30, pv_max:int=30, XP:int = 10):
        super().__init__(name, pv, pv_max)
        self.XP = XP

        """Méthode attaque défiissant l'attaque ennemie"""
        def attack(Target):
            dmg = randint(0,(Player.attk_dmg+Player.buff_attk))
            Target.pv = Target.pv-dmg
            print(f"{name} has done {dmg} damage")
        def readDetails(self):
            
