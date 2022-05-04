from qiskit import QuantumCircuit, Aer
import time

sim = Aer.get_backend('aer_simulator')

## 1I gate
####################################

qc = QuantumCircuit(1)
qc.i(0)
qc.measure_all()

tic = time.time()
result = sim.run(qc).result()
toc = time.time()

t = toc - tic
print(t)

## 1X gate
####################################

qc = QuantumCircuit(1)
qc.x(0)
qc.measure_all()

tic = time.time()
result = sim.run(qc).result()
toc = time.time()

t = toc - tic
print(t)

## 5X gate - inline 
####################################

qc = QuantumCircuit(1)
for i in range(5):
    qc.x(0)
qc.measure_all()

tic = time.time()
result = sim.run(qc).result()
toc = time.time()

t = toc - tic
print(t)

## 5X gate - parallel 
####################################

qc = QuantumCircuit(5)
for i in range(5):
    qc.x(i)
qc.measure_all()

tic = time.time()
result = sim.run(qc).result()
toc = time.time()

t = toc - tic
print(t)

## 7X gate - parallel 
####################################

qc = QuantumCircuit(7)
for i in range(7):
    qc.x(i)
qc.measure_all()

tic = time.time()
result = sim.run(qc).result()
toc = time.time()

t = toc - tic
print(t)

## 10X gate - parallel 
####################################

qc = QuantumCircuit(10)
for i in range(10):
    qc.x(i)
qc.measure_all()

tic = time.time()
result = sim.run(qc).result()
toc = time.time()

t = toc - tic
print(t)