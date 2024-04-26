#Use modules - import this as module in main py file
#DataBuilder ModelBuilder Text Similarity GPT
#Flask CORS API
#React Front-end + TypeScript + Framermotion
#SKLearn and Keras Model Builders
#CHATGPT API
#Text similarity levenshtein python
#Text augmentation - NLPAUG

from DataBuilder import *
from ModelBuilder import *

def main():
    #Data
    data = DataBuilder('QVA/src/assets/dataset.xlsx')
    data.replaceNa(['OS', 'Title', 'QID', 'Port', 'Threat'])
    data.preprocess()
    data.combineColumns('Input', ['OS', 'Title', 'QID', 'Port', 'Threat'])
    # data.augmentData('Input', 5)
    data.setInput('Input')
    data.setLabel('Solution')
    
    #Model
    model = ModelBuilder(LinearSVC(), data.getInput(), data.getLabel())
    print(model.printAccuracy())

main()