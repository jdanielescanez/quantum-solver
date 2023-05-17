
from ai.models.model import Model
from sklearn.svm import SVC

class QS_SVC(Model):
  def __init__(self):
    super().__init__('SVC', 'Support Vector Classifier')

  def set_model(self, _):
    self.model = SVC()
