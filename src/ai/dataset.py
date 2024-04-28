
import pandas as pd
from sklearn import tree
from sklearn.model_selection import train_test_split
from operator import itemgetter
import numpy as np

np.random.seed(42)

class Dataset:
  def __init__(self, file_name):
    self.file_name = file_name
    self.name = file_name.split('/')[-1].split('.')[0]
    self.df = self.__normalize(pd.read_csv(file_name))

    self.__split_data(self.df)
    self.important_vars = self.__compute_important_vars()
    self.view = self.df

  def __normalize(self, df):
    features = df.loc[:, df.columns != 'class']
    features = (features - features.min()) / (features.max() - features.min())
    df.loc[:, df.columns != 'class'] = features
    return df

  def __compute_important_vars(self):
    initial_decision_tree = tree.DecisionTreeClassifier(max_depth=4)
    initial_decision_tree.fit(self.train_data, self.train_targets)

    feature_importances = {}
    for i, col in enumerate(self.df.columns[:-1]):
      feature_importances[col] = initial_decision_tree.feature_importances_[i]

    important_vars = []
    for key, value in sorted(feature_importances.items(), key=itemgetter(1), reverse=True):
      if value != 0.0:
        important_vars.append(key)
    
    return important_vars

  def __split_data(self, df):
    self.features = df.iloc[:, :-1]
    self.targets = df.iloc[:, -1:]
    self.train_data, self.test_data, self.train_targets, self.test_targets = \
        train_test_split(
          self.features,
          self.targets,
          train_size=0.75,
          stratify=self.targets
        )

  def set_view_size(self, view_size):
    self.view = self.df[self.important_vars[:view_size] + ['class']]
    self.__split_data(self.view)

  def reset_view(self):
    self.view = self.df
    self.__split_data(self.view)

  def get_view(self):
    return self.view
