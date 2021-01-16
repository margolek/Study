import re
import numpy as np
from scipy import signal
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

def create_rxx(coef,array_size):
    rxx = np.empty((array_size,array_size))
    print(rxx)
    n = 0
    diagonal= np.full(array_size-n, coef[n])
    rxx = np.append(rxx,np.diag(diagonal,k=0))
        
    """
    diagonal = np.full(array_size-n, coef[n])
    rxx = np.append(rxx,np.diag(diagonal,k=n))
    rxx = np.append(rxx,np.diag(diagonal,k=-n))
    """
    print(rxx)


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