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
    plt.xlim([0,30])
    plt.title("Funkcja autokorelacji")
    output_data = plt.acorr(x, maxlags=30,normed=True)
    auto_coef = output_data[1][30:]
    plt.show()
    return auto_coef


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
            d = np.append(d,int(x[i]-coef*x[i-1]))
    if len(coef) == 2:
        for i in range(2,len(x)):
            d = np.append(d,int(x[i]-coef[0]*x[i-1]-coef[1]*x[i-2]))
    if len(coef) == 3:
        for i in range(3,len(x)):
            d = np.append(d,int(x[i]-coef[0]*x[i-1]-coef[1]*x[i-2]-coef[2]*x[i-3]))
    sum_d = np.sum(d**2)
    Gdpcm = sum_x/sum_d
    return Gdpcm


def quantization(x):

    MSE = np.array([])
    H = np.array([])
    q = np.arange(1,33)
    for i in q:
        xq = i*np.round(x/i)
        MSE = np.append(MSE, np.sum((x-xq)**2)/len(x))   
    PSNR = 10*np.log10(255**2/MSE)
    plt.figure(6)
    plt.grid(True)
    plt.xlabel('Stopień kompresji')
    plt.ylabel('PSNR')
    plt.plot(q,PSNR)
    plt.show()


    

if __name__ == "__main__":
    image = read_pgm("lena256.pgm", byteorder='<')
    image = np.array(image)
    plt.figure(1)
    plt.imshow(image, plt.cm.gray)
    plt.show()

    new_image = image.flatten('F') - np.mean(image.flatten('F'))
    autocorelation = autocorr(new_image)
    dpcm_profit_coef_1 = define_coef(autocorelation,1)
    dpcm_profit_coef_2 = define_coef(autocorelation,2)
    dpcm_profit_coef_3 = define_coef(autocorelation,3)
    dpcm_profit_coef_11 = dpcm_profit_2(dpcm_profit_coef_1, new_image)
    dpcm_profit_coef_22 = dpcm_profit_2(dpcm_profit_coef_2, new_image)
    dpcm_profit_coef_33 = dpcm_profit_2(dpcm_profit_coef_3, new_image)
    img_quant = quantization(new_image)

    


    