import pandas as pd 
import numpy as np
import hashing

# i = open("accounts.csv")
# keys = np.array([10,4])
# names = np.array(["NAME", "HI"])
# stats = np.array(["INFO", "YES"])

class CSV():
    def __init__(self, accounts = "Accounts"):
        self.users, self.names, self.words, self.stats, self.profileImg = (pd.read_csv(f"{accounts}.csv").values.T)
        self.users = list(self.users)
        self.names = list(self.names)
        self.words = list(self.words)
        # self.statsList = [eval(i) for i in self.stats]
        self.stats = list(self.stats)
        print(self.stats)
        self.authenticated = False
        self.user = ""
        # self.numToInfo = [[] num, data for enumerate(zip(self.users, self.names, self.stats)]
        self.userToNum = {user:num for num, user in enumerate(self.users)}
        self.userToPass = {user:pas for user, pas in zip(self.users, self.words)}
        print(self.userToNum)
        self.ind = 0
    def login(self, user, pas):
        '''
        Given a username and password, tries to find it, then sets all the local variables to the user's data.
        '''
        try:
            if hashing.hashTag(pas) == self.userToPass[user]:
                self.authenticated = True
                self.user = user
                self.ind = self.userToNum[self.user]
                self.userUsername = self.users[self.ind]
                self.userRealName = self.names[self.ind]
                self.userStat = eval(self.stats[self.ind])
                return True
            else:
                print("INVALID CREDENTIALS")
                return False
        except:
            print("INVALID CREDENTIALS")
    def rereadCSV(self, accounts = "Accounts"):
        '''
        It updates the arrays with the data.
        '''
        self.users, self.names, self.words, self.stats = (pd.read_csv(f"{accounts}.csv").values.T)
        self.users = list(self.users)
        self.names = list(self.names)
        self.words = list(self.words)
        self.stats = list(self.stats)
        # self.statsList = [eval(i) for i in self.stats]
        self.userToNum = {user: num for num, user in enumerate(self.users)}
        self.userToPass = {user:pas for user, pas in zip(self.users, self.words)}
        print(self.userToNum)

    def addClient(self, user, pas, name="",  stat="[]"):
        '''
        This adds a client to the database, with a username, password, actual name, and any past stats. 
        If the user is already in the database, it will print an error.
        '''
        if user in self.users:
            print("ERROR: PICK ANOTHER NAME")
            return
        self.users.append(user)
        self.names.append(name)
        self.words.append(hashing.hashTag(pas))
        self.stats.append(stat)
        self.updateCSV()
        self.rereadCSV()
    def editStats(self, newStat):
        if self.authenticated:
            self.stats[self.ind] = newStat
            self.updateCSV()
            self.rereadCSV()
        else:
            print("ERROR: NOT AUTHENTICATED")
    def editName(self, newName):
        if self.authenticated:
            self.names[self.ind] = newName
            self.updateCSV()
            self.rereadCSV()
        else:
            print("ERROR: NOT AUTHENTICATED")
    def editUsername(self, newUName):
        if self.authenticated:
            self.users[self.ind] = newUName
            self.updateCSV()
            self.rereadCSV()
        else:
            print("ERROR: NOT AUTHENTICATED")
    def changePassword(self, oldP, newP):
        if self.authenticated and hashing.hashTag(oldP) == self.words[self.ind]:
            self.words[self.ind] = hashing.hashTag(newP)
            self.updateCSV()
            self.rereadCSV()
        else:
            print("ERROR: NOT AUTHENTICATED")
    def getStats(self):
        if self.authenticated:
            return self.stats[self.ind]
        else: 
            return 0
    def updateCSV(self):
        pd.DataFrame(np.array([self.users, self.names, self.words, self.stats]).T).to_csv(f"Accounts.csv", header=["USERNAMES", "NAMES", "PASSWORDS", "INFO"], index=False)
