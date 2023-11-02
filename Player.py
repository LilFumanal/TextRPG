"""classe fille définissant les joueurs """
from Character import Character
import random

class Player(Character):
  def __init__(self, name, pv_max = 20, pv = 20, attk_dmg = 5, buff_attack = 0, buff_pv = 0, exp = 0, lvl = 1) -> None:
    super().__init__(name, pv, pv_max)
    self.attk_dmg = attk_dmg
    self.buff_attack: int  = buff_attack
    self.buff_pv: int = buff_pv
    self.exp: int = exp
    self.lvl: int = lvl
    
  def readDetails(self):
    """Obtiens les détails du joueur"""
    attk = self.buff_attack + self.attk_dmg
    maxpv = self.pv_max + self.buff_pv
    print(f"***** VOUS ****** \nNom: {self.name} \nAttaque : {attk},\nPV: {self.pv} / {maxpv} \nLevel: {self.lvl}\n Experience: {self.exp}")
  
  def attack(self, target):
    """Attaque une cible, lui infligeant des dégats fixes ainsi que des dégats aléatoires"""
    total = (self.attk_dmg) + (random.randint(0, 5))
    target.pv = target.pv - total
    print(f"{self.name} attack! {total} damages done!")
    
  def heal(self):
    """Soigne le joueur de 20% des points de vie max"""
    if self.pv < self.pv_max:
      add = self.pv_max / 100 * 20
      self.pv += add
      print(f"Healed: + {add} pvs")
    else:
      print("You're already full-life!")
    
  def level_up(self):
    """Monte d'un niveau, ajoutant des bonus de PV et d'attaque"""
    self.lvl += 1
    self.buff_pv= self.buff_pv + self.pv_max / 100 * 20
    self.buff_attack= self.buff_attack + self.attk_dmg / 100 * 20
    self.exp = 0
    print(f"Vous gagnez un niveau. \n Bonus d'attaque:{self.buff_attack} \n Bonus de PV:{self.buff_pv}")
    
  def level_down(self):
    """Perd un niveau, enlevant des bonus de PV et d'attaque"""
    if self.lvl > 1:
      self.lvl -= 1
      self.buff_pv= self.buff_pv - self.pv_max / 100 * 20
      self.buff_attack= self.buff_attack - self.attk_dmg / 100 * 20
      self.exp = 0
      print(f"Vous perdez un niveau. \n Bonus d'attaque: {self.buff_attack} \n Bonus de PV: {self.buff_pv}")
    else:
      print("Vous êtes déjà niveau 1, vous ne pouvez pas perdre de niveau. Vous êtes donc mort")
      exit()