
from abc import ABC, abstractmethod

class Model(ABC):
  def __init__(self, name, desc):
    ## The name of the model
    self.name = name
    ## A short description of the model
    self.description = desc
    ## The model itself
    self.model = None
    self.objective_func_vals = []

  ## A method to fit the model
  def fit(self, features, targets):
    self.objective_func_vals = []
    return self.model.fit(features, targets)

  ## A method to score the trained model
  def score(self, features, targets):
    return self.model.score(features, targets)