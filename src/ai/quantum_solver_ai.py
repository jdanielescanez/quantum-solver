#!/usr/bin/env python3

# Author: Daniel Escanez-Exposito

from ai.dataset_manager import DatasetManager
from ai.model_manager import ModelManager
from halo import Halo
from pwinput import pwinput
import time
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime
from sklearn.metrics import roc_curve, auc, confusion_matrix
from sklearn.preprocessing import label_binarize
import numpy as np
import pandas as pd
import seaborn as sn

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
    self.__main_menu()
  
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
    saved_model = self.model_manager.current_model

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
        self.model_manager.current_model = saved_model
        halo.fail()
        print('Exception:', exception)
        raise exception

    self.model_manager.current_model = saved_model
    header = 'Model | Train Score | Test Score'
    print('\nDataset:', dataset_name)
    print('-' * (len(dataset_name) + 8) + '\n')
    print(26 * ' ' + header)
    print((26 + len(header)) * '=')
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

    fitted_model = model.fit(dataset.train_data, dataset.train_targets.values.ravel(), [size])
    classes = model.model.classes_

    train_targets = label_binarize(dataset.train_targets, classes=classes)
    train_score = fitted_model.decision_function(dataset.train_data)
    train_pred = label_binarize(fitted_model.predict(dataset.train_data), classes=classes)
    self.__save_roc_curves(train_targets, train_score, classes, 'train')
    self.__save_confusion_matrix(train_targets, train_pred, classes, 'train')

    test_targets = label_binarize(dataset.test_targets, classes=classes)
    test_score = fitted_model.decision_function(dataset.test_data)
    test_pred = label_binarize(fitted_model.predict(dataset.test_data), classes=classes)
    self.__save_roc_curves(test_targets, test_score, classes, 'test')
    self.__save_confusion_matrix(test_targets, test_pred, classes, 'test')

    return {
      'train': model.score(dataset.train_data, dataset.train_targets),
      'test':  model.score(dataset.test_data, dataset.test_targets)
    }
  
  def __save_confusion_matrix(self, targets, pred, classes, file_tag):
    model_name = self.model_manager.current_model.name
    dataset_name = self.dataset_manager.current_dataset.name
    FILE_PATH_CONFUSION = 'src/ai/generated_images/' + model_name + '_' + dataset_name + '_'
    FILE_PATH_CONFUSION += datetime.today().strftime('%Y-%m-%d_%H-%M-%S')
    FILE_PATH_CONFUSION += '_confusion_matrix'

    confusion = confusion_matrix(targets.argmax(axis=1), pred.argmax(axis=1))
    df_cm = pd.DataFrame(confusion, index=classes, columns=classes)
    fig = plt.figure()
    sn.heatmap(df_cm, annot=True, fmt='g')
    plt.title(model_name + ' - ' + dataset_name + f' ({file_tag}) confusion matrix')
    plt.xlabel('Predicted Label')
    plt.ylabel('True Label')
    fig.savefig(FILE_PATH_CONFUSION + '_' + file_tag + '.png', format='png')
    fig.savefig(FILE_PATH_CONFUSION + '_' + file_tag + '.eps', format='eps')

  def __save_roc_curves(self, targets, y_score, classes, file_tag):
    n_classes = classes.shape[0]
    
    if n_classes == 2:
      y_score = np.array(list(map(lambda x: [x], y_score)))

    # Compute ROC curve and ROC area for each class
    fpr = dict()
    tpr = dict()
    roc_auc = dict()
    limit_classes = n_classes if n_classes != 2 else 1
    for i in range(limit_classes):
      fpr[i], tpr[i], _ = roc_curve(targets[:, i], y_score[:, i])
      roc_auc[i] = auc(fpr[i], tpr[i])

      plt.figure()
      plt.plot(
          fpr[i],
          tpr[i],
          color="darkorange",
          label="ROC curve (area = %0.2f)" % roc_auc[i],
      )
      plt.plot([0, 1], [0, 1], color="navy", linestyle="--")
      plt.xlim([0.0, 1.0])
      plt.ylim([0.0, 1.05])
      plt.xlabel("False Positive Rate")
      plt.ylabel("True Positive Rate")
      plt.title("Receiver operating characteristic example")
      plt.legend(loc="lower right")

      dataset_name = self.dataset_manager.current_dataset.name
      model_name = self.model_manager.current_model.name
      FILE_PATH = 'src/ai/generated_images/' + model_name + '_' + dataset_name + '_'
      FILE_PATH += datetime.today().strftime('%Y-%m-%d_%H-%M-%S') + '_' + classes[i]
      FILE_PATH += '_' + file_tag
      plt.savefig(FILE_PATH + '.eps', format='eps')
      plt.savefig(FILE_PATH + '.png', format='png')

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
      except Exception as e:
        raise e
