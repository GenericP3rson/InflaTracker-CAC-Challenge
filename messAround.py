import numpy as np
import pandas as pd

class Processing():
    def __init__(self, parent = "Products.csv"):
        self.csv = pd.read_csv(parent).values
    def conversion():
        # print(self.csv[:,1])
        print(self.csv[:, 7].astype(str))

i = Processing()