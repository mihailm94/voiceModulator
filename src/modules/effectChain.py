
#this bad boy writes a python script

#the only function takes a string as an argument

#the string is built from an array that gets parsed to a string

#the string contains the names of the desired effects

def writeFile(string):

    #open file for writing
    file = open("./project_nrsss0555407/src/modules/effectApply.py", "w")

    file.write("import sys")
    file.write("\n\n")
    
    #append to sys path cause you cannot import directly from another folder
    file.write("sys.path.append(\'./project_nrsss0555407/src/python-audio-effects/pysndfx\')")
    file.write("\n\n")

    file.write("from pysndfx import AudioEffectsChain")
    file.write("\n\n")

    file.write("fx = ( ")
    file.write("\n")

    file.write("\tAudioEffectsChain()")
    
    #should always be applied
    file.write(".highshelf()")

    #our magic
    file.write(string)

    #should always be applied
    file.write(".lowshelf()")


    file.write("\n\n")
    file.write(")")
    file.write("\n\n")

    file.write("infile = \'./project_nrsss0555407/src/audioFiles/file.wav\'")
    file.write("\n")

    file.write("outfile = \'./project_nrsss0555407/src/audioFiles/modulated.wav\'")
    file.write("\n\n")

    file.write("fx(infile, outfile)")
    file.write("\n")

    #closing is important
    file.close()


