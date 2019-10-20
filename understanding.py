'''
The Super Cool Thingy
'''

import numpy as np
import pandas as pd
import makeAccount, hashing
import matplotlib.pyplot as plt
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

user = makeAccount.CSV()
class Crohns():
    def __init__(self, accounts = "Accounts"):
        self.food = data[0]
        self.ing = data[1]
        self.ingEaten = [] # Key: [[ingName, total # of inflams, total # of times eaten, % of inflams]]
        self.accountInfo = user
        # Okay, automatically when we start the server the user isn't logged in.
        @app.route('/')
        def _home():
            return render_template('profile.html', logo="static/brandIcon.png", accountInfo=user)
        @app.route('/<string:name>', methods=["GET"])
        def _get_javascript_data(name):
            if name == "process":
                return ", ".join(data[0])
            if(render_template(name)):
                # Remember: ** We have a profile image, which was added in the accounts section. **
                return render_template(name, logo="static/brandIcon.png", accountInfo=user)
            return render_template("404.html")
        @app.route("/signUp", methods=["POST"])
        def _():
            username = request.form.get("accountName")
            passName = request.form.get("password")
            successful = user.addClient(username, passName)
            self.accountInfo = user
            return "1" if successful else "0"
        @app.route("/<string:name>", methods=["POST"])
        def _getData(name):
            # Go through our stuff
            username = request.form.get("accountName")
            attemptedPass = request.form.get("password")
            ans = "1" if user.login(username, attemptedPass) else "0"
            self.accountInfo = user
            print(user.theProfileImg)
            return ans
        if __name__ == '__main__':
            app.run(debug=True)
    
class Clusters(makeAccount.CSV):
    def __init__(self, accounts = "Accounts"):
        super()
        super().__init__(accounts)
        # print("UNDER HERE")
        # print(eval(i.getStats()))
        # print(self.allCoord)
    def loginAndEnter(self, user, word):
        self.login(user, word)
        self.stuff = eval(self.getStats())
        # print([[x, y-x] for _, x, y, _ in stuff[0]])
        self.allCoord = np.array([np.array([x, y-x]) for j in self.stuff for _, x, y, _ in j])
    def printPoints(self):
        x = [x for j in self.stuff for _, x, y, _ in j]
        y = [y-x for j in self.stuff for _, x, y, _ in j]
        self.labels = [label for j in self.stuff for label, _, _, _ in j]
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
    def KMeans(self):
        from sklearn.cluster import KMeans as KM
        algorithm = KM(n_clusters=2)
        categories = algorithm.fit_predict(self.allCoord)
        # plt.scatter(self.allCoord[categories == 0, 0], self.allCoord[categories == 0, 1], c= "green")
        # plt.scatter(self.allCoord[categories == 1, 0],self.allCoord[categories == 1, 1], c="red")
        # plt.scatter(algorithm.cluster_centers_[:, 0], algorithm.cluster_centers_[:, 1], c= "black", marker="*")
        for i, txt in enumerate(self.labels):
            plt.annotate(txt, (self.allCoord[i][0], self.allCoord[i][1]))
        plt.annotate("NO INFLAMMATION", algorithm.cluster_centers_[0])
        plt.annotate("CAUSES INFLAMMATION", algorithm.cluster_centers_[1])
        # plt.show()


i = Clusters()
i.loginAndEnter("SHREYA", "name")
i.printPoints()
i.KMeans()
i = Crohns()
# i.addClient("USERname", "Shreya C", "password", "[]")
# i.login("SHREYA", "name")
# i.filter()
# i.printFa()