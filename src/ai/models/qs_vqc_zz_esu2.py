
from ai.models.qs_vqc import QS_VQC
from qiskit.circuit.library import ZZFeatureMap, EfficientSU2


class QS_VQC_ZZ_ESU2(QS_VQC):
  def __init__(self):
    super().__init__('VQC_ZZ_ESU2', 'Variational Quantum Classifier - ZZFeatureMap - EfficientSU2')

  def set_model(self, args):
    n_qubits = args[0]
    feature_map = ZZFeatureMap(feature_dimension=n_qubits, reps=2)
    ansatz = EfficientSU2(num_qubits=n_qubits, reps=2)

    args.append(feature_map)
    args.append(ansatz)

    super().set_model(args)
