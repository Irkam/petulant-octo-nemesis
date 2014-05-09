INFINITY = 50000000
def levenshtein(seq1, seq2):
    s = ' ' + seq1
    t = ' ' + seq2
    d = {}
    S = len(s)
    T = len(t)
    for i in range(S):
        d[i, 0] = i
    for j in range (T):
        d[0, j] = j
    for j in range(1,T):
        for i in range(1,S):
            if s[i] == t[j]:
                d[i, j] = d[i-1, j-1]
            else:
                d[i, j] = min(d[i-1, j] + 1, d[i, j-1] + 1, d[i-1, j-1] + 1)
    return d[S-1, T-1]


class Word:
    def __init__(self, word, keywords):
        self.word = word
        self.keywords = keywords
        self.minlev = INFINITY

cmd_list = [Word("MOVE", ["va", "aller"]), Word("ATTACK", ["attaque", "attaque", "frappe"]), Word("TAKE", ["prend", "attrape"]), Word("TALK", ["parle", "parler"]), Word("SEE", ["arme", "armure", "vie", "pv"]), Word("QUIT", ["arreter", "stop"]), Word("PASS", ["passe"]), Word("REPEAT", ["recommence", "encore", "pareil", "idem"])]

dir_list = [Word("NORTH", ["nord"]), Word("EAST", ["est"]), Word("WEST",["ouest"]), Word("SOUTH", ["sud"])]

stt_list = [Word("WEAPON", ["arme"]), Word("ARMOUR", ["armure"]), Word("HP", ["vie", "pv"])]

def build_mnt_list(control):
    i = 0;
    mnt_list = [100];
    for mnt in control.currentRoom.characters:
        if mnt.clss == "MSTR" :
            mnt_list[i] = Word(mnt.name.upper(), [mnt.name.lower()])
            ++i
    return mnt_list;


def build_itm_list(control):
    i = 0
    itm_list = [100]
    for itm in control.currentRoom.items:
        itm_list[i] = Word(itm.name.upper(), [itm.name.lower()])
        ++i
    return itm_list


def build_npc_list(control):
    i = 0
    npc_list = [100]
    for npc in control.currentRoom.characters:
        if npc.clss == "NPC":
            npc_list[i] = Word(npc.name.upper(), [npc.name.lower()])
            ++i
    return npc_list


def try_word(vox_str, _type, control, treshold):
    #print("WORD :", vox_str)
    _list = [100]
    empty = [100]
    if _type == "cmd":
        _list = cmd_list
    if _type == "dir":
        _list = dir_list
    if _type == "mnt":
        _list = build_mnt_list(control)
    if _type == "itm":
        _list = build_itm_list(control)
    if _type == "npc":
        _list = build_npc_list(control)
    if _type == "stt":
        _list = stt_list

    if _list == empty:
        return ""
    
    for word in _list:
        word.minlev = INFINITY
    i = 0
    while i < len(_list):
        j = 0
        while j < len(_list[i].keywords):
            lev = levenshtein(_list[i].keywords[j], vox_str)
            _list[i].minlev = min(_list[i].minlev, lev)
            #print(_list[i].keywords[j], ":",lev,"/",_list[i].minlev)
            j += 1
        i += 1

    i = 0
    final = None
    f_lev = INFINITY
    while i < len(_list):
        if f_lev > _list[i].minlev and _list[i].minlev < treshold:
            f_lev = _list[i].minlev
            final = _list[i].word
        i += 1
    return final



def buildCommand(vox_input, control): #input : string; control : GameEngine.Control
    print(vox_input)
    sequence = vox_input.split(' ')
    seq_size = len(sequence)
    seq_ptr = 0
    _type = "cmd"
    cmd = ""
    while seq_ptr < seq_size:
        word = try_word(sequence[seq_ptr], _type, control, len(sequence[seq_ptr]))
        if word != None:
            cmd += word + " "
        if word == "MOVE":
            _type = "dir"
        if word == "ATTACK":
            _type = "mnt"
        if word == "TAKE":
            _type = "itm"
        if word == "TALK":
            _type = "npc"
        if word == "SEE":
            _type = "stt"
            seq_ptr -= 1
        if word == "QUIT":
            break
        if word == "PASS":
            break
        if word == "REPEAT":
            break
        seq_ptr += 1
        
    print(cmd)
    return cmd;