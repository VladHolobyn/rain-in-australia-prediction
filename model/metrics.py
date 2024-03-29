import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

class Metrics:
    def accuracy(conf_m):
        return (conf_m.TP + conf_m.TN) / (conf_m.TP + conf_m.TN + conf_m.FP + conf_m.FN)
    
    def precission(conf_m):
        return {
            0: (conf_m.TN)/(conf_m.TN+conf_m.FN), 
            1: (conf_m.TP)/(conf_m.TP+conf_m.FP)
        }
    
    def recall(conf_m):
        return {
            0: (conf_m.TN)/(conf_m.TN+conf_m.FP), 
            1: (conf_m.TP)/(conf_m.TP+conf_m.FN)
        }
    
    def f1(conf_m):
        precission = Metrics.precission(conf_m)
        recall = Metrics.recall(conf_m)
        
        return {
            0: (2* precission[0] * recall[0])/(precission[0] + recall[0]), 
            1: (2* precission[1] * recall[1])/(precission[1] + recall[1])
        }
    
    def tpr(conf_m):
        return Metrics.recall(conf_m)[1]
    
    def fpr(conf_m):
        return conf_m.FP/(conf_m.TN + conf_m.FP)

    def roc(y_true, y_prob, step = 0.05):
        threshold = 0
        fpr = []
        tpr = []

        while threshold <= 1:
            class_pred = [0 if y<= threshold else 1 for y in y_prob]
            conf_m = ConfusionMatrix(y_true, class_pred)

            fpr.append(Metrics.fpr(conf_m))
            tpr.append(Metrics.tpr(conf_m))

            threshold+=step

        return tpr, fpr

    def auc(tpr_ar, fpr_ar):
        return -1 * np.trapz(tpr_ar, fpr_ar)


class ConfusionMatrix():
    def __init__(self, y_test, y_pred):
        self.matrix = pd.crosstab(y_test, y_pred).reindex(columns=[0,1],index=[0,1], fill_value=0).values
        self.TN = self.matrix[0][0]
        self.FP = self.matrix[0][1]
        self.FN = self.matrix[1][0]
        self.TP = self.matrix[1][1]

    def print(self):
        fig, ax = plt.subplots()
        sns.heatmap(pd.DataFrame(self.matrix), annot=True, cmap="YlGnBu", fmt='g')
        ax.xaxis.set_label_position("top")
        plt.tight_layout()
        plt.title('Confusion matrix', y=1.1)
        plt.ylabel('Actual')
        plt.xlabel('Predicted')
