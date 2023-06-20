#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from ai.dataset_manager import DatasetManager
from ai.model_manager import ModelManager
from halo import Halo
from pwinput import pwinput
import time
import matplotlib.pyplot as plt
import seaborn as sns

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
    self.view_conf = None

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
      print('\tCurrent Dataset: ' + \
          self.dataset_manager.current_dataset.name)
    print('[4] Select Model')
    if self.is_selected_model:
      print('\tCurrent Model: ' + self.model_manager.current_model.name)
    if self.is_selected_dataset:
      print('[5] Set a View')
      if self.is_created_view:
        view_type, view_size = self.view_conf['type'], self.view_conf['size']
        print('\tCurrent View: ' + view_type + ' - size: ' + str(view_size))
      print('[6] See current Dataset (applying the View)')
    if self.is_selected_dataset and self.is_selected_model:
      print('[7] Train')
    
    if self.is_selected_dataset:
      print('[8] Experimental Mode [Dataset] (Train all models on the current dataset)')
    
    print('[9] Experimental Mode [ALL] (Train all models on all datasets)')
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
    elif option == 5:
      self.view_conf = self.dataset_manager.create_view()
    elif option == 6:
      df = self.dataset_manager.get_current_dataset()
      sns.pairplot(df, hue="class", palette="tab10")
      plt.show()
      self.dataset_manager.print_current_dataset()
    elif option == 7 and self.is_selected_dataset and self.is_selected_model:
      self.train()
    elif option == 8 and self.is_selected_dataset:
      self.experimental_mode_dataset()
    elif option == 9:
      self.experimental_mode_all()
    else:
      print('[!] Invalid option, try again')
    
  ## Train the current model using the current dataset
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
      print('\n[$] Experiment finished in ' + str(time_s) + ' s!')
      print('Results (' + model_name + ' - ' + dataset_name + '):', results)
    except Exception as exception:
      halo.fail()
      print('Exception:', exception)
      raise exception
  
    return results

## Train the all models using the current dataset
  def experimental_mode_dataset(self):
    results = {}
    dataset_name = self.dataset_manager.current_dataset.name

    for current_model in self.model_manager.models:
      self.model_manager.current_model = current_model
      model_name = self.model_manager.current_model.name

      start_time = time.time()
      halo_text = 'Executing ' + model_name + ' - ' + dataset_name
      halo = Halo(text=halo_text, spinner="dots")
      print()
      try:
        halo.start()

        results[model_name] = self.__train_and_get_data()
        
        halo.succeed()
        time_s = (time.time() - start_time)
        print('\n[$] Experiment finished in ' + str(time_s) + ' s!')
        print('Results (' + model_name + ' - ' + dataset_name + '):', results[model_name])
      except Exception as exception:
        halo.fail()
        print('Exception:', exception)
        raise exception

    print('\nDataset:', dataset_name)
    print('-' * (len(dataset_name) + 8) + '\n')
    print('Model                           | Train Score | Test Score')
    for model_name in results.keys():
      train_score, test_score = results[model_name]['train'], results[model_name]['test']
      print(model_name.rjust(31) + f" | {train_score:11.2f} | {test_score:10.2f}")
  
    return results

## Train the all models using the all datasets
  def experimental_mode_all(self):
    results = {}
    for current_dataset in self.dataset_manager.datasets:
      self.dataset_manager.current_dataset = current_dataset
      dataset_name = self.dataset_manager.current_dataset.name
      results[dataset_name] = {}

      for current_model in self.model_manager.models:
        self.model_manager.current_model = current_model
        model_name = self.model_manager.current_model.name

        start_time = time.time()
        halo_text = 'Executing ' + model_name + ' - ' + dataset_name
        halo = Halo(text=halo_text, spinner="dots")
        print()
        try:
          halo.start()

          results[dataset_name][model_name] = self.__train_and_get_data()
          
          halo.succeed()
          time_s = (time.time() - start_time)
          print('\n[$] Experiment finished in ' + str(time_s) + ' s!')
          print('Results (' + model_name + ' - ' + dataset_name + '):', results[dataset_name][model_name])
        except Exception as exception:
          halo.fail()
          print('Exception:', exception)
          raise exception

    for dataset_name in results.keys():
      results_dataset = results[dataset_name]
      print('\nDataset:', dataset_name)
      print('-' * (len(dataset_name) + 8) + '\n')
      print('Model'.rjust(32) + ' | Train Score | Test Score')
      for model_name in results_dataset.keys():
        train_score, test_score = results_dataset[model_name]['train'], results_dataset[model_name]['test']
        print(model_name.rjust(32) + f" | {train_score:10.2f} | {test_score:10.2f}")
  
    return results

  def __train_and_get_data(self):
    model = self.model_manager.current_model
    dataset = self.dataset_manager.current_dataset
    size = self.dataset_manager.get_current_size()

    plt.figure(0)
    plt.figure(0).clear()

    model.fit(dataset.train_data, dataset.train_targets.values.ravel(), [size])
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
        ## If a view has been created and is activated
        self.is_created_view = self.view_conf != None

        self.__show_options()
        self.__select_option()
      except Exception as _:
        pass
