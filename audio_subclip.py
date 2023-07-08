from pydub import AudioSegment
import math
import os

class SplitWavAudioMubin():
    def __init__(self, folder, filename):
        self.folder = folder
        self.filename = filename
        self.filepath = folder + '\\' + filename
        
        self.audio = AudioSegment.from_wav(self.filepath)
    
    def get_duration(self):
        return self.audio.duration_seconds
    
    def single_split(self, from_sec, to_sec, split_filename):
        t1 = from_sec * 1000
        t2 = to_sec * 1000
        split_audio = self.audio[t1:t2]   
        split_audio.export(self.folder + '\\Output\\' + split_filename, format="wav")
        
    def multiple_split(self, sec_per_split):
        total_secs = math.ceil(self.get_duration())
        for i in range(0, total_secs, sec_per_split):
            split_fn = self.filename.split('.')[0] + '_' + str(i) + '_' + str(i+5) + '.wav'
            self.single_split(i, i+sec_per_split, split_fn)
            print(str(i) + ' Done')
            if i == total_secs - sec_per_split:
                print('All splited successfully')

Output_folder = 'Output_1' 
if not os.path.exists(Output_folder):
    os.makedirs(Output_folder)
folder = 'E:\project_updating\split_file'
file = 'Raw.wav'
split_wav = SplitWavAudioMubin(folder, file)
split_wav.multiple_split(sec_per_split= 5)