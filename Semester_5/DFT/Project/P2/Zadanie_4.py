import re
import numpy as np
from scipy import signal
from scipy.fftpack import fft, dct,idct
import matplotlib.pyplot as plt
"""
Ze względu na ograniczenie upla do przesyłania 2 plików, sprawozdanie z zadań 1 oraz 2
umieściłem w miejscu sprawozdania poprzedniego
"""

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
    windowsize_r = 8
    windowsize_c = 8
    window = np.array([])
    blocks = []
    new_blocks = []
    my_dict = {}
    new_dict = {}
    count = 0
    for r in range(0,x.shape[0], windowsize_r):
        for c in range(0,x.shape[1], windowsize_c):
            window = x[r:r+windowsize_r,c:c+windowsize_c]
            window = dct(window,axis=1)
            window_quan = 32*np.round(window/32)
            new_window = idct(window)
            count = count + np.count_nonzero(window) #Rekwantyzacja uzyskanych współczynników dla stopnia kwantyzacji q = 32
            blocks.append(window)
            new_blocks.append(new_window)
    MSE = np.sum(((window-window_quan)**2)/len(x))
    PSNR = 10*np.log10(255**2/MSE)
    print('Wartość współczynnika PSNR wynosi: {0:0.2f}'.format(PSNR))
    print('Procent współczynników niezerowych dla transformaci DCT wzdłuż wierszy wynowi: {0:0.2f}%'.format(count/(256**2)*100))
    blocks = np.asarray(blocks)
    new_blocks = np.asarray(new_blocks)
    for n in range(0,1024,32):
        my_dict["blocks{0}".format(n/32)] = np.concatenate((blocks[n:n+32]),axis=1)
        new_dict["new_blocks{0}".format(n/32)] = np.concatenate((new_blocks[n:n+32]),axis=1)
    """
    Nie wiedziałem w taki sposób połączyć bloki uzywając słownika, ponieważ tutaj
    nie można wykonywać operacji 'slice' jak w przypadku listy
    """
    blocks1 = np.concatenate((my_dict['blocks0.0'],my_dict['blocks1.0'],my_dict['blocks2.0'],
                            my_dict['blocks3.0'],my_dict['blocks4.0'],my_dict['blocks5.0'],
                            my_dict['blocks6.0'],my_dict['blocks7.0'],my_dict['blocks8.0'],
                            my_dict['blocks9.0'],my_dict['blocks10.0'],my_dict['blocks11.0'],
                            my_dict['blocks12.0'],my_dict['blocks13.0'],my_dict['blocks14.0'],
                            my_dict['blocks15.0'],my_dict['blocks16.0'],my_dict['blocks17.0'],
                            my_dict['blocks18.0'],my_dict['blocks19.0'],my_dict['blocks20.0'],
                            my_dict['blocks21.0'],my_dict['blocks22.0'],my_dict['blocks23.0'],
                            my_dict['blocks24.0'],my_dict['blocks25.0'],my_dict['blocks26.0'],
                            my_dict['blocks27.0'],my_dict['blocks28.0'],my_dict['blocks29.0'],
                            my_dict['blocks30.0'],my_dict['blocks31.0']),axis=0)

    new_blocks1 = np.concatenate((new_dict['new_blocks0.0'],new_dict['new_blocks1.0'],new_dict['new_blocks2.0'],
                            new_dict['new_blocks3.0'],new_dict['new_blocks4.0'],new_dict['new_blocks5.0'],
                            new_dict['new_blocks6.0'],new_dict['new_blocks7.0'],new_dict['new_blocks8.0'],
                            new_dict['new_blocks9.0'],new_dict['new_blocks10.0'],new_dict['new_blocks11.0'],
                            new_dict['new_blocks12.0'],new_dict['new_blocks13.0'],new_dict['new_blocks14.0'],
                            new_dict['new_blocks15.0'],new_dict['new_blocks16.0'],new_dict['new_blocks17.0'],
                            new_dict['new_blocks18.0'],new_dict['new_blocks19.0'],new_dict['new_blocks20.0'],
                            new_dict['new_blocks21.0'],new_dict['new_blocks22.0'],new_dict['new_blocks23.0'],
                            new_dict['new_blocks24.0'],new_dict['new_blocks25.0'],new_dict['new_blocks26.0'],
                            new_dict['new_blocks27.0'],new_dict['new_blocks28.0'],new_dict['new_blocks29.0'],
                            new_dict['new_blocks30.0'],new_dict['new_blocks31.0']),axis=0)
    plt.figure(1)
    plt.title('Wynik transformacji wzdłuż wierszy')
    plt.imshow(blocks1,plt.cm.gray)
    plt.show()
    plt.figure(2)
    plt.title('Sygnał po rekonstrukcji w wyniku transfomacji DCT wzdłuż wierszy')
    plt.imshow(new_blocks1,plt.cm.gray)
    plt.show()


    window = np.array([])
    blocks = []
    my_dict = {}
    count = 0
    for r in range(0,x.shape[0], windowsize_r):
        for c in range(0,x.shape[1], windowsize_c):
            window = x[r:r+windowsize_r,c:c+windowsize_c]
            window = dct(window,axis=1)
            window = dct(window,axis=0)
            count = count + np.count_nonzero(window) #Rekwantyzacja uzyskanych współczynników dla stopnia kwantyzacji q = 32
            blocks.append(window)
    print('Procent współczynników niezerowych dla transformaci DCT wzdłuż wierszy i kolumn wynowi: {0:0.2f}%'.format(count/(256**2)*100))
    blocks = np.asarray(blocks)
    for n in range(0,1024,32):
        my_dict["blocks{0}".format(n/32)] = np.concatenate((blocks[n:n+32]),axis=1)
        new_dict["new_blocks{0}".format(n/32)] = np.concatenate((new_blocks[n:n+32]),axis=1)
    blocks1 = np.concatenate((my_dict['blocks0.0'],my_dict['blocks1.0'],my_dict['blocks2.0'],
                            my_dict['blocks3.0'],my_dict['blocks4.0'],my_dict['blocks5.0'],
                            my_dict['blocks6.0'],my_dict['blocks7.0'],my_dict['blocks8.0'],
                            my_dict['blocks9.0'],my_dict['blocks10.0'],my_dict['blocks11.0'],
                            my_dict['blocks12.0'],my_dict['blocks13.0'],my_dict['blocks14.0'],
                            my_dict['blocks15.0'],my_dict['blocks16.0'],my_dict['blocks17.0'],
                            my_dict['blocks18.0'],my_dict['blocks19.0'],my_dict['blocks20.0'],
                            my_dict['blocks21.0'],my_dict['blocks22.0'],my_dict['blocks23.0'],
                            my_dict['blocks24.0'],my_dict['blocks25.0'],my_dict['blocks26.0'],
                            my_dict['blocks27.0'],my_dict['blocks28.0'],my_dict['blocks29.0'],
                            my_dict['blocks30.0'],my_dict['blocks31.0']),axis=0)


    plt.figure(3)
    plt.title('Wynik transformacji DCT po wierszach i po kolumnach')
    plt.imshow(blocks1,plt.cm.gray)
    plt.show()
  
if __name__ == "__main__":
    image = read_pgm("lena256.pgm", byteorder='<')
    image = np.array(image)
    plt.figure(1)
    plt.imshow(image, plt.cm.gray)
    plt.show()
    divide = create_blocks(image)
