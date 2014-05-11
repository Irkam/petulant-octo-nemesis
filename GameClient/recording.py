import os
def record(outputfilename):
	os.system("rm " + outputfilename)
	cmd = "rec --rate 16k " + outputfilename + " silence 1 0.1 1% 1 3.0 3%"
	os.system(cmd)