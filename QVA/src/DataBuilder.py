import pandas as pd
import numpy as np

class DataBuilder:
    def __init__(self, fileName):
        self.df = pd.read_excel(fileName)
    
    def preprocess(self):
        self.df = self.df.dropna()

def main():
    data = DataBuilder('QVA/src/assets/dataset.xlsx')
    data.preprocess()
    print(data.df)

main()