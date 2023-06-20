
from ai.models.qs_vqc import QS_VQC
from qiskit.circuit.library import ZFeatureMap, RealAmplitudes


class QS_VQC_Z_RA(QS_VQC):
  def __init__(self):
    super().__init__('VQC_Z_RA', 'Variational Quantum Classifier - ZFeatureMap - RealAmplitudes')

  def set_model(self, args):
    n_qubits = args[0]
    feature_map = ZFeatureMap(feature_dimension=n_qubits, reps=2)
    ansatz = RealAmplitudes(num_qubits=n_qubits, reps=2)

    args.append(feature_map)
    args.append(ansatz)

    super().set_model(args)

