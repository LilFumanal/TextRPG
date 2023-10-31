"""Classe mère de tous les personnages du jeu"""
from abc import ABC, abstractmethod

class Character(ABC):
  def __init__(self, name, pv, pv_max) -> None:
    self.name: str = name
    self.pv: int = pv
    self.pv_max: int = pv_max
  
  @abstractmethod
  def readDetails(self):
    """Récupérer les détails du joueur"""
    pass
  
  @abstractmethod
  def attack(Target):
    """Méthode abstraite, l'attaque se joue différemment si le monstre ou le joueur est attaquant."""
    pass
