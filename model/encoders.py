
class LabelEncoder:
    def __init__(self):
        self.labels = {}

    def fit(self, arr, label):
        unique_values = list(set(arr))
        self.labels[label] = {val: idx for idx, val in enumerate(unique_values)}

    def transform(self, arr, label):
        if label in self.labels:
            return [self.labels[label][item] for item in arr]
        raise ValueError("Must fit the encoder before transforming the data")
    
    def fit_transform(self, arr, label):
        self.fit(arr, label)
        return self.transform(arr, label)
    