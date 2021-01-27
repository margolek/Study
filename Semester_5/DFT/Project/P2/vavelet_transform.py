import numpy as np
import matplotlib.pyplot as plt
import re
from scipy import signal
from scipy.fftpack import fft, dct,idct
import matplotlib.pyplot as plt
import pywt
import pywt.data


# Load image
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


def vavelet_transform(original):
	# Wavelet transform of image, and plot approximation and details
	titles = ['Approximation', ' Horizontal detail',
	          'Vertical detail', 'Diagonal detail']
	coeffs2 = pywt.dwt2(original, 'bior1.3')
	LL, (LH, HL, HH) = coeffs2
	fig = plt.figure(figsize=(12, 3))
	for i, a in enumerate([LL, LH, HL, HH]):
	    ax = fig.add_subplot(1, 4, i + 1)
	    ax.imshow(a, interpolation="nearest", cmap=plt.cm.gray)
	    ax.set_title(titles[i], fontsize=10)
	    ax.set_xticks([])
	    ax.set_yticks([])

	fig.tight_layout()
	plt.show()

original = read_pgm("lena256.pgm", byteorder='<')
original = np.array(original)
transform = vavelet_transform(original)