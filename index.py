'''
The Super Cool Thingy
'''

import numpy as np
import pandas as pd
import makeAccount
import http.server
import socketserver, os

PORT = 8000

processedData = "processedData"
try:
    data = pd.read_csv(F"{processedData}.csv").values.T
except:
   # Import our processing code
   import processing
   data = np.array(processing.parsify())
   # Now write it into a new file.
   pd.DataFrame(np.array(data).T).to_csv(f"{processedData}.csv", header=False, index=False)
   print(data.shape)
web_dir = os.path.join(os.path.dirname(__file__), 'ui')
os.chdir(web_dir)
Handler = http.server.SimpleHTTPRequestHandler

class Crohns(makeAccount.CSV):
    def __init__(self, parent="processedData.csv", accounts = "Accounts"):
        self.food = data[0]
        self.ing = data[1]
        self.ingEaten = [] # Key: [[ingName, total # of inflams, total # of times eaten, % of inflams]]
        print(self.food)
        with socketserver.TCPServer(("", PORT), Handler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()
        # self.food is our list to search from. Let's really quickly add this to the UI.


i = Crohns()
