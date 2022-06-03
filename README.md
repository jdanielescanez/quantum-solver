
# QuantumSolver

<div align="center">
  <a href="https://github.com/alu0101238944/quantum-solver">
    <img src="https://github.com/alu0101238944/quantum-solver/blob/main/images/logo192.png?raw=true" alt="Quantum Solver Logo" class="center">
  </a>

  <h3 align="center">QuantumSolver</h3>

  <p align="center">
    A little quantum toolset developed using <a href="https://qiskit.org/">Qiskit</a>
    <br />
    <a href="https://alu0101238944.github.io/quantum-solver/"><strong>Explore the docs »</strong></a>
    <br />
    </p>
</div>

<!-- omit in toc -->
## Table of Contents
- [QuantumSolver](#quantumsolver)
  - [Getting started](#getting-started)
    - [Warning](#warning)
    - [Download](#download)
    - [Command Line Interface](#command-line-interface)
      - [QuantumSolver](#quantumsolver-1)
      - [BB84](#bb84)
    - [Web Interface](#web-interface)
      - [Backend](#backend)
      - [Frontend](#frontend)
      - [Screenshots](#screenshots)
  - [Documentation](#documentation)

## Getting started

### Warning

The toolset uses your personal IBM Quantum Experience token to access to the IBM hardware. You can access to your API token or generate another one [here](https://quantum-computing.ibm.com/account).

You can also use the Guest Mode which only allows you to run quantum circuits in a local simulator ("aer_simulator").

### Download

```bash
git clone https://github.com/alu0101238944/quantum-solver.git
cd quantum-solver
pip3 install -e .
```

### Command Line Interface

#### QuantumSolver

```
python3 src/main_quantum_solver.py [optional IBMQ_TOKEN]
```

#### BB84

```
python3 src/main_bb84.py [optional IBMQ_TOKEN]
```

### Web Interface

#### Backend

```
cd quantum_solver_web
python3 src/flask-server/server.py
```

#### Frontend

```
cd quantum_solver_web
npm i
npm start
```

#### Screenshots

<!-- omit in toc -->
##### Home Page
<div align="center">
  <img src="https://github.com/alu0101238944/quantum-solver/blob/main/images/web-interface/home_web.png?raw=true" alt="Home Page" class="center">
</div>

<!-- omit in toc -->
##### Token Page
<div align="center">
  <img src="https://github.com/alu0101238944/quantum-solver/blob/main/images/web-interface/token_web.png?raw=true" alt="Token Page" class="center">
</div>

<!-- omit in toc -->
##### Main Menu Page
<div align="center">
  <img src="https://github.com/alu0101238944/quantum-solver/blob/main/images/web-interface/main_menu_web.png?raw=true" alt="Main Menu Page" class="center">
</div>

<!-- omit in toc -->
##### Run Page
<div align="center">
  <img src="https://github.com/alu0101238944/quantum-solver/blob/main/images/web-interface/run_web.png?raw=true" alt="Run Page" class="center">
</div>

<!-- omit in toc -->
##### Run Experimental Mode Page
<div align="center">
  <img src="https://github.com/alu0101238944/quantum-solver/blob/main/images/web-interface/run_experimental_mode_web.png?raw=true" alt="Run Experimental Mode Page" class="center">
</div>

## Documentation

QuantumSolver documentation is available at [https://alu0101238944.github.io/quantum-solver/](https://alu0101238944.github.io/quantum-solver/).
