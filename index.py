'''
The Super Cool Thingy
'''

import numpy as np
import pandas as pd
processedData = "processedData"
try:
    data = open(F"{processedData}.csv", "r").read()
except:
   # Import our processing code
   import processing
   data = processing.parsify()
   # Now write it into a new file.
   pd.DataFrame(np.array(data).T).to_csv(F"{processedData}.csv", header=False, index=False)
class Crohns():
    def __init__(self, parent = "Food.csv"):
        print(data)
    def findFood(self, food): 
        pass 
i = Crohns()
