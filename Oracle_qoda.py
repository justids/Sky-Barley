


import numpy as np
import math
import qoda
import random
n_qubits = 25

y = math.pi/5
N = 2**(n_qubits-1)
target = n_qubits -1

print(y/N)

kernel,thetas = qoda.make_kernel(list)
qubits = kernel.qalloc(n_qubits)

for i in range(n_qubits-1):
    kernel.h(target=qubits[i])

kernel.ry(parameter=thetas[0], target = qubits[target])

for i in range(n_qubits-1):
    kernel.rx(thetas[i*8+1], target=qubits[target])
    kernel.rz(thetas[i*8+2] , target=qubits[target])
    kernel.rx(thetas[i*8+3] , target=qubits[target])
    kernel.rz(thetas[i*8+4] , target=qubits[target])

    kernel.cx(control=qubits[i], target=qubits[target])
    kernel.rx(thetas[i*8+5] , target=qubits[target])
    kernel.rz(thetas[i*8+6] , target=qubits[target])
    kernel.rx(thetas[i*8+7] , target=qubits[target])
    kernel.rz( thetas[i*8+8] , target=qubits[target])

    kernel.cx(control=qubits[i], target=qubits[target])
    #kernel.cry(2**(i+1) * y/ N, control=qubits[i], target=qubits[target])

get_result = lambda parameter_vector: qoda.observe(kernel, parameter_vector, shots_count = 100)
parameter_vector = [y/N]
for i in range(n_qubits-1):
    parameter_vector.append(math.pi/2)
    parameter_vector.append(2**(i+1)*y/N/2+math.pi)
    parameter_vector.append(math.pi/2)
    parameter_vector.append(3*math.pi)
    parameter_vector.append(math.pi/2)
    parameter_vector.append(-2**(i+1)*y/N/2+math.pi)
    parameter_vector.append(math.pi/2)
    parameter_vector.append(3*math.pi)
result = qoda.sample(kernel, parameter_vector)
print(result)
