import numpy as np

with open('lena256.pgm', 'r') as infile:
    header = infile.readline()
    width, height, maxval = [int(item) for item in header.split()[1:]]
    image = np.fromfile(infile, dtype=np.uint16).reshape((height, width))