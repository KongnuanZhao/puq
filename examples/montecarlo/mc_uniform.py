#!/usr/bin/env python
"""
Monte Carlo basic example

Usage: mc.py
"""
from puq import *

def run():
    # Declare our parameters here
    v0 = Parameter('v', 'velocity', min=10, max=20)

    # Which host to use
    host = InteractiveHost()
    #host = PBSHost(env='/scratch/prism/memosa/env.sh', cpus_per_node=8, walltime='2:00')

    # select a parameter sweep method
    # These control the parameters sent to the test program
    # Currently the choices include Smolyak, and PSweep
    # For Smolyak, first arg is a list of parameters and second is the level
    uq = MonteCarlo([v0], 100)

    # If we create a TestProgram object, we can add a description
    # and the plots will use it.
    prog = TestProgram('./mc_prog.py', desc='Montecarlo Uniform Test')

    # Create a Sweep object
    return Sweep(uq, host, prog)
