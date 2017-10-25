import numpy as np
import librosa,librosa.display
import os,argparse
import matplotlib.pyplot as plt
from tqdm import tqdm

parser = argparse.ArgumentParser(description='Generate spectograms for a whole folder')

parser.add_argument("-d", "--directory",default='.',
                    help="Directory containing the spectograms",
                    action="store")
parser.add_argument("-t", "--truncate",type=int,
                    help="truncate the signals to a length",
                    action="store", default=7)

def spec(x,base_dir,truncate):
    if os.path.isdir(base_dir+x):
        print(x)
        x = base_dir+x + '/'
        return map(lambda a: spec(a,x,truncate),os.listdir(x))
    elif x[-4:] == '.wav' or x[-4:] == '.mp3':
        a_audio,sr = librosa.load(base_dir+x,sr=22050)
        if truncate != -1:
            a_audio = a_audio[:sr*truncate]
        a_spec = librosa.stft(a_audio,n_fft=2048)

        librosa.display.specshow(librosa.amplitude_to_db(a_spec,ref=np.max))
                              #y_axis='log', x_axis='time')
        plt.xlabel('Time')
        plt.ylabel('Hz')
       
        plt.tight_layout()
        plt.savefig(base_dir+x[:-4] + '.png')  
    else:
        return

if __name__ == "__main__":
    base_dir =  parser.parse_args().directory
    truncate =  parser.parse_args().truncate
    spec(base_dir,'',truncate)