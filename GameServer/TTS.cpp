// File : TTS.cpp
// Description : TTS engine part for speech server
// Authors : Stanislas "IfElseSwitch" Mur & Jean-Vincent "Irkam" Hay

#include <speak_lib.h>
#include <string>
#include <malloc.h>

using namespace std;

espeak_POSITION_TYPE position_type;
espeak_AUDIO_OUTPUT output;
char *path = NULL;
int Buflength = 500, Options = 0;
void* user_data;
t_espeak_callback *SynthCallback;
espeak_PARAMETER Parm;

char Voice[] = { "default" };
unsigned int Size, position = 0, end_position = 0, flags = espeakCHARS_AUTO, *unique_identifier;

void say(string text){
	output = AUDIO_OUTPUT_PLAYBACK;
	int I, Run = 1, L;
	espeak_Initialize(output, Buflength, path, Options);
	espeak_SetVoiceByName(Voice);
	Size = strlen(text) + 1;
	espeak_Synth(text, Size, position, position_type, end_position, flags,
		unique_identifier, user_data);
	espeak_Synchronize();
}