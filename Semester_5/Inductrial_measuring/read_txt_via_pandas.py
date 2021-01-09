import pandas as pd
import matplotlib.pyplot as plt


result = pd.read_table('data.txt',delim_whitespace=True,
names=['Data1','Data2'])

x = result['Data1']
y = result['Data2']

plt.figure(1)
plt.plot(x,y)
plt.show()