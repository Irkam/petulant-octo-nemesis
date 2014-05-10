# _*_ coding: utf8 _*_
## File : GameInit.py
## Description : Initialisation of Zork-like game
## Authors : Stanislas "IfElseSwitch" Mur & Jean-Vincent "Irkam" Hay

from GameCore import *
from GameEngine import *
#WEAPONS
no_weapon = Weapon("Aucune arme", 1)
stick = Weapon("Baton", 2)
knife = Weapon("Couteau", 3)
sword = Weapon("Epee", 5)
whip = Weapon("Fouet", 4)
flail = Weapon("Fleau", 6)
axe = Weapon("Hache", 7)
katana = Weapon("Katana", 8)
gun = Weapon("Pistolet", 10) #ULTIMATE WEAPON
MACHINEGUN = Weapon("Mitraillette", 100) #SECRET ULTIMATE WEAPON

#ARMOURS
no_armour = Armour("Aucune armure", 0)
leather = Armour("Cuir", 1)
mail = Armour("Mailles", 3)
plaq = Armour("Plaques", 5)
mithril = Armour("Mithril", 7) #ULTIMATE ARMOUR
PEGASUS = Weapon("Pegase", 10) #SECRET ULTIMATE ARMOUR

#MONSTERS
gob = Monster("Gobelin", 3, 3, stick, no_armour)
hob = Monster("Hobgobelin", 5, 5, knife, no_armour)
zom = Monster("Zombie", 10, 10, whip, no_armour)
sol = Monster("Soldat", 10, 10, sword, mail)
che = Monster("Chevalier", 20, 20, flail, plaq)
bar = Monster("Barbare", 40, 40, axe, leather)
dem = Monster("Demon", 100, 100, katana, mithril) #GARDS SECRET ULTIMATE WEAPON
dra = Monster("Dragon", 70, axe, plaq) #GARDS SECRET ULTIMATE ARMOUR

#NPC
Henry = NPC("Henry", 5, 5, no_weapon, no_armour, "Bonjour.")

#ROOMS
#tutorial rooms
nextR = createNextRooms(room_0, None, None, None)
tuto_4 = Room(["Vous êtes presque pret à partir à l'aventure. Pour savoir votre santé actuelle, dite vie. Pour connaitre votre arme, dites arme, et pour votre armure, dite armure. Sachez enfin que dire stop ou arrete ferme le jeu. Allez au nord pour commencer."], [],[], nextR)
nextR = createNextRooms(tuto_4, None, None, None)
tuto_3 = Room(["Très bien. Maintenant, vous allez vous battre. Dites attaque ou frappe puis le nom du monstre pour l'attaquer. Par exemple ici, vous devrez dire frappe le gobelin. Vous pouvez aussi repeter la dernière action en disant encore, pareil, idem, ou recommence. Vous pouvez aussi passer un tour, mais je n'en voit pas l'interet. Les monstres vous enpêchent de quitter la salle. Battez-les, puis allez au Nord"],[gob], [], nextR)
nextR = createNextRooms(tuto_3, None, None, None)
tuto_2 = Room(["Parfait. Vous rencontrerez parfois des personnages dans le jeu. Ils aurons peut etre un indice interessant. Pour leur parler, dites parle à ou parler à puis le nom du personnage. Vous pouvez essayer sur Henry. Ensuite, allez au Nord pour continuer"], [Henry],[], nextR)
nextR = createNextRooms(tuto_2, None, None, None)
tuto_1 = Room(["Bien. Pour prendre un objet, dites attrape ou prends puis le nom de l'objet. Maintenant, prenez l'armure de cuir qui est dans cette salle. Pour cela, vou pouvez simplement dire prends le cuir. Ensuite allez au Nord pour continuer"], [], [leather],nextR)
nextR = createNextRooms(tuto_1, None, None, None)
tuto_0 = Room(["Bienvenue aventurier ! Avant de commencer votre aventure, vous devez connaitre les ordres fondamentaux. Pour vous deplacer de salles en salles, dites va au puis la direction. Dites va au nord pour aller au nord. Dire aller au nord marche aussi. Allez au nord pour continuer le tutoriel."], [], [], nextR)

R1 = Room(["Vous êtes dans une clairière"], [NPC("Charles", 5, 5, no_weapon, , "Au revoir.")], [sword, None)
nextR = createNextRooms(R1 ,None, None, None)
R0 = Room(["Vous êtes dans une fôret.", "La fôret est dense."], [Henry], [Armour("Cuir", 1)], nextR)
ctr = Control(tuto_0)
ctr.run()
input("Appuyez sur entrée pour fermer.")
