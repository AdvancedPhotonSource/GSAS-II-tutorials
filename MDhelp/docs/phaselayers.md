<a name="Phase-Layers"></a>
# **Layers** phase tab

This is used to set up stacking fault models for simulations of x-ray diffraction patterns. See for example the [Diamond stacking faults tutorial](https://advancedphotonsource.github.io/GSAS-II-tutorials/StackingFaults-I/Stacking%20Faults-I.htm). The computations are done by a modified version of DIFFaX. See M.M.J. Treacy, J.M. Newsam and M.W. Deem, Proc. Roy. Soc. Lond. **433A**, 499-520 (1991) for more information on DIFFaX and please cite this if you use this section of GSAS-II.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. Menu '**Operations**' –

    * **Load from DIFFaX file** – load parameters from a DIFFaX input file
    * **Copy phase cell** – copy the lattice parameters from a selected phase (usually transformed from average unit cell)
    * **Simulate pattern** – run DIFFaX to simulate selected pattern
    * **Fit pattern** – refine stacking fault parameters to fit observed pattern (not available yet)
    * **Sequence simulations** – do a sequence of simulations incrementing a selected stacking fault parameter

2. Show a plot of the 2D diffraction pattern for the stacking model – look for streaks.
3. Select Laue symmetry
4. Reference unit cell – filled by Copy phase cell and is the stacking fault block dimensions (NB: refine inactive)
5. Layer width (a & b) – outer dimensions of crystallite; used for broadening calculations (NB: refine inactive)
6. Next are descriptions of the layers to be used in the calculations. They can be created atom-by-atom or imported from another GSAS-II gpx file. If a layer is already present, then the new layer can be the same; give it a different name.
7. The layers stack according to probability rules – these are presented in tables in the next section
8. You can specify specific layering sequences as a sequence of layer numbers (begins with 1).
9. Finally, you can set the type of sequence and the number of layers to use in the simulation

You can draw the layer structures as well as sequences of layers to check on how they fit together; see the Plot boxes for this.
