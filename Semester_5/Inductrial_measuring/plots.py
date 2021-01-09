import matplotlib.pyplot as plt
import numpy as np


filename = 'data.txt'

with open(filename) as file_obj:
	content = file_obj.readlines()


column1 = [i.replace(' ',',') for i in content]
column2 = [i.replace('\n','') for i in column1]
	



