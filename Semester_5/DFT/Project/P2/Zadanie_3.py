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

def create_rxx(coef,array_size):
    """
    Wyznaczyć funkcję autokorelacji sygnału 'lena256.pgm'; i zbudować macierz Rxx
    """
    Rxx = np.zeros((array_size,array_size))
    rowidx_triu, colidx_triu = np.triu_indices(array_size)
    rowidx_tril, colidx_tril = np.tril_indices(array_size)
    for n in np.arange(0,16*array_size):
        Rxx[rowidx_triu, colidx_triu] = coef[(colidx_triu-rowidx_triu)]
    for n in np.arange(0,16*array_size):
        Rxx[rowidx_tril, colidx_tril] = coef[(colidx_tril-rowidx_tril)]
    
    return Rxx

def create_t(Rxx):
    """
    Znaleźć wektory własne i zbudować z nich macierz T korzystając z funkcji eig: [V,D]=eig(Rxx);
    Rxx*V = V*D; T=V’; 
    """
    D,V = np.linalg.eig(Rxx)
    T = V.transpose()
    return T

def find_coef(x,T):
    """
    3)Wyznaczyć współczynniki transformacji sygnału względem T, DCT, FFT
    4)Wyznaczyć GTC dla powyższych transformacji
    W tym punkcie miałem problem z określeniem współczynników transformacji wzgledem T, ponieważ
    nie wiem jak połączyć rozmiar macierzy T (30,30) z rozmiarem sygnału(256**2)
    """
    DCT_coef = dct(x)
    print()
    FFT_coef = fft(x)
    Gtc_dct_den,Gtc_fft_den = 1,1
    Gtc_dct_num = np.sum(np.var(DCT_coef)**2)/len(x)
    Gtc_fft_num = np.sum(np.var(FFT_coef)**2)/len(x)
    for n in np.arange(0,len(x)):
        Gtc_dct_den = Gtc_dct_den*(var(Gtc_dct_coef[n]))
        Gtc_fft_den = Gtc_fft_den*(var(Gtc_fft_coef[n]))
    Gtc_dct_den = (Gtc_dct_den)**(1/len(x))
    Gtc_fft_den = (Gtc_fft_den)**(1/len(x))
    Gtc_dct = Gtc_dct_num/Gtc_dct_num
    Gtc_fft = Gtc_fft_num/Gtc_fft_den
    print('Gtc dla DCT wynosi: {}, natomiast dla FFT: {}'.fomat(Gtc_dct,Gtc_fft))




if __name__ == "__main__":
    image = read_pgm("lena256.pgm", byteorder='<')
    image = np.array(image)
    plt.figure(1)
    plt.imshow(image, plt.cm.gray)
    plt.show()

    new_image = image.flatten('F') - np.mean(image.flatten('F'))

    output_data = plt.acorr(new_image, maxlags=30,normed=True)
    auto_coef = output_data[1][30:]
    Rxx = create_rxx(auto_coef,30)
    T_matrix = create_t(Rxx)
    coef = find_coef(new_image,T_matrix)