# NexusMD

A Molecular Dynamics Simulation Package for Drug Discovery
## Description

NexusMD is the next-generation molecular dynamics simulation software package to predict protein-ligand binding affinities leading to drug discovery. NexusMD is equipped with modern free energy methods, novel sampling algorithms, and parallel programming to support diverse scientific applications.  
This repository provides a **Python showcase** of the NexusMD interface. It contains a minimal test setup and examples so users can explore how NexusMD simulations are configured and executed.
## Table of Contents

- [Description](#description)
- [Architecture](#architecture)
- [Getting Started](#getting-started)
  - [Dependencies](#dependencies)
  - [Installation (Published Version)](#installation-instructions-published-version)
- [Expected Output](#terminal-output)
- [Current Status](#current-status)
- [Version History](#version-history)
- [License](#license)

---

## Architecture

NexusMD is organized in simple layers so users configure simulations in Python while heavy computation runs in native backends. At a high level:

- **Frontend** – A Python API loads inputs, sets options, and launches a run.
- **Orchestration** – Chooses CPU or GPU execution and prepares the data required by the backend.
- **Core Engine** – Advances the simulation step-by-step, coordinating force evaluation, integration, constraints, and controllers.
- **Data & I/O** – Reads common input formats (e.g., PDB/XML), manages necessary transfers between host and accelerator, and writes coordinates/energies at user-defined intervals.
- **Extensibility** – New forces and analysis features can be added as plugins without changing the core workflow.

---
## Getting Started

### Dependencies

* **Python**: Version 3.11
* **Operating Systems**: 
  * Windows 10, 11
  * Linux (Tested on Ubuntu 20.04 or later)
* **Execution via the source code**:
  * For Windows: Visual Studio 2022
  * For Linux: GCC or Clang (latest version recommended)
* **CUDA**: Required for GPU Acceleration.

* **Execution the published version**:
  *Anaconda*


---

### Installation Instructions (Published Version)

#### Windows

1. **Install Anaconda**:
   - Download and install **Anaconda** from the [official website](https://docs.anaconda.com/anaconda/install/).
   - Select the following Advanced Installation Options during installation:
     <img src="https://github.com/user-attachments/assets/bce75eea-439d-4f04-88cc-be6c3c7e6d50" style="width:50%; height:50%;">

2. **Create a New Anaconda Environment**:
   - Press `Win + S` and type **Environment Variables**.
   - Open the Anaconda Prompt.
   - Create a new environment with Python 3.11:
     ```bash
     conda create -n nexusMD_env python=3.11
     ```
   - Activate the environment:
     ```bash
     conda activate nexusMD_env
     ```
3. **Install NexusMDMD library**:
   - run the following command to install NexusMD 1.2.0 MD software package:
     ```bash
     pip install -i https://test.pypi.org/simple/ NexusMD
     ```
4. **Prepare the Folder**:
   - Create a folder (preferebly on your Desktop for easy navigation on Anaconda Prompt) to contain all necessary files (available in the test folder (NexusMD github repository)):
     - `dhfr_ecoli_protein.pdb`: The PDB file for the system.
     - `system_dhfr_ecoli_protein.xml`: The system XML configuration file.
     - `state_dhfr_ecoli_protein.xml`: The state XML configuration file.
     - `NexusMDTest.py`: Test script for NexusMD.
   - Copy these files into the folder.

5. **Adjust Options in NexusMDTest.py**:
   - Open `NexusMDTest.py` in any text editor or IDE. A straightforward option's [Notepad++](https://notepad-plus-plus.org/downloads/)
   - Adjust any of the following parameters inside the `NexusMDTest.py` to enable or disable their inclusion during the MD simulation.
     ```bash
		conf = cfg()
		conf.systemXml = "system_dhfr_ecoli_protein.xml"
		conf.stateXml  = "state_dhfr_ecoli_protein.xml"
		conf.pdbInput  = "dhfr_ecoli_protein.pdb"
		conf.pdbOutput = "output_SimRun_dhfr_ecoli_protein.pdb"
		
		conf.useCuda     = True   
		conf.steps       = 100
		conf.reportEvery = 10
		
		conf.forceHarmonicAngle   = True
		conf.forceHarmonicBond    = True
		conf.forcePeriodicTorsion = True
		conf.forceNonbonded       = True
		
		conf.enableThermostat(300.0, 10.0) 
		conf.enableBarostat(1.0, 200)     
		
		conf.rigidWater    = True
		conf.hcovalentBond = True
     ```

6. **Run NexusMDTest.py**:
   - Navigate to the folder in the Anaconda Prompt make sure nexusMD_env environment is activated.
   - Run the test script:
     ```bash
     python NexusMDTest.py
     ```
---

### Key Notes
- Ensure the `.pdb`, `.xml`, and `NexusMDTest.py` files are all in the same folder for convenience.
- Adjust any parameters in the `NexusMDTest.py` file to match your use case (e.g., simulation parameters, desired forces, controllers, and constraints to enable, etc.).
- Output and results will depend on the configuration of the provided `.xml` and `.pdb` files.

## **Expected Output**

### **Terminal Output**
```bash
[NexusMD] run(): start
[md] CUDA              : ON
[md] Harmonic Bond     : ON
[md] Harmonic Angle    : ON
[md] Periodic Torsion  : ON
[md] Non-bonded        : ON
[md] Thermostat        : ON
         T = 300 K   Frequency = 10 1/ps
[md] Barostat          : ON
         P = 1 bar   every 200 steps
[md] Rigid water       : ON
[md] H-covalent shake  : ON
step: 0
step: 1
step: 2
step: 3
step: 4
step: 5
step: 6
step: 7
step: 8
step: 9
step: 10
[NexusMD] run(): done
```

### **Generated Files**
- **`output_SimRun_dhfr_ecoli_protein.pdb`** – Final simulation output in PDB format.
- **`PVFReportoutput_SimRun_dhfr_ecoli_protein.pdb`** – Contains **position, velocity, and force** quantities.
- **`TotalEnergyoutput_SimRun_dhfr_ecoli_protein.pdb`** – Records **kinetic, potential, and total energy** values in kJ/mol.
- **`EnsembleReportoutput_SimRun_dhfr_ecoli_protein.pdb`** – Contains **Kinetic Energy, Potential Energy, Temperature, Box Volume and Density** quantities related to controllers performance.
- **`SettleReportoutput_SimRun_dhfr_ecoli_protein.pdb`** – Contains **rigid water constraint** performance .
- **`ShakeReportoutput_SimRun_dhfr_ecoli_protein.pdb`** – Contains **hydrogen covalent bond constraint** performance .

---
## Current Status

- Functional **Python API** with backends (**CPU** or **CUDA**).
- End-to-end **simulation loop**: forces → integration → constraints → controllers → reporting.
- **Input parsing** for PDB/XML and **system initialization**.
- **Periodic boundary** wrapping and analysis outputs.
- **Constraints** (rigid water; H-covalent bonds) and **controllers** (thermostat; barostat).
- **Reporting** of coordinates and energies/ensemble/constraints properties.
- Automated Cross-platform builds under active testing (**Windows**, **Linux** tested).
- Public API and file formats are **experimental** and may change between versions.

---

## Version History
* 1.0.0
    * Initial Release
* 1.2.0
    * Prototype Release

## License
Nexus is licensed under the MIT License. See [LICENSE](https://mit-license.org/) for details.
