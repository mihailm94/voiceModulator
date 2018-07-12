import sys

sys.path.append('./project_nrsss0555407/src/python-audio-effects/pysndfx')

from pysndfx import AudioEffectsChain

fx = ( 
	AudioEffectsChain().highshelf()[''].lowshelf()

)

infile = './project_nrsss0555407/src/audioFiles/file.wav'
outfile = './project_nrsss0555407/src/audioFiles/modulated.wav'

fx(infile, outfile)
