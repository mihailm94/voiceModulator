import sys

sys.path.append('../python-audio-effects/pysndfx')

from pysndfx import AudioEffectsChain

fx = ( 
	AudioEffectsChain().highshelf().reverb().delay().lowshelf()

)

infile = '../audioFiles/file.wav'
outfile = '../audioFiles/modulated.wav'

fx(infile, outfile)