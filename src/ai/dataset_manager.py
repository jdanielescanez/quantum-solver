
import os
from ai.dataset import Dataset

DATASETS_PATH = 'src/ai/datasets/'

class DatasetManager:
  def __init__(self):
    self.datasets = [Dataset(DATASETS_PATH + file_name) for file_name in os.listdir(DATASETS_PATH)]
    self.current_dataset = None

  ## Print the available datasets
  def print_available_datasets(self):
    print('\nAvaliable datasets:')
    for i in range(len(self.datasets)):
      print('[' + str(i + 1) + ']', self.datasets[i].name)

  ## Dataset selection menu
  def select_dataset(self):
    self.current_dataset = None
    range_datasets = '[1 - ' + str(len(self.datasets)) + ']'
    index = -2
    while index < 0 or index >= len(self.datasets):
      msg = '[&] Select a dataset of the list ' + str(range_datasets) + ': '
      index = int(input(msg)) - 1
      if index == -1:
        self.current_dataset = None
        print('[$] Dataset not selected')
        return
      if index < 0 or index >= len(self.datasets):
        index = -1
        print('[!] The dataset must be one of the list', range_datasets)
      else:
        self.current_dataset = self.datasets[index]
        print('[$]', self.current_dataset.name, 'selected')

  def get_current_dataset(self):
    return self.current_dataset.get_view()

  def get_current_size(self):
    return len(self.get_current_dataset().columns) - 1

  def print_current_dataset(self):
    print(self.get_current_dataset())

  def create_view(self):
    self.current_dataset.reset_view()
    cols = self.current_dataset.important_vars
    range_cols = '[1 - ' + str(len(cols)) + ']'
    index = -2
    print('[*] The important variables of', self.current_dataset.name,
        'dataset are:', str(self.current_dataset.important_vars))
    while index < 0 or index >= len(cols):
      msg = '[&] Select a view size in range ' + str(range_cols) + ': '
      index = int(input(msg)) - 1
      if index == -1:
        print('[$] View not created')
        return None
      if index < 0 or index >= len(cols):
        index = -1
        print('[!] The size of the view must be in range ' + str(range_cols))
      else:
        size = index + 1
        self.current_dataset.set_view_size(size)
        print('[$] Created view:')
        print(self.current_dataset.get_view())
        return {'type': 'decision_tree', 'size': size}

  def reset_view(self):
    print('[$] Reseted view')
    self.current_dataset.reset_view()
