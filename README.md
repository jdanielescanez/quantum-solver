
# QuantumSolver

<div align="center">
  <a href="https://github.com/jdanielescanez/quantum-solver">
    <img src="https://github.com/jdanielescanez/quantum-solver/blob/main/images/logo192.png?raw=true" alt="Quantum Solver Logo" class="center">
  </a>

  <h3 align="center">QuantumSolver</h3>

  <p align="center">
    A little quantum toolset developed using <a href="https://qiskit.org/">Qiskit</a>
    <br />
    <a href="https://jdanielescanez.github.io/quantum-solver/"><strong>Explore the docs »</strong></a>
    <br />
    </p>
</div>

<!-- omit in toc -->
## Table of Contents
- [QuantumSolver](#quantumsolver)
  - [Getting started](#getting-started)
    - [Warning](#warning)
    - [Download and install](#download-and-install)
    - [Command Line Interface](#command-line-interface)
      - [QuantumSolver Basic](#quantumsolver-basic)
      - [QuantumSolver Subroutine](#quantumsolver-subroutine)
      - [QuantumSolver Crypto](#quantumsolver-crypto)
      - [QuantumSolver AI](#quantumsolver-ai)
    - [Web Interface](#web-interface)
      - [Backend](#backend)
      - [Frontend](#frontend)
      - [Screenshots](#screenshots)
  - [How to contribute to QuantumSolver?](#how-to-contribute-to-quantumsolver)
    - [QuantumSolver Basic](#quantumsolver-basic-1)
    - [QuantumSolver Subroutine](#quantumsolver-subroutine-1)
    - [QuantumSolver Crypto](#quantumsolver-crypto-1)
    - [QuantumSolver Composer](#quantumsolver-composer)
  - [Documentation](#documentation)

## Getting started

### Warning

The toolset uses your personal IBM Quantum Experience token to access to the IBM hardware. You can access to your API token or generate another one [here](https://quantum-computing.ibm.com/account).

You can also use the Guest Mode which only allows you to run quantum circuits in simulators.

### Download and install

This installation has been tested in the Linux distribution environment: Ubuntu 22.04.1.

```sh
# Update and install
sudo apt update && sudo apt upgrade

sudo apt install -y make build-essential libssl-dev zlib1g-dev \
libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python3-openssl \
git

# Pyenv installation
git clone https://github.com/pyenv/pyenv.git ~/.pyenv
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
echo 'eval "$(pyenv init --path)"' >> ~/.bashrc
```

It is now important to restart the terminal
```sh
reset
```

Python 3.8.12 installation
```sh
pyenv install 3.8.12
pyenv global 3.8.12
```

NVM installation
```bash
wget -qO- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.1/install.sh | bash
exec bash -l
```

Node 19.0.1 installation
```sh
nvm install node
nvm install 19.0.1
nvm use 19.0.1
```

QuantumSolver Installation
```bash
git clone https://github.com/jdanielescanez/quantum-solver.git
cd quantum-solver
python -m pip install -e .
cd web
npm install
```

### Command Line Interface

#### QuantumSolver Basic

This main program allows the execution of the circuits corresponding to the basic quantum algorithms: Radom Generation Number, Deutsch-Jozsa, Bernstein-Vazirani, Grover (2-qubits), Quantum Teleportation and Superdense Coding.

```
python3 src/main_quantum_solver.py [optional IBMQ_TOKEN]
```

#### QuantumSolver Subroutine

The main Subroutine program allows running more complex algorithms that require preprocessing of the parameters, and postprocessing of the output from the repeated execution of the defined circuits. 

```
python3 src/main_subroutine.py [optional IBMQ_TOKEN]
```


#### QuantumSolver Crypto

This main program gives the option to run a simulation of the following quantum cryptographic protocols: BB84, E91, B92, Six-State, a Quantum Substitute for RSA and Quantum Elgamal.

```
python3 src/main_crypto.py [optional IBMQ_TOKEN]
```


<!-- TODO:

#### QuantumSolver Composer

Permitir un bucle REPL capaz de añadir las diferentes funcionalidades, visualizar y ejecutar el circuito en cualquier momento (añadiendo entradas que el usuario defina por pantalla)

```
python3 src/main_composer.py [optional IBMQ_TOKEN]
```
-->

#### QuantumSolver AI

<!-- TODO: Add doc -->
```
python3 src/main_ai.py
```

### Web Interface

#### Backend

```
cd web
python3 src/flask-server/server.py
```

#### Frontend

```
cd web
npm run dev
```

#### Screenshots

<!-- omit in toc -->
##### Home Page
<div align="center">
  <img src="https://github.com/jdanielescanez/quantum-solver/blob/main/images/web-interface/home_web.png?raw=true" alt="Home Page" class="center">
</div>

<!-- omit in toc -->
##### Token Page
<div align="center">
  <img src="https://github.com/jdanielescanez/quantum-solver/blob/main/images/web-interface/token_web.png?raw=true" alt="Token Page" class="center">
</div>

<!-- omit in toc -->
##### Main Menu Page
<div align="center">
  <img src="https://github.com/jdanielescanez/quantum-solver/blob/main/images/web-interface/main_menu_web.png?raw=true" alt="Main Menu Page" class="center">
</div>

<!-- omit in toc -->
##### Run Page
<div align="center">
  <img src="https://github.com/jdanielescanez/quantum-solver/blob/main/images/web-interface/run_web.png?raw=true" alt="Run Page" class="center">
</div>

<!-- omit in toc -->
##### Run Experimental Mode Page
<div align="center">
  <img src="https://github.com/jdanielescanez/quantum-solver/blob/main/images/web-interface/run_experimental_mode_web.png?raw=true" alt="Run Experimental Mode Page" class="center">
</div>

## How to contribute to QuantumSolver?

### QuantumSolver Basic

Creates a derived class (whose name is the name of the algorithm in upper camel case format) in the `src/algorithms` directory from the abstract class `QAlgorithm`. To do this, you can copy and paste the simplest algorithm file found in the `QRand` library, changing the data to suit the circuit you want to implement. The data you must change, besides the name of the file itself (which should be the name of the class in snake case format):
- Algorithm name
- Brief description of the problem to be solved
- List of parameter objects, indicating for each of them the type, a brief description and a warning about the allowed values
- A method that given a `counts` result of the execution of the circuit extracts the result
- A lambda function that parses the entered parameters
- A method that checks the validity of the entered parameters
- A method that returns the parameterized circuit itself based on the parameters

It may seem an exahusive list, but following the `QAlgorithm` template (and especially its simpler implementation in `QRand`) it is quite simple. If you have any questions in this regard, follow the examples intuitively, open an issue or contact the developers.

Once the derived class has been created, to add it to QuantumSolver just add it to the `QAlgorithmManager` in the `src/algorithms/qalgorithmm_manager.py` directory. In the imported libraries add a line:
```python
from algorithms.algorithm_file_name import AlgorithmClass
```

Finally, add to the array of available algorithms your contribution:
```python
self.algorithms = [
      QRand(),
      DeutschJozsa(),
      BernsteinVazirani(),
      Grover(),
      QuantumTeleportation(),
      SuperdenseCoding(),
      AlgorithmClass()
    ]
```

In this way, the protocol will be available both in the QuantumSolver Basic command line interface and in the web interface. Consider making a Pull Request for the changes to be made publicly effective.

### QuantumSolver Subroutine

To contribute to this module, the procedure is completely analogous to that of QuantumSolver Basic. It has two minor differences:
- It uses `SubroutineManager` (`src/subroutine/subroutine_manager.py`) instead of `AlgorithmManager`.
- The `QSubroutine` class has two more methods than `QAlgorithm`:
  - One for preprocessing, where you must place the instructions you want to practice to the parameters before becoming part of the input to the circuit constructor.
  - Another one of postprocessing, where the instructions that transform the output of the repeated execution of the circuit (`counts`) in the final result of the algorithm to be implemented are included. 

The approach taken in the first simple derivative class for the Quantum Phase Estimation algorithm can be clearly seen.

### QuantumSolver Crypto

Follow the example implementation of any of the previously defined protocols (we recommend the use of BB84 as an initial template). To add your quantum cryptography protocol to QuantumSolver just add your created class to the protocols array of the `CyrptoManager` class of the `srcrypto_manager.py` file.

1. Add the import of your protocol
```python
from crypto.name_dir.name_file import CryptoProtocol
```
2. Adds the protocol class to the array
```python
self.protocols = [
  BB84(token),
  E91(token),
  B92(token),
  SixState(token),
  RsaSubstitute(token),
  ElGamal(token),
  CryptoProtocol(token)
]
```

With these steps, your protocol can be simulated from the main program `src/main_crypto.py`. Consider making a Pull Request for the changes to be made publicly effective.


### QuantumSolver Composer

Any complex classical circuit procedure can be defined from existing circuits or by creating new primitives. This module is still in the experimental phase.

## Documentation

QuantumSolver documentation is available at [https://jdanielescanez.github.io/quantum-solver/](https://jdanielescanez.github.io/quantum-solver/).
