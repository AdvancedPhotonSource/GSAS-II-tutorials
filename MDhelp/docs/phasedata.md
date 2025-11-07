<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="Phase-Data"></a>
<a name="_Data"></a>
# **Data** phase tab

This data tab serves several purposes. It is used to link histograms to the selected phase, and it allows the values and refinement flags to be set for the parameters that are defined for each histogram-phase pair, labeled as HAP parameters. [Note that some GSAS-II parameters are defined for each phase (atomic positions, for example), other parameters are defined for each histogram (scale factors and instrumental constants, for example) but the HAP parameters have values for each histogram in each phase.] 

The HAP parameters include: 

* the phase fraction; 
* the sample contributions to peak broadening: microstrain and crystallite size; 
* a LeBail intensity extraction flag; 
* hydrostatic/elastic strain shifts to lattice parameters; 
* corrections to peak intensities due to experimental effects (preferred orientation, extinction and disordered solvents).
The data tab also implements graphical representation for some of these HAP parameter sets.

For single crystal data, the only parameters are scale, extinction and disordered solvent. There is no scale factor directly associated with the histogram.

* **Use flag** - When the Use flag is selected, the currently selected phase is included in the computation of intensities as a contribution to the selected histogram (single-crystal histograms can have only one phase; powder histograms can have any number of associated phases). When not set, the phase is not included in the selected histogram, as if it the phase and histogram had not been linked. Changing the use flag is much easier that linking and unlinking phases and histograms. 

* **Start LeBail extraction** - When this is selected, intensities are set to values that are best fit using the LeBail intensity determination method rather than are computed from the atomic information for the phase. Cycling this setting will reset LeBail extracted intensities to their default (\(F^2\) = 100).

* **Phase fraction** - Used in powder histograms: a multiplier that determines the relative amount of the selected phase to a histogram. It is proportional the number of unit cells of the phase in the sample. The number is assumed to be on an arbitrary scale; the values are mass normalized to compute phase mass (weight) fractions. 

    Note that when the histogram scale factor is varied, these values are on a relative scale. Conventional practice is to vary the scale factor and to not vary the phase fraction for one phase in a histogram, but also common is to fix the histogram scale factor and refine all phase fractions. Do not refine the scale factor and all phase fractions unless a constraint is defined so the phase fractions add to 1.
  
* **Scale factor** - Used for single crystal data: relates \(F^2_{obs}\) to \(F^2_{calc}\).

* **Crystallite size peak broadening** – 
Peaks can be broadened due to the finite size of crystallites or due to microstrain (see below). Microstrain is more common other than in nanoparticles. 
The broadening is computed from size factor(s) in microns (1 μm = \(10^{-6}\) m), with the Scherrer constant assumed as unity. Sizes can be computed with a choice of three models: isotropic, uniaxial and ellipsoidal. 
Typical sensitivity for crystallite size is to no more than 4 μm (less for lower resolution instruments); beyond that the particles are effectively infinite for a diffraction experiment.

    * In **isotropic** broadening, crystallites are assumed to average as uniform in all directions and a single size value is supplied; 
    * with **uniaxial** broadening, a preferred direction (as a crystallographic axis, such as (001) is supplied) -- note that for most crystal systems only one axis makes sense -- and two size parameters are defined, one for along the axis and one for in the perpendicular plane; 
    * with **ellipsoidal**, six terms are used to define a broadening tensor that has arbitrary orientation -- this model may require constraints and is seldom needed. 

    Note that size broadening is usually Lorentzian, which corresponds to a LGmix value of 1.0; if this value is between 0 and 1, both Gaussian and Lorentz size broadening is modeled and a value of 0.0 is pure Gaussian. Values less than 0 or greater than 1 make no physical sense. LGmix is not commonly refined.
    
