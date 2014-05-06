INFINITY = 50000000
def levenshtein(s1, s2):
    if len(s1) < len(s2):
        return levenshtein(s2, s1)
 
    # len(s1) >= len(s2)
    if len(s2) == 0:
        return len(s1)
 
    previous_row = xrange(len(s2) + 1)
    for i, c1 in enumerate(s1):
        current_row = [i + 1]
        for j, c2 in enumerate(s2):
            insertions = previous_row[j + 1] + 1 # j+1 instead of j since previous_row and current_row are one character longer
            deletions = current_row[j] + 1       # than s2
            substitutions = previous_row[j] + (c1 != c2)
            current_row.append(min(insertions, deletions, substitutions))
        previous_row = current_row
 
    return previous_row[-1]
	
class Word :
	def __init__(self, word, keywords):
		self.word = word;
		self.keywords = keywords;
		self.minLev = INFINITY;

cmd_list[0] = Word("MOVE", {"va", "aller"});
cmd_list[1] = Word("ATTACK", {"attaque", "attaque", "frappe"});
cmd_list[2] = Word("TAKE", {"prend", "attrape"});
cmd_list[3] = Word("TALK", {"parle", "parler"});
cmd_list[4] = Word("SEE", {"arme", "armure", "vie", "pv"});
cmd_list[5] = Word("QUIT", {"arreter", "stop"});
cmd_list[6] = Word("PASS", {"passe"});
cmd_list[7] = Word("REPEAT", {"recommence", "encore", "pareil", "idem"});

dir_list[0] = Word("NORTH", {"nord"});
dir_list[1] = Word("EAST", {"est"});
dir_list[2] = Word("WEST",{"ouest"});
dir_list[3] = Word("SOUTH", {"sud"});

stt_list[0] = Word("WEAPON", {"arme"});
stt_list[1] = Word("ARMOUR", {"armure"});
stt_list[2] = Word("HP", {"vie", "pv"});

def build_mnt_list(control):
	i = 0;
	mnt_list = [100];
	for mnt in control.currentRoom.characters:
		if mnt.clss == "MSTR" : mnt_list[i] = Word(mnt.name.upper(), {mnt.name.lower()}); ++i;
	return mnt_list;

def build_itm_list(control):
	i = 0;
	itm_list = [100];
	for itm in control.currentRoom.items:
		itm_list[i] = Word(itm.name.upper(),{itm.name.lower()});
		++i;
	return itm_list;
	
def build_npc_list(control):
	i = 0;
	npc_list = [100];
	for npc in control.currentRoom.characters:
		if npc.clss == "NPC" : npc_list[i] = Word(npc.name.upper(),{npc.name.lower()}); 
		++i;
	return npc_list;

def try_word(str, type, control, treshold):
	list = [100];
	if type == "cmd" : list = cmd_list;
	if type == "dir" : list = dir_list;
	if type == "mnt" : list = build_mnt_list(control);
	if type == "itm" : list = build_itm_list(control);
	if type == "npc" : list = build_npc_list(control);
	if type == "stt" : list = stt_list;
	
	i = 0;
	while i < len(list):
		j = 0;
		while j < len(list[i].keywords):
			list[i].minLev = min(list[i].minLev, levenshtein(keywords[j]));
			++j;
		++i;
	
	i = 0;
	final = None;
	f_lev = INFINITY;
	while i < len(list):
		if (f_lev > list[i].minLev && list[i].minLev < treshold):
			f_lev = list[i].minLev;
			final = list[i].word;
		++i;
	return final;
			
	
def buildCommand(input, control): #input : string; control : GameEngine.Control
	sequence = input.split(' ');
	seq_size = len(sequence);
	seq_ptr = 0;
	type = "cmd"";
	cmd = "";
	while(seq_ptr < seq_size):
		word = try_word(sequence[seq_ptr], type, control, 10);
		if word != None : cmd += word + " ";
		if word == "MOVE"   : type = "dir";
		if word == "ATTACK" : type = "mnt";
		if word == "TAKE"	: type = "itm";
		if word == "TALK"	: type = "npc";
		if word == "SEE"	: type = "stt"; --seq_ptr;
		if word == "QUIT"	: break;
		if word == "PASS"	: break;
		if word == "REPEAT"	: break;
		seq_ptr += 1;
	return cmd;