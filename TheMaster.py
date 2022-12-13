import pandas as pd
from pedalboard import load_plugin,Pedalboard
from pedalboard.io import AudioFile
import glob
from pathlib import Path
import soundfile as sf
import pyloudnorm as pyln
import os

tracks = glob.glob('/path/to/**.wav')
# tracks = ['/Users/jaso/code/masters/548_pro/og/6 skalet.wav','/Users/jaso/code/masters/548_pro/og/12 beperfect.wav']
output_folder = '/path/out/'

pre_loud = []
post_loud = []
songs = []
rates = []
pre_peaks = []
post_peaks = []

for track in tracks:

    song_name_1 = Path(track).stem
    data,rate = sf.read(track)
    meter = pyln.Meter(rate)
    loudness = meter.integrated_loudness(data)

    print(song_name_1, '_', rate, ': ', loudness)

    lookfor = ', bitrate:'

    p = os.system(f"ffprobe -i '{track}' > output.txt 2>&1")

    if os.path.exists('output.txt'):
        fp = open('output.txt', "r")
        output = fp.readlines()
        fp.close()
        os.remove('output.txt')

    for line in output: 
        if lookfor in line:
            bitrate = line.split(lookfor,1)[1][1:5]
            print('bitrate : ',bitrate)
    
    os.system(f"ffmpeg -nostats -i '{track}' -filter_complex ebur128=peak=true -f null - > output.txt 2>&1")
    name = Path(track).stem
    output = open('output.txt').readlines()
    for line in output[-1:]:
        true_peak = line[16:-6]
        print('true_peak:', line[16:-6])

    pre_peaks.append(true_peak)


    '''
    PEDALBOARD_LOAD PLUGINS (PRO-L and SOOTHE)
    '''

    pro_l = load_plugin('/path/to/vsts/FabFilter Pro-L 2.vst3')
    pro_l.oversampling = 'Off'
    pro_l.filter_dc_offset = True
    pro_l.style = 'Transparent'
    pro_l.attack = '4100 ms'
    pro_l.release = '420 ms'
    pro_l.channel_link_transients = '100%'
    pro_l.channel_link_release = '50%'
    pro_l.lookahead = '4.6 ms'


    soothe = load_plugin('/path/to/vsts/soothe2.vst3')
    soothe.band_solo_on = False
    soothe.selected_band = -1
    soothe.sidechain_solo_on = False
    soothe.mode = 'soft'
    soothe.depth = 4.9
    soothe.sharpness = 5.0
    soothe.selectivity = 5.0
    soothe.attack = 'fast'
    soothe.release = 3.0
    soothe.low_cut_on = True
    soothe.low_cut_q = 0.7
    soothe.low_cut_freq_hz = 55
    soothe.low_cut_balance = 'even'
    soothe.low_cut_slope = '12 dB/oct'
    soothe.band1_on = True
    soothe.band1_freq_hz = 356
    soothe.band1_sens_db = 2.6
    soothe.band1_q = 0.6
    soothe.band1_balance = '100% | 73%'
    soothe.band1_mode = 'bell'
    soothe.band2_on = True
    soothe.band2_freq_hz = 906
    soothe.band2_sens_db = 1
    soothe.band2_q = 0.5
    soothe.band2_balance = '100% | 13%'
    soothe.band2_mode = 'bell'
    soothe.band3_on = True
    soothe.band3_freq_hz = '11k8'
    soothe.band3_sens_db = 4.4
    soothe.band3_q = 0.5
    soothe.band3_balance = '1% | 100%'
    soothe.band3_mode = 'bell'
    soothe.band4_on = True
    soothe.band4_freq_hz = 611
    soothe.band4_sens_db = 2.4
    soothe.band4_q = 1.0
    soothe.band4_balance = '100% | 73%'
    soothe.band4_mode = 'bell'
    soothe.high_cut_on = True
    soothe.high_cut_q = 0.7
    soothe.high_cut_freq_hz = '16k'
    soothe.high_cut_balance = 'even'
    soothe.high_cut_slope = '12 dB/oct'
    soothe.stereo_mode = 'mid | side'
    soothe.stereo_link = 0.0
    soothe.stereo_balance = 'even'
    soothe.offline_oversample = '4x'
    soothe.offline_resolution = 'ultra'
    soothe.oversample = 4
    soothe.resolution = 'ultra'
    soothe.mix = 100
    soothe.trim_db = 0
    soothe.delta = False
    soothe.bypass = False
    soothe.input_trim_db = '0.0 dB'


    '''
    SET TRUE PEAK &
    SET TARGET LOUDNESS

    '''
    target_output = -1
    target_loudness = -13.5 + abs(target_output)
    
    
    if loudness > target_loudness:
        gain = 1
        output = target_output + round((target_loudness-loudness),2)
        print('output = ',output)
    else:
        gain = abs(round(target_loudness-loudness,2))+1
        output = target_output

    print('gain L2 :',gain)
    pro_l.gain = f'+{gain} dB'
    pro_l.output_level = f'{output} dBTP'
    song_name = Path(track).stem  + '_mstrd'

    with AudioFile(track, 'r') as f:
        audio = f.read(f.frames)
        samplerate = f.samplerate

    board = Pedalboard([soothe,pro_l])

    effected_sound = board(audio, samplerate)

    track_out = f'{output_folder}/{song_name}.wav' 

    with AudioFile(track_out, 'w', samplerate, effected_sound.shape[0],quality='best',bit_depth=32) as f:
            f.write(effected_sound)

    p = os.system(f"ffprobe -i '{track_out}' > output.txt 2>&1")

    if os.path.exists('output.txt'):
        fp = open('output.txt', "r")
        output = fp.readlines()
        fp.close()
        os.remove('output.txt')

    for line in output: 
        if lookfor in line:
            bitrate = line.split(lookfor,1)[1][1:5]
            print('bitrate : ',bitrate)
    
    os.system(f"ffmpeg -nostats -i '{track_out}' -filter_complex ebur128=peak=true -f null - > output.txt 2>&1")
    name = Path(track).stem
    output = open('output.txt').readlines()
    for line in output[-1:]:
        true_peak_out = line[16:-6]
        print('true_peak:', line[16:-6])

    post_peaks.append(true_peak_out)


    data,rate = sf.read(track_out)
    meter = pyln.Meter(rate)
    post_loudness = meter.integrated_loudness(data)
    print('mstrd_: ',song_name_1, '_', rate, ': ', post_loudness)

    pre_loud.append(loudness)
    post_loud.append(post_loudness)
    songs.append(song_name_1)
    rates.append(rate)

df = pd.DataFrame()
df['track_name'] = songs
df['sample_rate'] = rates
df['pre_loudness'] = pre_loud
df['post_loudness'] = post_loud
df['true_peak_before'] = pre_peaks
df['true_peak_after'] = post_peaks

df.to_csv(f'{output_folder}/loudness_results.csv')