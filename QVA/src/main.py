#Use modules - import this as module in main py file
#DataBuilder ModelBuilder Text Similarity GPT
#Flask CORS API
#React Front-end + TypeScript + Framermotion
#SKLearn and Keras Model Builders
#CHATGPT API
#Text similarity levenshtein python
#Text augmentation - NLPAUG
#Save models as pickle files, Load models as APIs which load to GPT

from DataBuilder import *
from ModelBuilder import *

def main():
    #Data
    data = DataBuilder('QVA/src/assets/dataset.xlsx')
    data.replaceNa(['OS', 'Title', 'QID', 'Port', 'Threat'])
    data.preprocess()
    data.combineColumns('Input', ['OS', 'Title', 'QID', 'Port', 'Threat'])
    
    data.dataFrequency('Solution', 10)
    # data.augmentData('Input', 5)
    # print(data.df)

    data.setInput('Input')
    data.setLabel('Solution')

    
    #Model
    model = ModelBuilder(
        "SVM Qualys Model", 
        LinearSVC(), 
        data.getInput(), 
        data.getLabel()
    )
    print("Accuracy: " + str(model.printAccuracy()))
    # print(model.printCm())
    # print(model.printLc())

main()