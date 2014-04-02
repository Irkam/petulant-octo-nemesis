from GameCore import *

def input_uppper(prompt):
    return input(prompt).upper()

outfct = print
infct = input_uppper

class Control:
    def __init__(self, startRoom):
        self.currentRoom = startRoom
        self.player = Player()
        self.lastCmd = ""
        self.isRun = False
    def seekCharacter(self, characterName):
        for character in self.currentRoom.characters:
            if character.name.upper() == characterName :
                return character
        return None
    def seekItem(self, itemName):
        for item in self.currentRoom.items:
            if item.name.upper() == itemName : return item
        return None
    def interpret(self, cmd):
        cmd_e = cmd.split(" ", 1)
        if cmd_e[0] == "QUIT" :
            self.isRun = False
            return
        if cmd_e[0] == "PASS" : return
        if cmd_e[0] == "ATTACK" and len(cmd_e) == 2:
            target = self.seekCharacter(cmd_e[1])
            if target != None:
                out = self.player.attack(target)
                outfct(out)
            else : outfct("Cible invalide")
        elif cmd_e[0] == "TAKE" and len(cmd_e) == 2:
            item = self.seekItem(cmd_e[1])
            if item != None:
                out = self.player.take(item)
                outfct(out)
        elif cmd_e[0] == "TALK" and len(cmd_e) == 2 :
            target = self.seekCharacter(cmd_e[1])
            if target != None and target.clss == "NPC":
                outfct(target.name + " : " + target.dialog)
        elif cmd_e[0] == "SEE" and len(cmd_e) == 2 :
            if cmd_e[1] == "WEAPON" :
                outfct(self.player.weapon.name + " : {0} dmg".format(self.player.weapon.mod))
            elif cmd_e[1] == "ARMOUR" :
                outfct(self.player.armour.name + " : {0} res".format(self.player.armour.mod))
            elif cmd_e[1] == "HP" :
                outfct("{0}/{1}".format(self.player.hp, self.player.maxHP))
        elif cmd_e[0] == "REPEAT" and len(cmd_e) == 1 :
            self.interpret(self.lastCmd)
        elif cmd_e[0] == "MOVE" and len(cmd_e) == 2 :
            if self.currentRoom.isClear():
                if self.currentRoom.nextRooms != None and self.currentRoom.nextRooms[cmd_e[1]] != None:
                    self.currentRoom = self.currentRoom.nextRooms[cmd_e[1]]
                    outfct(self.currentRoom.enterRoom())
                else : 
                    outfct("Impossible d'aller par là.")
            else :
                outfct("Le chemin est barré par des ennemis")
        else : outfct("Erreur.")
    def check(self):
        out = ""
        for character in self.currentRoom.characters:
            if character.hp <= 0 :
                out += character.name + " est mort.\n"
                self.currentRoom.characters.remove(character)
            elif character.clss == "MSTR" :
                    out += character.attack(self.player) + "\n"
        if self.player.hp <= 0:
            out += "Vous êtes mort.\n"
            self.isRun = False
        return out
    def run (self):
        cmd = ""
        out = self.currentRoom.enterRoom()
        outfct(out)
        self.isRun = True
        while self.isRun == True:
            cmd = infct(">")
            self.interpret(cmd)
            if (cmd != "REPEAT"):
                self.lastCmd = cmd
            out = self.check()
            outfct(out)
