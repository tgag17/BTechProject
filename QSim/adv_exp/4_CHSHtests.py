from qiskit import QuantumRegister, ClassicalRegister
from qiskit import QuantumCircuit, execute, BasicAer
import numpy as np
import time

#Options & Noise goes here - Don't change options variable name & block
options = {
"rotation_error": {'rx':[1.0, 0.0], 'ry':[1.0, 0.0], 'rz':[1.0,0.0]},
"tsp_model_error": [1.0, 0.0],
"thermal_factor": 1.0,
"decoherence_factor": 1.0,
"depolarization_factor": 1.0,
"bell_depolarization_factor": 1.0,
"decay_factor": 1.0,
}

backend = BasicAer.get_backend('dm_simulator')

s = 0
for i in range(4):
  qc = QuantumCircuit()
  q = QuantumRegister(2, 'q')
  c = ClassicalRegister(2, 'c')

  qc.add_register(q)
  qc.add_register(c)

  a = np.pi/10

  qc.h(0)
  qc.cx(0, 1)
  qc.ry(a, 0)
  
  if i == 1 or i == 3:
    qc.h(0)
  if i == 2 or i == 3:
    qc.h(1)

  qc.measure(q[0],c[0])
  qc.measure(q[1],c[1])

##### 

  tic = time.time()
  job = execute(qc, backend=backend, **options)
  toc = time.time()
  job_result = job.result()
  
  s += toc-tic
  
print(s)
