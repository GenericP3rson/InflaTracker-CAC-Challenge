'''
The Super Cool Thingy
'''

import numpy as np
import pandas as pd
import makeAccount
from flask import Flask, render_template, send_from_directory, jsonify, request
app = Flask(__name__,
static_url_path="/static")
processedData = "processedData"
accountData = pd.read_csv("Accounts.csv")
try:
    data = pd.read_csv(F"{processedData}.csv").values.T
except:
   # Excepts every time...
   # Import our processing code
   import processing
   data = processing.parsify()
   # Now write it into a new file.
   pd.DataFrame(np.array(data).T).to_csv(f"{processedData}.csv", header=False, index=False)


class Crohns():
    def __init__(self, accounts = "Accounts"):
        self.food = data[0]
        self.ing = data[1]
        self.ingEaten = [] # Key: [[ingName, total # of inflams, total # of times eaten, % of inflams]]

        @app.route('/')
        def _home():
            return render_template('search.html')
        @app.route('/<string:name>', methods=["GET"])
        def _get_javascript_data(name):
            if name == "process":
                return ", ".join(data[0])
            if(render_template(name)):
                # We need to send some account stats with us.
                # For now... This'll be kinda insecure.
                return render_template(name, logo="static/brandIcon.png")
                '''
                , accountInfo={
                    "name": "Sarah",
                    "work": "Please?",
                    "profileImg": "https://cdn1.iconfinder.com/data/icons/avatar-1-2/512/User2-512.png"
                }
                '''
            return render_template("404.html")
        @app.route("/<string:name>", methods=["POST"])
        def getData(name):
            # Go through our stuff
            username = request.form.get("accountName")
            attemptedPass = request.form.get("password")
            
            for i in range(len(accountData["USERNAMES"])):
                if accountData["USERNAMES"][i] == username:
                    # Username in database, now check password.
                    return F"{1 if accountData['PASSWORDS'][i] == attemptedPass else 0}"
            return "0"
        if __name__ == '__main__':
            app.run(debug=True)
    

i = Crohns()
# i.addClient("USERname", "Shreya C", "password", "[]")
# i.login("SHREYA", "name")
# i.filter()
# i.printFa()