# Super quick program to just hash Accounts.csv passwords that we just randomly put in.
import pandas as pd
import hashing
newVersion = pd.read_csv("Accounts.csv")
for i in range(len(newVersion)):
    newVersion["PASSWORDS"][i] = hashing.hashTag(newVersion["PASSWORDS"].copy(deep=True)[i])
newVersion.to_csv("Accounts.csv")