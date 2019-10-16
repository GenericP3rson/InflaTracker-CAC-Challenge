'''
The Super Cool Thingy
'''

import numpy as np
import pandas as pd
import makeAccount, hashing
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
        self.accountInfo = {}
        # Okay, automatically when we start the server the user isn't logged in.
        @app.route('/')
        def _home():
            return render_template('profile.html', logo="static/brandIcon.png", accountInfo=self.accountInfo)
        @app.route('/<string:name>', methods=["GET"])
        def _get_javascript_data(name):
            if name == "process":
                return ", ".join(data[0])
            if(render_template(name)):
                # Remember: ** We have a profile image, which was added in the accounts section. **
                return render_template(name, logo="static/brandIcon.png", accountInfo=self.accountInfo)
            return render_template("404.html")
        @app.route("/<string:name>", methods=["POST"])
        def getData(name):
            # Go through our stuff
            username = request.form.get("accountName")
            attemptedPass = request.form.get("password")
            
            for i in range(len(accountData["USERNAMES"])):
                if accountData["USERNAMES"][i] == username:
                    # Username in database, now check password.
                    userPassed = 1 if accountData['PASSWORDS'][i] == hashing.hashTag(attemptedPass) else 0
                    if userPassed:
                        # The user logged in successfully, now set accountInfo to all our info.
                        self.accountInfo = {
                            "name": accountData["USERNAMES"][i],
                            "info": accountData["INFO"][i],
                            "names": accountData["NAMES"][i]
                        }
                    return str(userPassed)
            return "0"
        if __name__ == '__main__':
            app.run(debug=True)
    

i = Crohns()
# i.addClient("USERname", "Shreya C", "password", "[]")
# i.login("SHREYA", "name")
# i.filter()
# i.printFa()