* **Microstrain peak broadening**  - This is computed as unitless fraction of Δd/d (or equivalently ΔQ/Q) times \(10^6\). Typical microstrain is ~1000, but may be significantly higher in physically processed materials. Note that the term residual stress is sometimes used for microstrain, but residual stress can be computed from microstrain when the elastic strain constants are known. Microstrain was can be computed in GSAS-II via a choice of three models: isotropic, uniaxial and generalized: 
    * In **isotropic** broadening, microstrain broadening assumed to be the same in all crystallographic directions and a single value is supplied; 
    * with **uniaxial** broadening, a preferred direction (as a crystallographic axis, such as 0,0,1) is supplied -- note that for most crystal systems only one axis makes sense -- and two microstrain parameters are defined, one for along the axis and one for in the perpendicular plane; 
    * with **generalized**, the [Nicolae Popa](https://journals.iucr.org/j/issues/2020/06/00/es5029/index.html)/[Peter Stephens](https://journals.iucr.org/paper?hn0085) second-order expansion model is used and the number of terms will depend on the crystal system. It is typically possible to refine all terms when significant anisotropic strain broadening is present.
    
    Note that microstrain broadening is usually Lorentzian, which corresponds to a LGmix value of 1.0; if this value is between 0 and 1, both Gaussian and Lorentz size broadening is modeled and a value of 0.0 is pure Gaussian. Values less than 0 or greater than 1 make no physical sense. LGmix is not commonly refined.

* **Hydrostatic/elastic strain** – This shifts the lattice constants for the contribution of a phase into a histogram. These $D_{ij}$ values are added to the [reciprocal lattice parameter tensor terms](http://gsas-ii.readthedocs.io/en/latest/GSASIIutil.html#gsasiilattice-unit-cell-computations). They must be refined in sequential refinements or where the lattice constants are slightly different in different histograms (as an example, see the [Combined X-ray/CW-neutron refinement of \(\rm PbSO_4\) tutorial](https://advancedphotonsource.github.io/GSAS-II-tutorials/CWCombined/Combined%20refinement.htm)) or may account for changes to the lattice constants due to external stress (as occurs in a high-pressure measurement.) Note that *these values and the phase's lattice parameters (on the General tab) should not be refined at the same time*. When the values are non-zero, the lattice constants after application of these strain tensor terms is shown with these $D_{ij}$ values.

    For cubic material, an extra term, eA ($\epsilon_A$) with units of Å${}^{-2}$, is included that is particularly useful in high pressure work. This accounts for the shift of peaks due to macroscopic stress along the (111) directions:

    $$\Delta 2 \theta = - 180.*d^2 * \Delta D_{hkl, \epsilon_A}  * \tan(\theta) / \pi$$ 

    $$\Delta T = -{\rm difC} * d^2 * \Delta D_{hkl, \epsilon_A} /2.$$

    where $\Delta 2 \theta$ is in degrees and$\Delta T$ is TOF in $\mu$sec; $d$ is d-space (Å) and 

    $$\Delta D_{hkl, \epsilon_A} = \epsilon_A  {(hk)^2 +(hl)^2 +(kl)^2 \over (h^2 +k^2 +l^2)^2}$$


   <a name="Phase-Preferred_orientation"></a>
   <a name="Preferred_orientation"></a>
   <a name="preferred_orientation"></a>

* **Preferred Orientation** – Preferred orientation (texture) can be treated in one of two different sections of GSAS-II, either the Preferred Orientation correction here in the Data tab, or the "[Texture](phasetexture.md)" tab, depending on what is desired. 
The Preferred Orientation correction here is typically used for crystallographic studies, where intensity corrections are desired to repair for undesired texture in the sample, while the Texture tab is used for studies where the goal is to characterize preferred orientation in a sample.

    The preferred orientation correction, here in the Phase/Data tab, can apply one of two different types of intensity corrections. One is to apply a cylindrical (wire symmetry) spherical harmonics orientational distribution function and the other is a simpler,   single-parameter model, known as **March-Dollase**. Note either of these is applied to only a single histogram.
This is in contrast to the model applied in the Texture tab, where the corrections from a set of spherical harmonics terms will be applied to all histograms associated with the current phase appears. Note that multiple sample orientations or detector settings are usually needed to determine texture with symmetry lower than cylindrical. Typically, the Preferred Orientation correction here is used for crystallographic studies, where intensity corrections are desired to repair for undesired texture in the sample, while the Texture tab is used for studies where the goal is to characterize preferred orientation in a sample. Note that both the Preferred Orientation and Texture corrections should not be used at the same time.

    Use of the **March-Dollase** model requires a definition of a unique axis (as a reciprocal space vector) and then a single ratio can be refined, which specifies the relative amount of excess (value >1) or depleted (value <1) crystallites in that direction. Note that there is only one choice for the unique axis for many crystal systems, such as 001 for hexagonal and tetragonal. 
    
    The **Spherical Harmonics model** allows for a more complex probability surface (which is always constrained to match the symmetry of the crystal system and assumes a cylindrical symmetry sample.) An order parameter term is available which dictates how many terms are introduced into the model and thus the complexity of the probability surface. Note that use of this model requires that the correct value is used for Sample parameters. For the goniometer \(\chi\) (chi) setting be sure to use: 
    
    * \(\chi\) = 90.0 for Debye-Scherrer or 
    * \(\chi\) = 0.0 for Bragg-Brentano.

    A measure of fit quality can be made by plotting the Preferred Orientation for different reflections. (Use the selection box at the at the top right to cause this to be displayed.) The MRD (multiples of random distribution) term will be 1 everywhere for a random (texture-free) sample. A value that is significantly below zero is not physically possible and indicates overfitting. The amount of the correction that has been applied to each reflection for a phase in a histogram is shown in the `Prfo` column of the "Reflection Lists" table. This should also be positive for every reflection.

* **Extinction** – This can occur when crystals/crystallites have minimal mosaic character, which results in lowering of diffraction intensities for the most intense reflections. This is not commonly seen in CW powder diffraction, but can be more apparent in neutron TOF data. For single crystal data the extinction model is more complex allowing for primary and two types of secondary extinction.

* **Disordered solvent**; Babinet A & B - This correction, using the Babinet model, is typically used to treat scattering from solvent that is not well-ordered in protein structures. It probably makes no sense in most any other application.

* **Merohedral twins** - Used for single crystal data; gives twin law transformation matrix and fraction for each twin member. These are for merohedral twins where the observed structure factors are a composite of contributions from each twin. Twin fractions are automatically constrained to sum to unity.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

* In this tab, menu items allow copying values or refinement flags to histograms/phases and selection of which histograms are used in the current phase.
* The plot selection items allow for three dimensional representations of the microstrain or crystallite size distributions (which are spheres for isotropic treatments); preferred orientation can be plotted as a Psi scan (a plot of relative crystallite abundance for a particular reflection as a function of azimuthal angle) or as an inverse pole figure (which shows a stereographic projection of the probability distribution for different reciprocal lattice directions as viewed down the sample cylinder axis). For no texture/preferred orientation this figure would be flat = 1.0.

