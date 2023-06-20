
from ai.models.model import Model
from qiskit_machine_learning.algorithms.classifiers import VQC
from qiskit.algorithms.optimizers import COBYLA

import matplotlib.pyplot as plt
from IPython.display import clear_output

plt.rcParams["figure.figsize"] = (12, 6)

class QS_VQC(Model):
  def __init__(self, name, desc):
    super().__init__(name, desc)

  def set_model(self, args):
    _, feature_map, ansatz = args

    self.model = VQC(
      feature_map=feature_map,
      ansatz=ansatz,
      optimizer=COBYLA(maxiter=100),
      callback=self.callback_graph
    )

  ## A method to draw the objective function
  def callback_graph(self, weights, obj_func_eval):
    clear_output(wait=True)
    self.objective_func_vals.append(obj_func_eval)
    plt.title("Objective function value against iteration")
    plt.xlabel("Iteration")
    plt.ylabel("Objective function value")
    plt.plot(range(len(self.objective_func_vals)), self.objective_func_vals, color='blue')
    # plt.show(block=False)
    plt.pause(0.001)
