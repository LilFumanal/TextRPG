from Character import Character
import random

class Player(Character):
  def __init__(self, name, pv_max = 20, pv = 20, attk_dmg = 5, buff_attack = 0, buff_pv = 0, exp = 0, lvl = 1) -> None:
    super().__init__(name, pv, pv_max, attk_dmg)
    self.buff_attack: int = buff_attack
    self.buff_pv: int = buff_pv
    self.exp: int = exp
    self.lvl: int = lvl
    
  def readDetails(self):
    print("Attack", self.buff_attack + self.attk_dmg, "\n "
          "PV:", self.pv, "/", self.pv_max + self.buff_pv, "\n "
          "Level:", self.lvl, "\n "
          "Experience:", self.exp, "\n ")
  
  def attack(self, target):
    total = (self.attk_dmg) + (random.randint(0, 5))
    target.pv = target.pv - total
    print(self.name, "attack!", total, "damages done!")
    
  def heal(self, target):
    if target.pv == 0:
      self.pv = self.pv 

player1 = Player("Andrew")
player2 = Player("PIERRE")
player1.readDetails()

player1.attack(player2)
player2.readDetails()