import analyzation
import filecreate
import os
import glob
import time
import ast
import string
os.chdir("davids-thing/TestTexts/")
scanned = open("scanned.cfg","a+")
finalpercentage = open("percentage.file","a")

for file in glob.glob("*.txt"):
    f = open(file)
    if f.name not in scanned.readline(10000000):
        for line in f:
            line = ast.literal_eval(line) ### DO NOT CHANGE LITERAL EVAL. THIS IS A (CRAPPY) SECURITY FIX.
            lineperc = analyzation.PercentageCheckAbsolute(line)
            scanned.write(filecreate.GetNameAndTeamNum(line) + "\n")
            finalarray = []
            finalarray.append(str(lineperc))
            splitname = f.name.split("-")
            splitname = splitname[0] + " " + splitname[1]
            finalarray.append(splitname)
            finalarray = ' '.join(finalarray)
            finalpercentage.write(finalarray + "\n")
            f.close

    else:
        print "This array has already been inserted"
scanned.close
finalpercentage.close


        

    
