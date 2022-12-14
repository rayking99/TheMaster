# TheMaster
Implementation of Spotify Pedalboard for Mastering.

You will need:

-  pip install pedalboard

-  pip install pyloudnorm

-  pip install soundfile

-  brew install ffmpeg



Highly recommend Fabfilter Pro-L2 and Oeksound Soothe 2 (they're a little bit expensive but top of the line.)

It's a pretty good levelling mastering engine - all the tracks in an album end up super close to -14 LUFS (or whatever you specify) and -1 true peak. 
- Note: at the moment -14 LUFS and -1 true peak are implemented by Spotify.. the levels set should result in no further changes to the tracks by them. 

I've set it to -13.5 as this will result in just a little louder than -14.. the results are below.

Sound quality is pretty amazing with the 32x oversample on L2 and a good Soothe preset - you can change these settings in the TheMaster.py if you like. 

It's very simply built - just input the folder name of inputs, folder name of outputs and hit run. 

It will work with WAV but you may need to convert other types of files to WAV using the ConvertToWav.py. 

I found that this was a pretty good solution to create a nicely levelled album without steamrolling it etc. However - if your tracks are sitting at -7LUFS with a -0.1 true peak and you're trying to get them to -14LUFS, -1 TP... you'll likely get an Imagine dragons kind of thing. 

You'll get an output file with it too:

|    | trackname           | samplerate | pre-loudness | post-loudness | truepeak-before | truepeak-after |
|----|---------------------|------------|--------------|---------------|-----------------|----------------|
| 0  | 3 only love         | 44100      | -16.42       | -13.97        | -0.1            | -1.0           |
| 1  | 2 inmyarms          | 44100      | -12.29       | -13.72        | -0.1            | -1.2           |
| 2  | 10 usic             | 44100      | -14.10       | -13.63        | -0.1            | -1.0           |
| 3  | blue                | 44100      | -23.52       | -12.96        | 13.4            | -2.4           |
| 4  | 7 sununtomoon       | 44100      | -14.29       | -14.32        | -0.1            | -1.0           |
| 5  | 11 lifeline         | 44100      | -16.48       | -13.65        | -0.1            | -1.0           |
| 6  | 8 yo                | 44100      | -13.56       | -13.97        | -0.1            | -1.0           |
| 7  | 13 adore            | 44100      | -15.26       | -13.89        | -0.1            | -1.0           |
| 8  | 5 rous              | 44100      | -20.12       | -13.88        | -4.6            | -1.0           |
| 9  | 4 tada              | 44100      | -7.95        | -13.91        | -0.1            | -5.6           |
| 10 | 15 cheerio          | 44100      | -10.46       | -13.96        | -0.1            | -3.1           |
| 11 | 12 beperfect        | 48000      | -19.25       | -13.93        | -9.9            | -2.7           |
| 12 | 6 skalet            | 44100      | -12.40       | -13.99        | -0.1            | -1.1           |
| 13 | 9 bu                | 44100      | -7.20        | -13.37        | 0.1             | -6.3           |
| 14 | (Bonus) postman pat | 44100      | -12.67       | -13.61        | -0.0            | -1.0           |
| 15 | 1 hey               | 44100      | -13.94       | -13.92        | -0.1            | -1.0           |
| 16 | 14 smile            | 44100      | -13.04       | -13.71        | -0.1            | -1.0           |
