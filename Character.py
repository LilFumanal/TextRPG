from abc import ABC, abstractmethod

class Character(ABC):
  def __init__(self, name, pv, attk_dmg) -> None:
    self.name = name
    self.pv = pv
    self.attk_dmg = attk_dmg
  
  def readDetails(self):
    print(self.name, "has", self.pv, "and will attack with", self.attk_dmg, "damages")
  
  @abstractmethod
  def attack(Target):
    pass
