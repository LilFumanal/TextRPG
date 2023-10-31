"""Classe mère de tous les personnages du jeu"""
from abc import ABC, abstractmethod

class Character(ABC):
  def __init__(self, name, pv, attk_dmg) -> None:
    self.name: str = name
    self.pv: int = pv
    self.attk_dmg: int = attk_dmg
  
  def readDetails(self):
    """Récupérer les détails du joueur"""
    print(self.name, "has", self.pv, "PV and will attack with", self.attk_dmg, "damages.")
  
  @abstractmethod
  def attack(Target):
    """Méthode abstraite, l'attaque se joue différemment si le monstre ou le joueur est attaquant."""
    pass
