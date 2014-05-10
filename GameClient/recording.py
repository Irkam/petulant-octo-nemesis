import os
def record(outputfilename):
	os.system("rm " + outputfilename)
	cmd = "rec --rate 16k " + outputfilename + " silence 1 0.2 1% 1 1.0 2%"
	os.system(cmd)