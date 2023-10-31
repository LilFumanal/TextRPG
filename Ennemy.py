"""Classe fille de Character définissant les ennemis"""
from Character import Character
from Player import Player
from random import *


class Ennemy(Character):
    def __init__(self, name:str = "Gobelin", pv:int = 30, pv_max:int=30, XP:int = 10):
        super().__init__(name, pv, pv_max)
        self.XP = XP

    def attack(self, target):
      """Méthode attaque définissant l'attaque ennemie"""
      dmg = randint(0,(target.attk_dmg+target.buff_attk)) 
      target.pv = target.pv-dmg
      print(f"{self.name} has done {dmg} damage")
            
    def readDetails(self, target):
      "Donne les détails de l'ennemis: la range de son attaque, ses PVs, et l'expérience qu'il donnera si vaincu"
      print(f"Attack from 0 to {target.attk_dmg + target.buff_attk} \n 
      PV: {self.pv} / {self.pv_max} \n 
      Points d'experience: {self.XP} \n ")
