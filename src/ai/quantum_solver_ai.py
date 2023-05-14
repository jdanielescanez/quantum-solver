#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from ai.dataset_manager import DatasetManager
from ai.model_manager import ModelManager
from halo import Halo
from pwinput import pwinput
import time
import matplotlib.pyplot as plt

QUANTUM_SOLVER_AI = 'QuantumSolver AI'

## Main Class of QuantumSolver AI
class QuantumSolverAI():
  ## Constructor
  def __init__(self, token=None):
    ## A DatasetManager instance
    self.dataset_manager = DatasetManager()
    ## A ModelManager instance
    self.model_manager = ModelManager()

  ## Run main function
  def run(self):
    self.__show_header()
    self.__main_menu()

  ## Print header
  def __show_header(self):
    print('\n' + QUANTUM_SOLVER_AI + '\n' + '=' * len(QUANTUM_SOLVER_AI) + '\n')
    print('A little quantum toolset developed using Qiskit')
  
  ## Print options
  def __show_options(self):
    print('\n' + QUANTUM_SOLVER_AI)
    print('=' * len(QUANTUM_SOLVER_AI) + '\n')
    print('[1] See available Datasets')
    print('[2] See available Models')
    print('[3] Select Dataset')
    if self.is_selected_dataset:
      print('\tCurrent Subroutine: ' + \
          self.dataset_manager.current_dataset.name)
    print('[4] Select Model')
    if self.is_selected_model:
      print('\tCurrent Model: ' + self.model_manager.current_model.name)
    if self.is_selected_dataset and self.is_selected_model:
      print('[5] Train')
    print('[0] Exit\n')

  ## Main menu
  def __select_option(self):
    option = int(input('[&] Select an option: '))
    if option == 0:
      print()
      exit(0)
    elif option == 1:
      self.dataset_manager.print_available_datasets()
    elif option == 2:
      self.model_manager.print_available_models()
    elif option == 3:
      self.dataset_manager.select_dataset()
    elif option == 4:
      self.model_manager.select_model()
    elif option == 5 and self.is_selected_dataset and self.is_selected_model:
      self.train()
    else:
      print('[!] Invalid option, try again')
    
  ## Train the current model using the selected backend and dataset
  def train(self):
    dataset_name = self.dataset_manager.current_dataset.name
    model_name = self.model_manager.current_model.name

    start_time = time.time()
    halo_text = 'Executing ' + model_name + ' - ' + dataset_name
    halo = Halo(text=halo_text, spinner="dots")
    try:
      halo.start()

      results = self.__train_and_get_data()
      
      halo.succeed()
      time_s = (time.time() - start_time)
      print('\n[$] Experiment Finished in ' + str(time_s) + ' s!')
      print('Results (' + model_name + ' - ' + dataset_name + '):', results)
    except Exception as exception:
      halo.fail()
      print('Exception:', exception)
      raise exception
  
    return results

  def __train_and_get_data(self):
    model = self.model_manager.current_model
    dataset = self.dataset_manager.current_dataset
    model.fit(dataset.train_data, dataset.train_targets.values.ravel())
    return {
      'train': model.score(dataset.train_data, dataset.train_targets),
      'test':  model.score(dataset.test_data, dataset.test_targets)
    }

  ## Loop for the main menu
  def __main_menu(self):
    while True:
      try:
        ## If a current dataset has been selected
        self.is_selected_dataset = self.dataset_manager.current_dataset != None
        ## If a current model has been selected
        self.is_selected_model = self.model_manager.current_model != None

        self.__show_options()
        self.__select_option()
      except Exception as _:
        pass
