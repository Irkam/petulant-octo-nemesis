from GameCore import *
from GameEngine import *


room = Room(["Vous êtes dans une fôret.", "La fôret est dense."], [Monster("Gobelin", 3, 3, Weapon("", 1), Armour("", 0)), NPC("Henry", 5, 5, Weapon("", 1), Armour("", 0), "Bonjour.")], [Armour("Cuir", 1)], None)
ctr = Control(room)
ctr.run()
input("Appuyez sur entrée pour fermer.")
