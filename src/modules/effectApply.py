import sys

sys.path.append('/home/pi/project_nrsss0555407/src/python-audio-effects/pysndfx')

from pysndfx import AudioEffectsChain

fx = ( 
	AudioEffectsChain().highshelf()[''].lowshelf()

)

infile = '/home/pi/project_nrsss0555407/src/audioFiles/file.wav'
outfile = '/home/pi/project_nrsss0555407/src/audioFiles/modulated.wav'

fx(infile, outfile)
