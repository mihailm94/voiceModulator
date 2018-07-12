#this python script attaches the effects to be attached to the recorded file
import sys
sys.path.append('../pysndfx')
from pysndfx import AudioEffectsChain

fx = (
    AudioEffectsChain()
    .highshelf()
    .reverb()
    .phaser()
    .delay()
    .lowshelf()
)

infile = './audioFiles/file.wav'
outfile = './audioFiles/modulated.wav'


fx(infile, outfile)
