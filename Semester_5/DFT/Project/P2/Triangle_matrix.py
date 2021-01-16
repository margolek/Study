import re
import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

dim = 5
coef = np.array([0,1,2,3,4])
M = np.zeros((dim,dim))

rowidx_triu, colidx_triu = np.triu_indices(dim)
rowidx_tril, colidx_tril = np.tril_indices(dim)
print(colidx_triu-rowidx_triu)
print(colidx_tril-rowidx_tril)
# the diagonal offset can be calculated by subtracting the row index from column index
for n in np.arange(0,15):
    M[rowidx_triu, colidx_triu] = coef[(colidx_triu-rowidx_triu)]
for n in np.arange(0,15):
    M[rowidx_tril, colidx_tril] = coef[(rowidx_tril-colidx_tril)]
print(M)