'''
The Super Cool Thingy
'''

import numpy as np
import pandas as pd
import makeAccount1 as makeAccount
import hashing, os
import matplotlib.pyplot as plt
from flask import Flask, render_template, send_from_directory, jsonify, request
from sklearn.cluster import KMeans as KM
app = Flask(__name__,
static_url_path="/static")
processedData = "processedData"
accountData = pd.read_csv("Accounts.csv")
NAME = "inflaTracker.png"
try:
    data = pd.read_csv(F"{processedData}.csv").values.T
except:
   # Excepts every time...
   # Import our processing code
   import processing
   data = processing.parsify()
   # Now write it into a new file.
   pd.DataFrame(np.array(data).T).to_csv(f"{processedData}.csv", header=False, index=False)

user = makeAccount.CSV()
class Crohns(makeAccount.CSV):
    def loginAndEnter(self, user, word):
        self.login(user, word)
        print(self.getStats())
        self.stuff = eval(self.getStats())
        # print([[x, y-x] for _, x, y, _ in stuff[0]])
        self.allCoord = np.array([np.array([x, y-x]) for j in self.stuff for _, x, y, _ in j])
    def printPoints(self):
        x = [x for j in self.stuff for _, x, y, _ in j]
        y = [y-x for j in self.stuff for _, x, y, _ in j]
        self.labels = [label for j in self.stuff for label, _, _, _ in j]
        if len(self.allCoord) == 0:
            plt.text(0, 0, "Make Sure To Eat First!", color="red", fontsize=15)
            plt.savefig("static/" + NAME)
            self.src = NAME
            return 0
        # print(ratio)
        plt.ylabel("NO REACTION")
        plt.xlabel("REACTION")
        plt.yticks(np.arange(0, max(self.allCoord[:, 0]) + 10, 1))
        plt.xticks(np.arange(0, max(self.allCoord[:, 1]) + 10, 1))
        # plt.scatter(np.array(x), np.array(y))
        # plt.scatter(self.allCoord[:, 0], self.allCoord[:, 1])
        # for i, txt in enumerate(self.labels):
        #     # plt.annotate(txt, (x[i], y[i]))
        #     plt.annotate(txt, (self.allCoord[i][0], self.allCoord[i][1]))
        # plt.show()
        return 1
    def KMeans(self):
        return1 = self.printPoints()  
        if not return1:
            return
        algorithm = KM(n_clusters=2)
        categories = algorithm.fit_predict(self.allCoord)
        print(self.stuff, categories)
        plt.scatter(self.allCoord[categories == 0, 0], self.allCoord[categories == 0, 1], c= "green")
        plt.scatter(self.allCoord[categories == 1, 0],self.allCoord[categories == 1, 1], c="red")
        plt.scatter(algorithm.cluster_centers_[:, 0], algorithm.cluster_centers_[:, 1], c= "black", marker="*")
        for i, txt in enumerate(self.labels):
            plt.annotate(txt, (self.allCoord[i][0], self.allCoord[i][1]))
        plt.annotate("NO INFLAMMATION", algorithm.cluster_centers_[0])
        plt.annotate("CAUSES INFLAMMATION", algorithm.cluster_centers_[1])
        plt.savefig("static/" + NAME)
        self.src = NAME

    def __init__(self, accounts = "Accounts"):
        super()
        super().__init__(accounts)
        self.food = data[0]
        self.ing = data[1]
        self.ingEaten = [] # Key: [[ingName, total # of inflams, total # of times eaten, % of inflams]]
        self.accountInfo = ""
        self.src = ""
        # Okay, automatically when we start the server the user isn't logged in.
        @app.route('/')
        def _home():
            return render_template('profile.html', logo="static/brandIcon.png", accountInfo={
                    "user": self.user
                })
        @app.route('/<string:name>', methods=["GET"])
        def _get_javascript_data(name):
            if name == "process":
                return ", ".join(data[0])
            if(render_template(name)):
                # Remember: ** We have a profile image, which was added in the accounts section. **
                if self.user != "":
                    self.KMeans()
                print("HEy", self.src)
                return render_template(name, logo="static/brandIcon.png", accountInfo={
                    "user": self.user
                }, src=self.src)
            return render_template("404.html")
        @app.route("/ingredients/<string:name>", methods=["GET"])
        def _get_ingredients(name):
            print(self.foodData)
            return
        @app.route("/signUp", methods=["POST"])
        def _():
            username = request.form.get("accountName")
            passName = request.form.get("password")
            successful = self.addClient(username, passName)
            if successful:
                self.loginAndEnter(username, passName)
            return "1" if successful else "0"
        @app.route("/<string:name>", methods=["POST"])
        def _getData(name):
            # Go through our stuff
            username = request.form.get("accountName")
            attemptedPass = request.form.get("password")
            ans = "1" if self.login(username, attemptedPass) else "0"
            if ans == "1":
                self.loginAndEnter(username, attemptedPass)
            return ans
        if __name__ == '__main__':
            app.run(debug=False)


i = Crohns()
# i.addClient("USERname", "Shreya C", "password", "[]")
# i.login("SHREYA", "name")
# i.filter()
# i.printFa()