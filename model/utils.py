import matplotlib.pyplot as plt
import seaborn as sns
import random

def plot_missing_values(data):
    missing_data = data.isnull()
    total_missing = missing_data.sum()
    percent_missing = (total_missing / len(data)) * 100

    plt.figure(figsize=(10, 6))
    sns.heatmap(missing_data, cbar=False, cmap='YlGnBu', yticklabels=False)

    for col in data.columns:
        col_missing = percent_missing[col]
        if col_missing > 0:
            col_percentage = round(col_missing, 2)
            plt.text(data.columns.get_loc(col) + 0.5, data.index.get_loc(0) + 0.5, f'{col_percentage}%', 
                     ha='center', va='center', fontsize=6, color='black', fontweight='bold')

    plt.title('Missing Values in Dataset', fontsize=10)
    plt.show()

def plot_missing_values_bar(data):
    missing_values_count = data.isnull().sum().sort_values(ascending=True)
    missing_values_percentage = (missing_values_count / len(data)) * 100

    plt.figure(figsize=(10, 6))
    plt.barh(missing_values_count.index, missing_values_percentage, color='skyblue')
    plt.xlabel('Percentage of Missing Values')
    plt.title('Missing Values in Dataset')

    plt.show()

def train_test_split(X, y, test_size, random_state):
    if random_state is not None:
        random.seed(random_state)

    num_samples = X.shape[0]
    indices = list(range(num_samples))
    random.shuffle(indices)

    split_index = int(num_samples * (1 - test_size))
    train_indices = indices[:split_index]
    test_indices = indices[split_index:]

    X_train, X_test = X[train_indices], X[test_indices]
    y_train, y_test = y[train_indices], y[test_indices]

    return X_train, X_test, y_train, y_test
