import re
import numpy as np
import matplotlib.pyplot as plt
def read_pgm(filename, byteorder='>'):
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

def autocorr(x):
    plt.figure(2)
    plt.grid(True)
    plt.title("Funkcja autokorelacji")
    output_data = plt.acorr(x, maxlags=30,normed=True)
    auto_coef = output_data[1][30:]
    plt.show()
    return auto_coef
def variance(x):
    return 'Wariancja sygnału wynosi: {0:4e}'.format(np.var(x))

def variance_diff(x):
    return 'Wariancja różnic próbek sygnału wynosi: {0:2e}'.format(np.var(np.diff(x,n=1)))

def dpcm_profit(x):
    d = np.array([])
    sum_x = np.sum(x**2)
    for i in range(1,len(x)):
        d = np.append(d,x[i]-x[i-1])
    sum_d = np.sum(d**2)
    Gdpcm = sum_x/sum_d
    return 'Zysk z kodowania DPCM wynosi: {0:0.3f}'.format(Gdpcm)

def dpcm_profit_with_coef(x,auto):
    a = np.array([[auto[0],auto[1],auto[2]], [auto[1],auto[0],auto[1]],[auto[2],auto[3],auto[0]]])
    b = np.array([[auto[1]],[auto[2]],[auto[3]]])
    return np.linalg.solve(a,b)


if __name__ == "__main__":
    image = read_pgm("lena256.pgm", byteorder='<')
    image = np.array(image)
    print(image)
    plt.figure(1)
    plt.imshow(image, plt.cm.gray)
    plt.show()
    new_image = image.flatten() - np.mean(image.flatten())
    autocorelation = autocorr(new_image)
    variance = variance(new_image)
    print(variance)
    variance_diff = variance_diff(new_image)
    print(variance_diff)
    dpcm_profit = dpcm_profit(new_image)
    print(dpcm_profit)
    dpcm_profit = dpcm_profit_with_coef(new_image,autocorelation)
    print(dpcm_profit)


    