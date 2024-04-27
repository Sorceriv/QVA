import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
import nlpaug.augmenter.word as naw

STOPWORDS = set(stopwords.words('english'))
REPLACE_BY_SPACE_RE = re.compile('[/(){}\\[\\]\\|@,;]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')

class DataBuilder:
    def __init__(self, fileName):
        self.df = pd.read_excel(fileName)
    
    def clean_data(self, text):
        text = text.lower()
        text = REPLACE_BY_SPACE_RE.sub(' ', text)
        text = BAD_SYMBOLS_RE.sub('', text)
        text = text.replace('x', '')
        #text = re.sub(r'\W+', '', text)
        text = ' '.join(word for word in text.split() if word not in STOPWORDS)
        return text
    
    def dropNa(self, columnNames):
        self.df.dropna(subset = columnNames, inplace=True)

    def replaceNa(self, columnNames):
        for columnName in columnNames:
            self.df[columnName] = self.df[columnName].fillna('')

    def preprocess(self):
        self.df = self.df.reset_index(drop=True)
        for header in self.df.columns:
            self.df[header] = self.df[header].astype(str).apply(self.clean_data)
    
    def combineColumns(self, newColumnName, columnNames):
        self.df[newColumnName] = ""
        for columnName in columnNames:
            self.df[newColumnName] += ' ' + self.df[columnName]

    def dataFrequency(self, columnName, num):
        #Remove underrepresented data
        threshold = num
        try:
            value_counts = self.df[columnName].value_counts() # Entire DataFrame 
            to_remove = value_counts[value_counts < threshold].index
            self.df[columnName].replace(to_remove, np.nan, inplace=True)
            self.df.dropna(subset = columnName, inplace=True)
            # print(self.df[columnName].value_counts())
        except:
            print("Invalid column name")
        pass

    def augmentData(self, columnName, num):
        aug = naw.SynonymAug()
        for index, row in self.df.iterrows():
            augmentedRows = aug.augment(row[columnName], num)
            for augmentedRow in augmentedRows:
                newRow = row.copy()
                newRow[columnName] = augmentedRow
                self.df = pd.concat([self.df, pd.DataFrame([newRow])], ignore_index=True)
    
    def setInput(self, columnName):
        try:
            self.inputData = self.df[columnName]
        except:
            print("Invalid column name")
    
    def getInput(self):
        try:
            return self.inputData
        except:
            print("Input has not been set. Please set input first using <data>.setInput('Name of your column')")

    def setLabel(self, columnName):
        try:
            self.labelData = self.df[columnName]
        except:
            print("Invalid column name")

    def getLabel(self):
        try:
            return self.labelData
        except:
            print("Label has not been set. Please set label first using <data>.setLabel('Name of your column')")