"""Classe fille de Character définissant les ennemis"""
from Character import Character
from Player import Player
from random import *


class Ennemy(Character):
    def __init__(self, name:str = "Gobelin", pv:int = 30, pv_max:int=30, xp:int = 10):
        super().__init__(name, pv, pv_max)
        self.xp = xp

    def attack(self, target):
      """Méthode attaque définissant l'attaque ennemie"""
      if self.pv <= 0:
        pass
      else: 
        x = target.attk_dmg+target.buff_attack
        dmg = randint(0, x) 
        target.pv = target.pv-dmg
        print(f"{self.name} has done {dmg} damage")
            
    def readDetails(self, target):
      "Donne les détails de l'ennemi: la puissance de son attaque, ses PVs, et l'expérience qu'il donnera si vaincu"
      total = target.attk_dmg + target.buff_attack
      print(f"****** MONSTRE ****** \n{self.name}  \nAttaque entre 0 et {total} \nPV: {self.pv} / {self.pv_max} \nPoints d'experience: {self.xp} \n ")