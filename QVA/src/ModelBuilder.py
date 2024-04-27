from sklearn.svm import LinearSVC
from sklearn.pipeline import make_pipeline
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import learning_curve
import matplotlib.pyplot as plt
import seaborn as sns

class ModelBuilder():
    def __init__(self, modelName, modelType, features, labels):
        self.modelName = modelName
        self.features = features
        self.labels = labels

        self.model = make_pipeline(CountVectorizer(), modelType)
        self.train_data, self.test_data, self.train_labels, self.test_labels = train_test_split(self.features, self.labels, test_size=0.2, random_state=42)
        self.model_fit = self.model.fit(self.train_data, self.train_labels)
        self.model_predictions = self.model_fit.predict(self.test_data)

    def printAccuracy(self):
        self.accuracy = metrics.accuracy_score(self.test_labels, self.model_predictions)
        return self.accuracy
    
    def classificationReport(self):
        return metrics.classification_report(self.test_labels, self.model_predictions)
    
    def printCm(self):
        sns.set(font_scale=0.5) 
        m_cm = metrics.confusion_matrix(self.test_labels, self.model_predictions)
        plt.figure(figsize=(8, 8))
        sns.heatmap(m_cm, annot=True, fmt='d', cmap='Blues', xticklabels=self.model.classes_, yticklabels=self.model.classes_)
        plt.title(self.modelName + ' Confusion Matrix')
        plt.xlabel('Predicted')
        plt.ylabel('Actual')
        plt.show()

    def printLc(self):
        train_sizes, train_scores, test_scores = learning_curve(
            self.model, self.train_data, self.train_labels, cv=5, scoring='accuracy', train_sizes=np.linspace(0.1, 1.0, 10)
        )
        train_mean = np.mean(train_scores, axis=1)
        train_std = np.std(train_scores, axis=1)
        test_mean = np.mean(test_scores, axis=1)
        test_std = np.std(test_scores, axis=1)

        plt.figure(figsize=(10, 6))
        plt.plot(train_sizes, train_mean, color='blue', marker='o', markersize=5, label='Training Accuracy')
        plt.fill_between(train_sizes, train_mean - train_std, train_mean + train_std, alpha=0.15, color='blue')
        plt.plot(train_sizes, test_mean, color='green', linestyle='--', marker='s', markersize=5, label='Validation Accuracy')
        plt.fill_between(train_sizes, test_mean - test_std, test_mean + test_std, alpha=0.15, color='green')

        plt.title(self.modelName + ' Learning Curve')
        plt.xlabel('Training Examples')
        plt.ylabel('Accuracy')
        plt.legend(loc='lower right')
        plt.grid()
        plt.show()
        

