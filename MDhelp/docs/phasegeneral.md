<a name="Phase-General"></a>
<a name="General"></a>
# **General** phase tab

This section of the phase information provides overall parameters describing the phase such as: the phase's name, space group, the unit cell parameters and overall parameters for the atom types present in the phase. It also has the controls for Pawley intensity extraction and for computing Fourier maps for this phase. It can also has the controls for Monte Carlo/Simulated Annealing for solving structures with flexible rigid molecular bodies.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. Menu '**Compute**' – The compute menu shows computations that are possible for this phase.

    **Fourier map**
    :    Compute Fourier maps according to the controls set at bottom of General page. 

    **Search map**
    :    Search the computed Fourier map. Peaks that are above 'Peak cutoff' % of the maximum will be found in this procedure; they will be printed on the console and will be shown in the ["Map peaks'](#TBD) page. This page will immediately be shown, and the peaks will be shown on the structure drawing for this phase as white 3-D crosses. 

    **Charge flipping**
    :    Performs a charge flipping *ab initio* structure solution using the method of Oszlanyi & Suto (Acta Cryst. **A60**, 134-141, 2004). You will need to select a source for the reflection set and perhaps select an element for normalization by its form factor, a resolution limit (usually 0.5Å) and a charge flip threshold (usually 0.1); these are found near the bottom of the General window. There are also Test HKLs to show the progress in phasing with charge flipping cycles. They show the generally chaotic phase behavior before a solution is found; after that the phases are essentially fixed. No use is made of this information; it is just for your edification. A progress bar showing the charge flip residual is shown while the charge flip is in operation. When the residual is no longer decreasing (be patient – it doesn't necessarily fall continuously), press the Cancel button to stop the charge flipping, otherwise it will stop at 10,000 cycles. The resulting map will be positioned to properly place symmetry operators (N.B.: depends on the quality of the resulting phases; the map could be still offset by a few steps), searched for peaks and the display shifts to Map peaks to show them. 

    **4D Charge flipping**
    :   4-Dimensional charge flipping is done for a modulated structure. Only available for phases with a 3+1 superspace group. 

    **Clear map**
    :   This clears any Fourier/charge flip map from the project; the Fourier map controls are also cleared. 

    **MC/SA**
    :    Perform Monte Carlo/Simulated Annealing structure solution using the model as set up in the MC/SA tab and the controls at the bottom of this tab. 

    **Multi MC/SA**
    :    Perform multiple Monte Carlo/Simulated Annealing structure solutions, accumulating the best ones as set up in the MC/SA tab. 

    **Transform**
    :    This allows for a change in axes, symmetry or unit cell. It is also used to create a magnetic phase from a chemical (nuclear) phase. One important transformation that can be done here is for Origin 1 settings to Origin 2 ([see more extensive elsewhere](./others.md#Origin_1)). 

    **Compare Cells**
    :    Compares two supplied unit cells for a transformation matrix that converts one to the other within supplied search tolerances using the NIST*LATTICE program. If this is used, please cite:
        
    : * V. L. Karen and A. D. Mighell, NIST Technical Note 1290 (1991). ([link](https://nvlpubs.nist.gov/nistpubs/Legacy/TN/nbstechnicalnote1290.pdf))
        * V. L. Karen & A. D. Mighell, U.S. Patent 5,235,523. ([link](https://patents.google.com/patent/US5235523A/en?oq=5235523))

    **Compare polyhedra**
    :    Compares idealized polyhedra (tetrahedron & octahedron) to those obtained from a Reverse Monte Carlo run in RMCProfile. 

    **Select magnetic/subgroup phase**
    :    Selection of the results from a magnetic subgroup analysis done in the [PWDR/Unit cells list](#TBD) data tree item. This will generate a new magnetic phase. Can also be used to select from possible subgroups of a nonmagnetic super group for possible symmetry reduction. See the 
[PWDR/Unit cells list description](#TBD) for further information. 

    **Protein quality**
    :    Evaluate protein quality by Python versions of `errat` & `errat2` codes by Colovos, C. & Yeates, T.O. Protein Science **2**, 1511-1519 (1991). 

The items in the upper part of the General page that can be changed are Phase name, Phase type, Space group, unit cell parameters & refine flag. These are described in turn:

* **Phase name** – this is the name assigned to this phase. It can be changed at any time.
* **Phase type** – this can only be set when there are no atoms in the Atoms page for this phase. Select it when the phase is initialized.
* **Space group** – this is usually set when the phase is initialized, but it can be changed later. Be careful about the impact on Atom site symmetry and multiplicity if you do. The choice of space group will set which unit cell parameters are displayed in this window. 

    GSAS-II will recognize any legal space group symbol using the short Hermann-Mauguin forms, provided whitespace is placed between the axial fields (e.g. "F d 3 m" not "Fd3m", but note that "F d -3 m" is interpreted the same as "F d 3 m". Standard Space groups will also be recognized without spaces, but non-standard ones will not.
    
    For space groups where there is a choice of origin (e.g. F d 3 m), GSAS-II always uses the 2nd setting, the one where the center of inversion is located at the origin
([see more extensive elsewhere](./others.md#Origin_1)). 

* **Refine unit cell** – set this flag to refine the unit cell parameters in a Rietveld or Pawley refinement. The actual parameters refined are the symmetry allowed terms (A0-A5) in the expression 
$$ d^{*2} = A_0h^2 + A_1 k^2 + A_2 l^2 + A_3 hk + A_4 hl + A_5 kl $$ 
where \(A_0 - A_5\) correspond to elements in the reciprocal metric tensor element (**G**) where off-diagonal contributions are doubled, A0-A5 = \(G_{11}\), \(G_{22}\), \(G_{33}\), \(2 *  G_{12}\), \(2 *  G_{13}\), \(2 *  G_{23}\)

* **a, b, c, alpha, beta, gamma** – lattice parameters; only those permitted by the space group are shown. The volume is computed from the values entered.

If there are entries in the Atoms tab, then the Elements table is shown below on the General tab; you may select the isotope (only relevant for neutron diffraction experiments). The density (just above the Elements) is computed depending on this choice, the unit cell volume and the atom fractions/site multiplicities in the entries on the Atoms page.

Next are the Pawley controls.

* **Do Pawley refinement?** – This must be chosen to perform a Pawley refinement as opposed to a Rietveld refinement for this phase. NB: you should clear the Histogram scale factor refinement flag (found in [Sample parameters](#TBD) for the powder data -- PWDR histogram) as it cannot be refined simultaneously with the Pawley reflection intensities.
* **Pawley dmin** – This is the minimum d-spacing to be used in a Pawley refinement. NB: be sure to set this to match the minimum d-spacing indicated by the powder pattern limits (see Limits for the powder data set).
* **Pawley dmax** – This is the maximum d-spacing for reflections in a Pawley refinement. It is usually defined by the beginning of the data collection scan and will thus remove reflections that have too large d-spacing to be seen in the scan.
* **Pawley neg. wt.** – This is the weight for a penalty function applied during a Pawley refinement on resulting negative intensities. Use with caution; initially try very small values (e.g. .01). A value of zero means no penalty is applied.

Fourier map controls are shown next on the General page. Single crystal data or a completed Rietveld or Pawley refinement is required before a Fourier map can be computed. Select the desired type of map, the source of the reflection set and the map resolution desired. The peak cutoff is defined as a percentage of the maximum and defines the lowest level considered in the peak search.

Charge flip controls are below the Fourier map controls.

* **Reflection sets** – This is the source of structure factors to be used in a charge flip calculation. These may be either a single crystal data set, or structure factors extracted from a powder pattern via a Pawley or LeBail refinement or a Rietveld refinement.
* **Normalizing element** – This is an element form factor chosen to normalize the structure factors before charge flipping. None (the default) can be selected from the lower right of the Periodic Table display shown when this is selected.
* **Map grid step** – This is the step size of the charge flip map; default is 0.25Å. The set of reflections is expanded to a full sphere and zero filled to 2X this value; this suite of reflections is then used for charge flipping.
* **k-Factor** – This is the threshold on the density map, all densities below this are charge flipped.
* **k-Max** – This is an upper threshold on the density map; all densities above this are charge flipped. In this way the "uranium solution" problem is avoided. Use k-Max = 10-12 for equal atom problems and larger for heavy atom ones (typically 2X largest atom number).
* **Test HKLs** – plot of phases for selected hkls are shown at end of charge flipping run. Just for you to look at.

Monte Carlo/Simulated Annealing controls are at the bottom of the window.

* **Reflection set from** – This is the source of structure factors to be used in a charge flip calculation. These may be either a single crystal data set, or structure factors extracted from a powder pattern via a Pawley or Lebail refinement or a Rietveld refinement.
* **d-min** - This restricts the set of reflections to be used in the MC/SA run. Suggest using no lower than 2.0.
* **MC/SA runs** – pulldown with selection of number of trials to be done.
* **MC/SA Refine** – requires a refinement of parameters over range about each test position.
* **MC/SA schedule** – This selects the schedule for the "temperature" to be used during MC/SA run. For 'fast' and 'log', coefficients control details of schedule; a plot shows the scheduled temperatures for the set of steps.
* **Annealing schedule** – This selects the beginning MC/SA "temperature", final "temperature", and number of trials at each step.

