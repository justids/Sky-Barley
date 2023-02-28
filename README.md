# Multi Qubit Quantum Amplitude Estimation using Variational circuit
Xandau Qhack Hackathon
### Team Name:

Sky Barley

### Project Description:

Quantum Amplitude Estimation(QAE) is an essential quantum algorithm with applications in quantum machine learning, quantum enhanced Monte-Carlo algorithm, finance, etc.[4] However, QAE uses Quantum Phase Estimation (QPE), which has a deep circuit depth and requires high performance from quantum hardware, making it difficult to operate on noisy intermediate-scale quantum (NISQ) devices.

One algorithm that has been proposed to address these issues is Maximum Likelihood Amplitude Estimation(MLAE). MLAE does not use QPE, but instead exploits classical maximum likelihood estimation to implement a relatively simple circuit, and in certain situations, achieves quadratic speedups.

Variational Quantum Amplitude Estimation (VQAE) is a modified one of MLAE, which adds variational optimization to reduce the depth of the circuit.

In this project, Our team showed that VQAE method can approximate MLAE with small error, Variational Quantum Amplitude Estimation [1] and (2) using the All of our codes are exploited cuQuantum and Quantum Optimized Device Architecture (QODA) provided by NVIDIA.

### File Description 
- 2023 QHack Open Hackathon(Sky Barley).pdf: Summary of the VQAE project.

- QAE_with_MLAE.ipynb: Implemented MLAE with pennylane library. Also we have used lightning.gpu device which uses cuQuantum SDK.      
- Oracle_qoda.py: We have used QODA library to simulate quantum circuit. 

- VQAE.ipynb: Implemented VQAE with pennylane library. Also we have used lightning.gpu device which uses cuQuantum SDK.
- VQAE2.ipynb: Implemented VQAE with other cost systems. 





### Which challenges/prizes would you like to submit your project for?

- NVIDIA Challenge : We exploited cuQauntum and QODA for executing the quantum circuits.
- Quantum computing today! : We reproduced the result of ref 4.
- Hybrid Quantum-Classical Computing Challenge : We used variational circuit ansatz instead of exact oracle which has deep circuit depth.

### References:

[1] K. Plekhanov, M. Rosenkranz, M. Fiorentini, and M. Lubasch, *[\"Variational Quantum Amplitude Estimation\"](https://arxiv.org/abs/2109.03687)*, Arxiv (2021).

[2] Y. Suzuki, S. Uno, R. Raymond, T. Tanaka, T. Onodera, and N. Yamamoto, *[\"Amplitude Estimation without Phase Estimation\"](https://arxiv.org/abs/1904.10246)*, Quantum Inf Process 19, 75 (2020).

[3] G. Brassard, P. Høyer, M. Mosca, and A. Tapp, *Quantum Computation and Information*, Contemp Math 53 (2002).

[4] A. Callison and D. E. Browne, *[\"Improved Maximum-Likelihood Quantum Amplitude Estimation\"](https://arxiv.org/abs/2209.03321)*
, Arxiv (2022)
