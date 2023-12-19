import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

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


class ConfusionMatrix():
    def __init__(self, y_test, y_pred):
        self.matrix = pd.crosstab(y_test, y_pred).values
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
