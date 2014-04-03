# _*_ coding: utf8 _*_
## File : GameCore.py
## Description : Core classes for the Zork-like game engine
## Authors : Stanislas "IfElseSwitch" Mur & Jean-Vincent "Irkam" Hay

def printline(line):
    print (line + "\n")

def formatClss(clss):
    if   clss == "MSTR" : return "Monstre : "
    elif clss == "NPC"  : return "PNJ : "
    elif clss == "WPN"  : return "Arme : "
    elif clss == "ARMR" : return "Armure : "
    elif clss == "HEAL" : return "Soins : "
    elif clss == "BST"  : return "Boost : "
    else : return ""
    
##CHARACTERS
class Character :
    clss = "NA"
    def __init__(self, name, hp, maxHP, weapon, armour):
        self.name = name
        self.hp = hp
        self.maxHP = maxHP
        self.weapon = weapon
        self.armour = armour
    def attack(self, target):
        dmg = self.weapon.mod - target.armour.mod
        target.hp -= dmg
        out = ""
        verbForm = ""
        Targname = target.name + " "
        if self.clss == "PLYR":
            out += "Vous "
            verbForm = "avez"
        elif target.clss == "PLYR":
            out += self.name + " "
            Targname = ""
            verbForm = "vous a"
        else :
            out += self.name + " "
            verbForm = "a"
        out += verbForm + " attaqué " + Targname + "et " + verbForm + " infligé {0} degats.".format(dmg)
        return out
    def take(self, item):
        out = ""
        if (item.clss == "WPN") :
            self.weapon = item
            out = self.name + " s'est équipé de " + item.name + "({0} degats)".format(item.mod)
        elif (item.clss == "ARMR") :
            self.armour = item
            out = self.name + " s'est équipé de " + item.name + "({0} protection)".format(item.mod)
        elif (item.clss == "HEAL") :
            self.hp = min(self.maxHP, self.hp + item.mod)
            out = self.name + " s'est soigné de {0} pv".format(item.mod)
        elif (item.clss == "BST") :
            self.maxHP += item.mod
            out = self.name + " a boosté ses PV max de {0} pv".format(item.mod)
        elif (item.clss == "TRP") :
            self.hp -= item.mod
            out = self.name + " est tombé dans un piège " + item.name + " et a reçu {0} degats".format(item.mod)
        return out

class Player(Character):
    clss = "PLYR"
    def __init__(self):
        Character.__init__(self, "Joueur", 5, 100, Weapon("", 1), Armour("", 0))

class Monster(Character):
    clss = "MSTR"
    def __init__(self, name, hp, maxHP, weapon, armour):
        Character.__init__(self, name, hp, maxHP, weapon, armour)
class NPC(Character):
    clss = "NPC"
    def __init__(self, name, hp, maxHP, weapon, armour, dialog):
        Character.__init__(self, name, hp, maxHP, weapon, armour)
        self.dialog = dialog
        
## ITEMS
class Item :
    def __init__(self, name, mod):
        self.name = name
        self.mod = mod
class Weapon(Item):
    clss = "WPN"
    def __init__(self, name, mod):
        Item.__init__(self, name, mod)
        
class Armour(Item):
    clss = "ARMR"
    def __init__(self, name, mod):
        Item.__init__(self, name, mod)

class Heal(Item):
    clss = "HEAL"
    def __init__(self, name, mod):
        Item.__init__(self, name, mod)

class Boost(Item):
    clss = "BST"
    def __init__(self, name, mod):
        Item.__init__(self, name, mod)
class Trap(Item):
    clss = "TRP"
    def __init__(self, name, mod, fakeclss):
        self.fakeclss = fakeclss
        Item.__init__(self, name, mod)

##ROOMS    

def createNextRooms(room_North, room_South, room_East, room_West):
	return {'NORTH':room_North, 'SOUTH':room_South, 'EAST':room_East, 'WEST':room_West}

class Room :
    def __init__(self, outstrs, characters, items, nextRooms):
        self.outstrs = outstrs
        self.characters = characters
        self.items = items
        self.nextRooms = nextRooms
    def enterRoom(self):
        out = ""
        out += (self.outstrs[0])
        out += " Vous y voyez : \n"
        for ch in self.characters:
            clss = formatClss(ch.clss)
            out += "\t" + clss + ch.name + "\n"
        for it in self.items :
            clss = ""
            if it.clss != "TRP" : clss = formatClss(it.clss)
            else : clss = formatClss(it.fakeclss)
            out += "\t" + clss +it.name + "\n"
        out += "Le chemin part : \n"
        if (self.nextRooms == None) : return out
        if self.nextRooms["NORTH"] != None : out += "\t-au Nord\n"
        if self.nextRooms["SOUTH"] != None : out += "\t-au Sud\n"
        if self.nextRooms["EAST"]  != None  : out += "\t-a l'Est\n"
        if self.nextRooms["WEST"]  != None  : out += "\t-a l'Ouest\n"
        return out
        
    def isClear(self) :
        for ch in self.characters:
            if ch.clss == "MSTR" : return False
        return True
            
