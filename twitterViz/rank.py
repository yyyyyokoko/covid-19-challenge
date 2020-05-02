import os
import pandas as pd

basepath = "covid-19-challenge/csv/"
files = os.listdir(basepath)

def getfilenames(filename):
    #for filename in files:
    temp = filename.split("-")
    date = int(temp[2].split(".")[0])
    if int(temp[1]) == 3:
        if date == 31:
            secondfilename = "2020-04-01.csv"
        else:
            secondfilename = "2020-03-" + str(date+1) + ".csv"
    elif int(temp[1]) == 4:
        if date == 22:
            secondfilename = None
        elif date < 9:
            secondfilename = "2020-04-0" + str(date+1) + ".csv"
        else:
            secondfilename = "2020-04-" + str(date+1) + ".csv"
    return filename, secondfilename

for filename in files:
    first, second = getfilenames(filename)
    firstfile = pd.read_csv(basepath + first)
    if second:
        secondfile = pd.read_csv(basepath + second)
        for word in secondfile.word:
            if word in list(firstfile.word):
                firstindex = firstfile.index[firstfile['word']== word]+1
                secondindex = secondfile.index[secondfile['word']== word]+1
                secondfile.loc[secondfile.word == word, 'change'] = firstindex - secondindex
                secondfile["change"].fillna("New", inplace = True) 
                secondfile.to_csv(second, index = False)