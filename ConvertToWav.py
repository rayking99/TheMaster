import soundfile
import glob
from pathlib import Path

'''
Currently it is set to 'float32' ... 'PCM_24' or 'PCM_16' also ok
'''

files = glob.glob('/path/to/input/**.flac', recursive=True)

for file in files:
    filename = Path(file).stem
    data, samplerate = soundfile.read(file)
    soundfile.write('path/to/output/file.wav', data, samplerate, subtype='float32')

    soundfile.write()



