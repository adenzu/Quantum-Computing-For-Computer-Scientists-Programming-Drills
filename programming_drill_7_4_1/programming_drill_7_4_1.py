import numpy as np
# programming drill 7.4.1


class QuantumGate(np.ndarray):
    @classmethod
    def TensorProduct(cls, gate1, gate2):
        if gate1.shape != gate2.shape:
            raise ValueError('gate shape is invalid')
        return np.kron(gate1, gate2)

    @classmethod
    def Identity(cls, n_qubits: int):
        return np.eye(2**n_qubits, dtype=np.complex64)

    @classmethod
    def Hadamard(cls):
        return np.array([[1, 1], [1, -1]], dtype=np.complex64) / np.sqrt(2)

    @classmethod
    def R(cls, theta: float):
        return np.array([[1, 0], [0, np.exp(1j * theta)]], dtype=np.complex64)

    @classmethod
    def CNOT(cls):
        return np.array([[1, 0, 0, 0],
                         [0, 1, 0, 0],
                         [0, 0, 0, 1],
                         [0, 0, 1, 0]], dtype=np.complex64)


class QuantumEmulator:
    def __init__(self, n_qubits: int):
        self.n = n_qubits
        self.state = np.zeros(2**n_qubits, dtype=np.complex64)
        self.gates = []

    def changeStateSize(self, n_qubits: int):
        self.n = n_qubits
        self.state = np.zeros(2**n_qubits, dtype=np.complex64)

    def setInitialState(self, state: np.ndarray):
        if state.shape != (2**self.n,):
            raise ValueError('state shape is invalid')
        self.state = state

    def addGate(self, gate: QuantumGate):
        if gate.shape != (2**self.n, 2**self.n):
            raise ValueError('gate shape is invalid')
        self.gates.append(gate)

    def resetGates(self):
        self.gates = []

    def measure(self):
        if np.all(self.state == 0):
            raise ValueError('state is empty')
        current_state = self.state.copy()
        for gate in self.gates:
            current_state = gate @ current_state
        return np.random.choice(range(2**self.n), p=np.abs(current_state)**2)


def main():
    n_qubits = 2
    qem = QuantumEmulator(n_qubits)

    n_samples = 10_000

    # test 1 - 2 qubits hadamard gates
    qem.setInitialState(np.array([1, 0, 0, 0], dtype=np.complex64))
    qem.addGate(QuantumGate.TensorProduct(
        QuantumGate.Hadamard(), QuantumGate.Hadamard()))
    results = np.zeros(2**n_qubits, dtype=np.int32)
    for _ in range(n_samples):
        results[qem.measure()] += 1
    print(results / n_samples)
    print("Test passed" if np.allclose(results / n_samples,
          [0.25, 0.25, 0.25, 0.25], rtol=0.04) else "Test failed")

    # test 2 - 2 qubits entangled hadamard gate
    qem.setInitialState(np.array([1, 0, 0, 0], dtype=np.complex64))
    qem.addGate(QuantumGate.TensorProduct(
        QuantumGate.Identity(1), QuantumGate.Hadamard()))
    qem.addGate(QuantumGate.CNOT())
    results = np.zeros(2**n_qubits, dtype=np.int32)
    for _ in range(n_samples):
        results[qem.measure()] += 1
    print(results / n_samples)
    print("Test passed" if np.allclose(results / n_samples, [0.5, 0, 0, 0.5], rtol=0.02)
          else "Test failed")


if __name__ == '__main__':
    main()
