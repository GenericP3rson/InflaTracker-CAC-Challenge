'''
The Super Cool Thingy
'''

import numpy as np
import pandas as pd

class Processing():
    def __init__(self, parent = "Products.csv"):
        self.csv = pd.read_csv(parent, dtype=str).values
        # self.csv = np.array(self.csv[:,1] + self.csv[:,-1])
        # print(self.csv[:,1], self.csv[:,-1])
        print(type(self.csv[:,0][1]), type(self.csv[:,-1][1]))
class Crohns():
    def __init__(self, parent = "Products.csv"):
        process = Processing()
        pass
    def findFood(self, food): 
        pass 
i = Crohns()
