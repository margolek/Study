import re
import numpy as np
from scipy import signal
from scipy.fftpack import fft, dct
import matplotlib.pyplot as plt


def read_pgm(filename, byteorder='>'):
    """
    Wczytanie pliku przy użyciu wyrażeń regularnych
    """
    with open(filename, 'rb') as f:
        buffer = f.read()
    try:
        header, width, height, maxval = re.search(
            b"(^P5\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n])*"
            b"(\d+)\s(?:\s*#.*[\r\n]\s)*)", buffer).groups()
    except AttributeError:
        raise ValueError("Not a raw PGM file: '%s'" % filename)
    return np.frombuffer(buffer,
                            dtype='u1' if int(maxval) < 256 else byteorder+'u2',
                            count=int(width)*int(height),
                            offset=len(header)
                            ).reshape((int(height), int(width)))

def create_blocks(x):
    print(x)
    windowsize_r = 8
    windowsize_c = 8
    window = np.array([])
    blocks = []
    for r in range(0,x.shape[0], windowsize_r):
        for c in range(0,x.shape[1], windowsize_c):
            window = x[r:r+windowsize_r,c:c+windowsize_c]
            window = dct(window,axis=1)
            blocks.append(window)
    blocks = np.asarray(blocks)
    for n in range(0,33):
        blocks1 = np.concatenate((blocks[0],blocks[1],blocks[2],blocks[3],blocks[4],blocks[5]),axis=1)     
    plt.figure(1)
    plt.imshow(blocks1,plt.cm.gray)
    plt.show()
    for r in range(0,x.shape[0], windowsize_r):
        for c in range(0,x.shape[1], windowsize_c):
            window = x[r:r+windowsize_r,c:c+windowsize_c]
            window = dct(window,axis=1)
            window = dct(window,axis=0)
    plt.figure(2)
    plt.imshow(window,plt.cm.gray)
    plt.show()
if __name__ == "__main__":
    image = read_pgm("lena256.pgm", byteorder='<')
    image = np.array(image)
    plt.figure(1)
    plt.imshow(image, plt.cm.gray)
    plt.show()
    divide = create_blocks(image)
