from qiskit import QuantumCircuit, execute, Aer
import qiskit.providers.aer.noise as noise
import numpy as np

lim = np.linspace(0, 2*np.pi, 21)

y = []
for i in lim:
    
    
    error_1 = noise.depolarizing_error(i, 1)
    error_2 = noise.depolarizing_error(i, 2)

    # Add errors to noise model
    noise_model = noise.NoiseModel()
    noise_model.add_all_qubit_quantum_error(error_1, ['u1', 'u2', 'u3'])
    noise_model.add_all_qubit_quantum_error(error_2, ['cx'])

    # Get basis gates from noise model
    basis_gates = noise_model.basis_gates
    
    s = []
    for i in range(4):
        qc = QuantumCircuit(2,2)

        a = np.pi/10

        qc.h(0)
        qc.cx(0, 1)
        qc.ry(a, 0)

        if i == 1 or i == 3:
            qc.h(0)
        if i == 2 or i == 3:
            qc.h(1)

        qc.measure([0, 1], [0, 1])

        result = execute(qc, Aer.get_backend('qasm_simulator'),
                         basis_gates=basis_gates,
                         noise_model=noise_model).result()
        counts = result.get_counts()

        items = counts.items()
        exp_value = 0

        for key,value in items:
            exp_value += (-1)**(int(key[0])+int(key[1])) * value

        exp_value = exp_value/1024
        s.append(exp_value)
        
    y.append(s[0] + s[1] - s[2] + s[3])

