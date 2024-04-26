from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer

class ModelBuilder():
    def __init__(self, modelType, features, labels):
        self.features = features
        self.labels = labels

        self.model = make_pipeline(CountVectorizer(), modelType)
        self.train_data, self.test_data, self.train_labels, self.test_labels = train_test_split(self.features, self.labels, test_size=0.2, random_state=42)
        self.model_fit = self.model.fit(self.train_data, self.train_labels)
        self.model_predictions = self.model_fit.predict(self.test_data)

    def printAccuracy(self):
        self.accuracy = metrics.accuracy_score(self.test_labels, self.model_predictions)
        return self.accuracy

