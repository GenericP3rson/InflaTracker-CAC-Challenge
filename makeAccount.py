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
        self.profileImg = list(self.profileImg)
        self.authenticated = False
        self.user = ""
        # self.numToInfo = [[] num, data for enumerate(zip(self.users, self.names, self.stats)]
        self.userToNum = {user:num for num, user in enumerate(self.users)}
        self.userToPass = {user:pas for user, pas in zip(self.users, self.words)}
        self.ind = 0
    def login(self, user, pas):
        '''
        Given a username and password, tries to find it, then sets all the local variables to the user's data.
        '''
        try:
            if hashing.hashTag(pas) == self.userToPass[user]:
                self.authenticated = True
                self.user = user
                # We forgot to edit self.ind....
                for i in range(len(self.users)):
                    if self.users[i] == user:
                        self.ind = i
                self.theProfileImg = self.profileImg[self.ind]
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
            return False
    def rereadCSV(self, accounts = "Accounts"):
        '''
        It updates the arrays with the data.
        '''
        self.users, self.names, self.words, self.stats, self.profileImg = (pd.read_csv(f"{accounts}.csv").values.T)
        self.users = list(self.users)
        self.names = list(self.names)
        self.words = list(self.words)
        self.stats = list(self.stats)
        self.profileImg = list(self.profileImg)
        # self.statsList = [eval(i) for i in self.stats]
        self.userToNum = {user: num for num, user in enumerate(self.users)}
        self.userToPass = {user:pas for user, pas in zip(self.users, self.words)}

    def addClient(self, user, pas, name="",  stat="[]"):
        '''
        This adds a client to the database, with a username, password, actual name, and any past stats. 
        If the user is already in the database, it will print an error.
        '''
        if user in self.users:
            print("ERROR: PICK ANOTHER NAME")
            return False
        self.user = user
        self.users.append(user)
        self.names.append(name)
        self.words.append(hashing.hashTag(pas))
        self.stats.append(stat)
        self.profileImg.append(F"https://picsum.photos/id/{len(self.user)}/200/300")
        self.theProfileImg = F"https://picsum.photos/id/{len(self.user)}/200/300"
        self.updateCSV()
        self.rereadCSV()
        return True
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
        pd.DataFrame({
            "USERNAMES": self.users,
            "NAMES": self.names,
            "PASSWORDS": self.words,
            "INFO": self.stats,
            "PROFILE_IMG": self.profileImg
        }).to_csv("Accounts.csv", index=False)
