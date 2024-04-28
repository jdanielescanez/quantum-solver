
from abc import ABC, abstractmethod
import numpy as np

np.random.seed(42)

class Model(ABC):
  def __init__(self, name, desc):
    ## The name of the model
    self.name = name
    ## A short description of the model
    self.description = desc
    ## The model itself
    self.model = None
    ## Objective function values
    self.objective_func_vals = []

  @abstractmethod
  def set_model(self, args):
    pass

  ## A method to fit the model
  def fit(self, features, targets, args):
    self.set_model(args)
    self.objective_func_vals = []
    return self.model.fit(features, targets)

  ## A method to score the trained model
  def score(self, features, targets):
    return self.model.score(features, targets)
