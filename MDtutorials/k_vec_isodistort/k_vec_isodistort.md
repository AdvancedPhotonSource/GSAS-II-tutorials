---
title: Use the k-vector searched with GSAS-II to talk to ISODISTORT
---
<!--- Don't change the HTML version of this file; edit the .md version -->

* Exercise files are found [here](data/index.html)

<a name=Intro></a>

## Intro

When the symmetry of a system is lowering through a group-subgroup pathway while going through a phase transition, one can try to use the emerging satellite peaks in the diffraction pattern to search for a k-vector that best explains the satellite peak positions. Refer to the two tutorials regarding the k-vector search in GSAS-II, [here](https://advancedphotonsource.github.io/GSAS-II-tutorials/k_vec_tutorial/k_vec_tutorial.html) and [here](https://advancedphotonsource.github.io/GSAS-II-tutorials/k_vec_tutorial_non_zero/k_vec_tutorial_non_zero.html). Once we obtain the alternative k-vector, we can move forward to use the k-vector to talk to ISODISTORT to search for all the isotropic subgroups that are compatible with the k-vector. It covers all the irreducible representations (IRs) compatible with the k-vector and the order parameters associated with each IR. An exhaustive refinement can then be performed for each of the candidate subgroup against the experimental diffraction data of the low symmetry phase. In this tutorial, we will demonstrate how to use the implementation in GSAS-II regarding this. Going through the steps to be presented here, we are expecting a series of GSAS-II project file, each for a specific subgroup candidate.

For the demonstration purpose, here we are using the SrTiO${}_3$ structure as the parent and an arbitrarily generated subgroup (space group: $P4/mmm$) with a k-vector of (0, 1/2, 0). We simulated the powder diffraction data for both, with a typical instrument parameter file from the POWGEN diffractometer at SNS, ORNL. We will then use the simulated data to conduct a 'reverse engineering'. Namely, we can fit the simulated data from the subgroup with the parent phase and from there, we can use the residual peaks to extract the k-vector candidate and for a selected k-vector, we can construct GSAS-II project files for each of the subgroup candidate. We will `not` perform the exhaustive refinement for all the generated project files, though. `In the future, we can think about creating a wrapper script to run through all the generated candidate subgroups in a programmable manner.`

Here below is shown the two structures used in this tutorial -- (left) the parent STO structure and (right) the arbitrarily generated subgroup structure.

<img src="./imgs/structures.png" alt="order parameter plot" style="width:500px;">

## Data Simulation

For the data simulation with a CIF file, for sure we can use GSAS-II to do it. But here we want to showcase a convenient web-based tool for such a purpose. In fact, the backend calculation engine is still using GSAS-II, it is just that we will be doing this through an easy-accessible web interface. First, download the two structure files we include in the tutorial, `STO_Parent.cif` and `STO_Subgroup.cif`, together with the instrument parameter file we will be using for the simulation `powgen_profile_lwf.instprm`. Then go to the website, [https://addie.ornl.gov/simulatingpowder](https://addie.ornl.gov/simulatingpowder) (or, go to [https://addie.ornl.gov](https://addie.ornl.gov), then `Scattering Tools` => `SimulatePowder`). The interface looks like the figure to the right.

![ADDIE Powder Diff Simulation](imgs/addie_simu.png)

There we can upload the CIF file and the instrument parameter file to use for the simulation and click on the `Submit` button. One can notice that we have a dropdown selection menu there in the interface from which we can select one of the pre-included instruments such as NOMAD and POWGEN at SNS, ORNL and HB-2A (Powder) and HB-2C (WAND^2), HFIR, ORNL. One can also select the scatterer type and put in some optional parameters (follow the link there to see what options we can put in). The resulted here will be like the figure to the right.

![ADDIE Powder Diff Simulation Result](imgs/addie_simu_result.png)

We can download the simulated powder diffraction data by clicking on the `Datafile Download` button on top of the time-of-flight (TOF) result presented at the very top. Data in $d$ and $Q$ space are also presented but we do not need them here. We can do this for both CIF files provided here and if we do not change the CIF file names (`STO_Parent.cif` and `STO_Subgroup.cif`), we will obtain the following two simulated powder diffraction patterns, `STO_Parent_neutron_powder_calc.txt` and `STO_Subgroup_neutron_powder_calc.txt`, for the parent and subgroup phase, respectively. We will use these two simulated data files for the next part of the tutorial. Before that, if we want to have a quick comparison between the two datasets, we can go to [https://addie.ornl.gov/plotter](https://addie.ornl.gov/plotter), select the `Multiple Files Mode` and upload the two data files for a quick comparison plot. Here to the right is presented a demo for the tool.

![ADDIE Data Plotter](imgs/addie_plotter.gif)

## Refinement of the Subgroup Data with the Parent Phase

Since we are dealing with the simulated data so here we are not going to refine the parent data with the parent phase since that will be trivial and we are expecting a 'perfect' refinement. To start, we load in the subgroup simulated data and refine it with the parent phase, pretending that we don't know the subgroup structure. First, launch the GSAS-II GUI,

## Authors

| | 
| ---: |
| Yuanpeng Zhang |
| September 25, 2025 |
