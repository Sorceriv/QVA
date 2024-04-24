#Use modules
#DataBuilder ModelBuilder Text Similarity GPT
#Flask CORS API
#React Front-end + TypeScript + Framermotion
#SKLearn and Keras Model Builders
#CHATGPT API
#Text similarity levenshtein python
#Text augmentation - NLPAUG

import pandas as pd
import numpy as np
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

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
    
    def preprocess(self):
        self.df = self.df.dropna()
        self.df = self.df.reset_index(drop=True)
        for header in self.df.columns:
            self.df[header] = self.df[header].astype(str).apply(self.clean_data)
    
    def combineColumns(self, newColumnName, columnNames):
        self.df[newColumnName] = ""
        for columnName in columnNames:
            self.df[newColumnName] += ' ' + self.df[columnName]

    def augmentData(self):
        pass
    
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
            self.labelData = self.df(columnName)
        except:
            print("Invalid column name")

    def getLabel(self):
        try:
            return self.labelData
        except:
            print("Label has not been set. Please set label first using <data>.setLabel('Name of your column')")





def main():
    data = DataBuilder('QVA/src/assets/dataset.xlsx')
    data.preprocess()
    data.combineColumns('Input', ['OS', 'Title', 'QID', 'Port', 'Threat'])
    print(data.df['Input'])

main()