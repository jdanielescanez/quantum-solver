
from ai.models.qs_vqc import QS_VQC
from qiskit.circuit.library import ZFeatureMap, ExcitationPreserving


class QS_VQC_Z_EP(QS_VQC):
  def __init__(self):
    super().__init__('VQC_Z_EP', 'Variational Quantum Classifier - ZFeatureMap - ExcitationPreserving')

  def set_model(self, args):
    n_qubits = args[0]
    feature_map = ZFeatureMap(feature_dimension=n_qubits, reps=2)
    ansatz = ExcitationPreserving(num_qubits=n_qubits, reps=2)

    args.append(feature_map)
    args.append(ansatz)

    super().set_model(args)

