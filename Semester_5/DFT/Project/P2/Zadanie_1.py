import re
import numpy as np
import matplotlib.pyplot as plt
def read_pgm(filename, byteorder='>'):
    """Wczytanie pliku przy uzyciu wyrażeń refularnych"""
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
    plt.xlim([0,30])
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

def define_coef(auto,number_of_coef):
    if number_of_coef == 1:
        a = auto[0]
        b = auto[1]
        return b/a
    elif number_of_coef == 2:
        a = np.array([[auto[0],auto[1]],[auto[1],auto[0]]])
        b = np.array([[auto[1]],[auto[2]]])
        return np.linalg.solve(a, b)
    elif number_of_coef == 3:
        a = np.array([[auto[0],auto[1],auto[2]], [auto[1],auto[0],auto[1]],[auto[2],auto[1],auto[0]]])
        b = np.array([[auto[1]],[auto[2]],[auto[3]]])
        return np.linalg.solve(a,b)

def dpcm_profit_2(coef,x):
    coef = coef.flatten()
    d = np.array([])
    sum_x = np.sum(x**2)
    if len(coef) == 1:
        for i in range(1,len(x)):
            d = np.append(d,x[i]-coef*x[i-1])
    if len(coef) == 2:
        for i in range(1,len(x)):
            d = np.append(d,x[i]-coef[0]*x[i-1]-coef[1]*x[i-2])
    if len(coef) == 3:
        for i in range(1,len(x)):
            d = np.append(d,x[i]-coef[0]*x[i-1]-coef[1]*x[i-2]-coef[2]*x[i-3])
    sum_d = np.sum(d**2)
    Gdpcm = sum_x/sum_d
    return Gdpcm

def plot_profit(y1,y2,y3):
    plt.figure(3)
    plt.grid(True)
    plt.title('Zysk prezykcji - bez kwantyzacji')
    plt.xlabel('Liczba współczynników predykcji')
    x = [1,2,3]
    plt.xlim([0,5])
    plt.stem(x,[y1,y2,y3])
    plt.show()

def quantization(x):
    """
    W tym punkcie nie zgadza mi się wartość entropi, która
    przybiera wartości niemotoniczne i nie mogę się zorientować
    co może być tego problemem. Otrzymany historam również mi się
    niestety nie pokrywa.
    """

    MSE = np.array([])
    H = np.array([])
    q = np.arange(1,33)
    for i in q:
        xq = i*np.round(x/i)
        MSE = np.append(MSE, np.sum((x-xq)**2)/len(x))
        d = np.array([])     
        for i in np.arange(1,len(x)):
            d = np.append(d,xq[i]-xq[i-1])
        a = np.histogram(d)
        #probability = a[1]
        #/(np.sum(a[1]))
        #H =  np.append(H,-np.sum(probability * np.log2(probability)))

    PSNR = 10*np.log10(255**2/MSE)
    plt.figure(6)
    plt.grid(True)
    plt.xlabel('Stopień kwantyzacji')
    plt.ylabel('PSNR')
    plt.plot(q,PSNR)
    plt.show()

    #plt.figure(7)
   # plt.grid(True)
    #plt.xlabel('Stopień kwantyzacji')
   # plt.ylabel('Entropia')
    #plt.plot(q,H)
   # plt.show()

    

if __name__ == "__main__":
    image = read_pgm("lena256.pgm", byteorder='<')
    image = np.array(image)
    plt.figure(1)
    plt.imshow(image, plt.cm.gray)
    plt.show()

    new_image = image.flatten('F') - np.mean(image.flatten('F'))

    autocorelation = autocorr(new_image)

    variance = variance(new_image)
    print(variance)

    variance_diff = variance_diff(new_image)
    print(variance_diff)

    dpcm_profit = dpcm_profit(new_image) 
    print(dpcm_profit)

    dpcm_profit_coef_1 = define_coef(autocorelation,1)
    print('W przypadku 1 współczynnika otrzymujemy:{}'.format(dpcm_profit_coef_1))
    dpcm_profit_coef_2 = define_coef(autocorelation,2)
    print('W przypadku 2 współczynników otrzymujemy:{}'.format(dpcm_profit_coef_2))
    dpcm_profit_coef_3 = define_coef(autocorelation,3)
    print('W przypadku 3 współczynników otrzymujemy:{}'.format(dpcm_profit_coef_3))
    
    dpcm_profit_coef_11 = dpcm_profit_2(dpcm_profit_coef_1, new_image)
    print('W przypadku 1 współczynnika otrzymujemy: G={}'.format(dpcm_profit_coef_11))
    dpcm_profit_coef_22 = dpcm_profit_2(dpcm_profit_coef_2, new_image)
    print('W przypadku 2 współczynników otrzymujemy: G={}'.format(dpcm_profit_coef_22))
    dpcm_profit_coef_33 = dpcm_profit_2(dpcm_profit_coef_3, new_image)
    print('W przypadku 3 współczynników otrzymujemy: G={}'.format(dpcm_profit_coef_33))

    plot_profit = plot_profit(dpcm_profit_coef_11,dpcm_profit_coef_22,dpcm_profit_coef_33)

    img_quant = quantization(new_image)
    


    