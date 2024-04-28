#Use modules - import this as module in main py file
#DataBuilder ModelBuilder Text Similarity GPT
#Save models as pickle files, Load models as APIs which load to GPT
#Flask CORS API
#React Front-end + TypeScript + Framermotion
#SKLearn and Keras Model Builders
#CHATGPT API
#Text similarity levenshtein python
#Text augmentation - NLPAUG


from DataBuilder import *
from ModelBuilder import *

def main():
    # #New Data and  Model
    # #Data
    # data = DataBuilder('QVA/src/assets/dataset.xlsx')
    # data.replaceNa(['OS', 'Title', 'QID', 'Port', 'Threat'])
    # data.preprocess(['OS', 'Title', 'QID', 'Port', 'Threat'])
    # data.combineColumns('Input', ['OS', 'Title', 'QID', 'Port'])

    # data.augmentData('Input', 5)
    # data.dataFrequency('Solution', 10)
    # # data.augmentData('Input', 5)
    # # print(data.df)

    # data.setInput('Input')
    # data.setLabel('Solution')

    
    # #Model - remove input and labels if loading model or add random text or data, maybe separate save and load features from constructor
    # model = ModelBuilder(
    #     "SVM Qualys Model", 
    #     LinearSVC(), 
    #     data.getInput(), 
    #     data.getLabel(),
    #     filePath="C:/Users/eddz9/Desktop/QVA/QVA/QVA/src/models/"
    # )

    #Loaded Model/s
    #With augmented data
    model = ModelBuilder(
        "SVM Qualys Model", 
        LinearSVC(), 
        filePath="C:/Users/eddz9/Desktop/QVA/QVA/QVA/src/models/"
    )


    print("Accuracy: " + str(model.printAccuracy()))
    # print(model.printCm())
    # print(model.printLc())
    predictions = model.predict(["Apache Log4j Denial of Service (DOS) Vulnerability (Log4Shell)"])
    print("Text: " + predictions['text'][0])
    print("Prediction: " + predictions['prediction'][0])
    #Add Text Similarity

    #GPT responses

    #Front-end API

main()