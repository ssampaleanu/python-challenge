# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 13:47:51 2018

@author: Stef
"""

import pandas as pd
import numpy as np

election = input("Which election would you like to review? (1 or 2) ")
if election == str("1"):
    elecData = "election_data_1.csv"
elif election == str("2"):
    elecData = "election_data_2.csv"
else:
    print("Value not found. Please enter a valid number.")
    
elec_df = pd.read_csv(elecData)

elecSumm = pd.DataFrame(elec_df["Candidate"].value_counts())
numVoters = elec_df["Candidate"].count()
elecSumm["% of vote"] = (elecSumm["Candidate"]/numVoters * 100)
elecSumm.rename(columns = {"Candidate":"Vote Count"})

elecSumm = elecSumm.sort_values("% of vote",ascending=False)
elecSumm["Name"] = elecSumm.index
winner = elecSumm.iloc[0,2]


print("Election Results")
print("-------------------------")
print("Total Votes: " + str(numVoters))
print("-------------------------")
for index, row in elecSumm.iterrows():
    print(str(row["Name"]) + ": " + str(row["% of vote"]) + "% (" + str(row["Candidate"]) + " votes)")
print("-------------------------")
print("Winner: " + str(winner))
print("-------------------------")

