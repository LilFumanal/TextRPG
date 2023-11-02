"""Fichier principal définissant le dérouement du jeu"""
from Player import Player
from Ennemy import Ennemy

def create_player():
    """Fonction permettant de donner un nom a la classe joueur"""
    nom = input(f"Bonjour jeune aventurier, quel est votre nom ? \n")
    print(f"{nom}, c'est ça ? Bienvenue dans le donjon Deathtrap")
    adventurer = Player(nom)
    return adventurer

def combat(adventurer, monster):
  """propose des actions pour combattre le monstre et affiche l'état du joueur et du monstre (pv, attaque...)"""
  while adventurer.pv > 0 and monster.pv > 0:
    monster.readDetails(adventurer)
    adventurer.readDetails()
    r = input("1: ATTAQUER \n2: FUIR \n")
    if r == "1":
      adventurer.attack(monster)
      monster.attack(adventurer)
      combat(adventurer, monster)
    elif r == "2":
      print("Vous avez fuit le combat. \n GAME OVER")
      exit()
    else :
      print("Veuillez taper 1 ou 2.")
      combat(adventurer, monster)
  life_time(adventurer, monster)

def init_combat(adventurer):
    """Pemret d'initier le combat entre le joueur et le monstre"""
    monster = Ennemy()
    print(f"Un {monster.name} apparait devant vous! Que faites-vous ?")
    combat(adventurer, monster)
    
def life_time(adventurer, monster):
    """Définis ce"""
    if adventurer.pv <= 0:
      print("Oh non, vous êtes morts!")
      if adventurer.lvl < 1:
        print("Pas de chance! Adieu.")
        exit()
      else:
        print("Vous perdez un niveau et votre expérience acquise.")
        adventurer.level_down()
        init_combat(adventurer)
    elif monster.pv <= 0:
      print("OHLALA vous avez gagné!")
      exp_up(adventurer, monster)
      init_combat(adventurer)
    else :
      print ("Votre combat a été interrompu de manière inattendue...")
      exit()

def exp_up(adventurer, monster):
  adventurer.exp += monster.xp
  print(f"Vous gagnez {monster.xp}")
  if adventurer.exp >= 100:
    print("Oh! Vous montez d'un niveau!")
    adventurer.level_up()

def main():
  game =  create_player()
  init_combat(game)
  
main()