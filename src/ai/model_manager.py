
from ai.models.qs_svc import QS_SVC
from ai.models.qs_vqc_z_ra import QS_VQC_Z_RA
from ai.models.qs_vqc_z_esu2 import QS_VQC_Z_ESU2
from ai.models.qs_vqc_z_ep import QS_VQC_Z_EP
from ai.models.qs_vqc_zz_ra import QS_VQC_ZZ_RA
from ai.models.qs_vqc_zz_esu2 import QS_VQC_ZZ_ESU2
from ai.models.qs_vqc_zz_ep import QS_VQC_ZZ_EP

class ModelManager:
  ## Constructor
  def __init__(self):
    ## The selected current model
    self.current_model = None
    ## The available models
    self.models = [
      QS_SVC(),
      QS_VQC_Z_RA(),
      QS_VQC_Z_ESU2(),
      QS_VQC_Z_EP(),
      QS_VQC_ZZ_RA(),
      QS_VQC_ZZ_ESU2(),
      QS_VQC_ZZ_EP(),
    ]

  ## Current model setter
  def set_current_model(self, i):
    if i < len(self.models):
      self.current_model = self.models[i]

  ## Print the available models
  def print_available_models(self):
    print('\nAvaliable models:')
    for i in range(len(self.models)):
      model = self.models[i]
      print('[' + str(i + 1) + ']\tName:', model.name)
      print('\tDescription:', model.description)

  ## Model selection menu
  def select_model(self):
    self.parameters = None
    range_models = '[1 - ' + str(len(self.models)) + ']'
    index = -2
    while index < 0 or index >= len(self.models):
      msg = '[&] Select a model of the list ' + str(range_models) + ': '
      index = int(input(msg)) - 1
      if index == -1:
        self.current_model = None
        print('[$] Model not selected')
        return
      if index < 0 or index >= len(self.models):
        index = -1
        print('[!] The model must be one of the list', range_models)
      else:
        self.current_model = self.models[index]
        print('[$]', self.current_model.name, 'selected')
