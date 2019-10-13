'''
The Super Cool Thingy
'''

import numpy as np
import pandas as pd
import makeAccount
from flask import Flask, render_template, request, send_from_directory, jsonify
app = Flask(__name__,
static_url_path="/static")
processedData = "processedData"
try:
    data = pd.read_csv(F"{processedData}.csv").values.T
except:
   # Excepts every time...
   # Import our processing code
   import processing
   data = processing.parsify()
   # Now write it into a new file.
   pd.DataFrame(np.array(data).T).to_csv(f"{processedData}.csv", header=False, index=False)


class Crohns(makeAccount.CSV):
    def __init__(self, accounts = "Accounts"):
        self.food = data[0]
        self.ing = data[1]
        print(data)
        self.ingEaten = [] # Key: [[ingName, total # of inflams, total # of times eaten, % of inflams]]
        print(data)

        @app.route('/')
        def home():
            return render_template('index.html')
        @app.route('/<string:name>', methods=["GET"])
        def get_javascript_data(name):
            if name == "process":
                return ", ".join(data[0])
        if __name__ == '__main__':
            app.run(debug=True)
    

i = Crohns()
# i.addClient("USERname", "Shreya C", "password", "[]")
# i.login("SHREYA", "name")
# i.filter()
# i.printFa()
