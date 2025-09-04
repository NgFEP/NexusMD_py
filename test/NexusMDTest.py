"""
NexusMD quick-start example

Tips:
- Set conf.useCuda = True to run on GPU (requires CUDA runtime).
- 'steps' is total MD steps; 'reportEvery' controls logging/output cadence.
- Forces are ON by default.
- Controllers (Thermostat/Barostat) are OFF by default; enable them explicitly.
- Rigid-water and H-covalent constraints are optional.

Caveat: Not recommended to switch OFF Harmonic Bond or Harmonic Angle forces:
    the system can collapse without these constraints.
"""

from NexusMD import cfg, run

conf = cfg()
conf.systemXml = "system_dhfr_ecoli_protein.xml"
conf.stateXml  = "state_dhfr_ecoli_protein.xml"
conf.pdbInput  = "dhfr_ecoli_protein.pdb"
conf.pdbOutput = "output_SimRun_dhfr_ecoli_protein.pdb"

# Device
conf.useCuda     = True   # True for GPU, False for CPU
conf.steps       = 100
conf.reportEvery = 10

# Forces
conf.forceHarmonicAngle   = True
conf.forceHarmonicBond    = True
conf.forcePeriodicTorsion = True
conf.forceNonbonded       = True

# Controllers
conf.enableThermostat(300.0, 10.0)  # T [K], collision frequency [1/ps]
conf.enableBarostat(1.0, 200)       # P [bar], apply every N steps

# Constraints
conf.rigidWater    = True
conf.hcovalentBond = True

# Run MD
run(conf)
