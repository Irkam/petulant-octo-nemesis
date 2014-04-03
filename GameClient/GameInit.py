# _*_ coding: utf8 _*_
## File : GameInit.py
## Description : Initialisation of Zork-like game
## Authors : Stanislas "IfElseSwitch" Mur & Jean-Vincent "Irkam" Hay

from GameCore import *
from GameEngine import *
R1 = Room(["Vous êtes dans une clairière"], [NPC("Charles", 5, 5, Weapon("", 1), Armour("", 0), "Au revoir.")], [Weapon("Epee", 2)], None)
nextR = createNextRooms(R1 ,None, None, None)
R0 = Room(["Vous êtes dans une fôret.", "La fôret est dense."], [Monster("Gobelin", 3, 3, Weapon("", 1), Armour("", 0)), NPC("Henry", 5, 5, Weapon("", 1), Armour("", 0), "Bonjour.")], [Armour("Cuir", 1)], nextR)
ctr = Control(R0)
ctr.run()
input("Appuyez sur entrée pour fermer.")
