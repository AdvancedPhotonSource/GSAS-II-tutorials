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

Since we are dealing with the simulated data, here we are not going to refine the parent data with the parent phase since that will be trivial and we are expecting a 'perfect' refinement. To start, we load in the subgroup simulated data and refine it with the parent phase, pretending that we don't know the subgroup structure. First, launch the GSAS-II GUI, and then proceed to the menu item `Import` => `Powder Data` => `from Topas xyz/qye or 2th Fit2D chi/qchi file`, followed by browsing files and selecting the simulated data from previous step, namely `STO_Subgroup_neutron_powder_calc.txt`. If `ADDIE` interface was used previously for simulating the data, the downloaded simulated data will be ending with `.txt`. In this case, we have to select `any file (*.*)` from the file type dropdown selection while trying to find the previously saved simulated data. Once the data is selected, we want to click on `Yes` when prompted with the window to confirm the selection. Automatically, this will be followed by GSAS-II letting us to select the instrument parameter file. Here, we want to select exactly the one that was used above for the data simulation, i.e., `powgen_profile_lwf.instprm`. By default, GSAS-II assumes `GSAS iparm file (*.prm, *.inst, *.ins)`. Therefore, here we want to select `GSAS-II iparm file (*.instprm)` from the file type dropdown selection so that we can select the instrument parameter file `powgen_profile_lwf.instprm` to use.

Next, proceed to the menu item `Import` => `Phase` => `from CIF file` and select the parent structure CIF file, `STO_Parent.cif`. Click `Yes` to confirm the selection when prompted. When asked, we want to give the phase a name -- here I am using `STO_parent`. GSAS-II will then let us select which histogram to attach the phase to -- here we only have one histogram and that is for sure the one we want to select. Just check the box in front of the histogram in the prompted window and click on `OK`. Without any other settings, let's just go ahead with the refinement -- go the menu `Calculate` => `Refine`. If we haven't saved the project yet, we will be asked to first save the project before proceeding and we can give the project a name like `test_subgroup_data_with_parent_structure.gpx` (we don't have to give the extension explicitly). Since we are dealing with the simulated data here, even though we are fitting the data simulated from the subgroup structure with the parent phase, we are still getting a very small Rwp (0.031%). However, if we zoom in the plot, we will see some peaks are not indexed by the parent structure, as seen to the right.

![Unindexed peaks by the parent structure](imgs/missing_peaks.png)

We will first pick up those extra peaks visually and perform the k-vector search. For more details about the k-vector search capability in GSAS-II, please refer to the tutorial [here](https://advancedphotonsource.github.io/GSAS-II-tutorials/k_vec_tutorial/k_vec_tutorial.html) and [here](https://advancedphotonsource.github.io/GSAS-II-tutorials/k_vec_tutorial_non_zero/k_vec_tutorial_non_zero.html). Here, we go to `Peak List` in the tree item (as one of the sub-items for the histogram tree item), and then go to the menu item `Peak Fitting` and enable `Add impurity/subgrp/magnetic peaks` (click on the item to see a check mark in front of the item text label). Then we go to the GSAS-II data plot window -- make sure the `Powder Patterns` tab is active. Following the previous steps, we now should be able to click on data points on the plot with the mouse to add in extra peaks. Here shown to the right are the peaks that I selected.

![Extra peaks selection for k-vector search](imgs/extra_peaks.png)

If by accident we select an extra peak unintentionally, we can remove it by right clicking on the extra peak that we want to remove. Or we can drag the extra peak to the position that we want it to be. Once we make sure several of the extra peaks are accurately selected, we can proceed to the k-vector search. Go back to the GSAS-II main window, click on the `Unit Cells List` item under the histogram tree item and check the `Search for k-vector` box, as shown to the right,

![k-vector search](imgs/k_vec_search.png)

Here, let's keep all the inputs as default and click on `Start Search`. In a blinking moment, we should be able to see the searched k-vector candidate where the results will be listed according to how close the extra peaks as will be yielded from a certain k-vector candidate are to those selected extra peaks, from the top to the bottom. ***GSAS-II does not try to pin down those unique k-vector arms and quite often we would see equivalent k-vectors appearing in the search result, as we would see in this case shown to the right***.

![k-vector search result](imgs/k_vec_result_table.png)

By default, the candidate k-vector at the very top of table will be checked -- we can check whichever one in the table if needed and only one of them can be checked at a time. With a certain k-vector candidate checked, we can click on the `Call ISODISTORT` button to use the selected k-vector to talk to ISODISTORT for constructing an exhaustive list of subgroups that are compatible with the selected k-vector. For sure, we need internet connection at this step. Once the button is clicked, we will first need to confirm the citation of ISODISTORT before proceeding. Clicking on `OK`, GSAS-II will then do the job in the background. Here are several critical steps happening in the background,

- Upload the phase in GSAS-II to ISODISTORT

- Feed in the selected k-vector

- Go through the combination of IRREPs and order parameters and generate the corresponding subgroups, in an exhaustive manner

- Save the CIF for each generated subgroup

- Create and save a GSAS-II project file with the parent phase replaced by one candidate subgroup at a time

The processing will take some time, depending on the number of candidate subgroups compatible with the selected k-vector. In the test case here, we are having 19 candidate subgroups in total and we can see the `P4/mmm` space group in the list, which is indeed our ground truth. Next, we will have to load open each of the saved GSAS-II project files, perform the refinement and go from there to determine the answer that best explains the diffraction pattern. We are not going to do that here. In the future, we will be working on a script with which one can run through those candidate subgroups refinement in a scriptable manner.

## Authors

| | 
| ---: |
| Yuanpeng Zhang |
| October 14, 2025 |
