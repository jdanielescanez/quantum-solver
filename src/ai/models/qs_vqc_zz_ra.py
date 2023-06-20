
from ai.models.qs_vqc import QS_VQC
from qiskit.circuit.library import ZZFeatureMap, RealAmplitudes


class QS_VQC_ZZ_RA(QS_VQC):
  def __init__(self):
    super().__init__('VQC_ZZ_RA', 'Variational Quantum Classifier - ZZFeatureMap - RealAmplitudes')

  def set_model(self, args):
    n_qubits = args[0]
    feature_map = ZZFeatureMap(feature_dimension=n_qubits, reps=2)
    ansatz = RealAmplitudes(num_qubits=n_qubits, reps=2)

    args.append(feature_map)
    args.append(ansatz)

    super().set_model(args)

