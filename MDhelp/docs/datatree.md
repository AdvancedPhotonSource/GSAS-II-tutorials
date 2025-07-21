<!--- Don't change the HTML version of this file; edit the .md version -->
# GSAS-II data tree overview

GSAS-II creates projects that are saved in `.gpx` files. The [GSAS-II Data Tree](./applicationwindow.md#Data_tree), which is shown on the left side of the main GSAS-II window shows a hierarchical index to the contents of a project. This index will usually have all of the entries listed below on the [Universal Data Tree Items](./commontreeitems.md) page, which are found in all types of GSAS-II projects and will also have at least one entry representing some sort of experimental data (or simulation) -- called a histogram -- and will likely have one or more phase entries. 

When you click on an entry in the [data tree](./applicationwindow.md#Data_tree), the right side of the GUI, the [GSAS-II Data Window](./applicationwindow.md#Data_frame)  will show the associated information with that section of the .gpx file, you may have access to additional menu commands and visualization information related to the selected data tree item may be shown in the [GSAS-II Graphics Window](./applicationwindow.md#Plots). 

Most of the subsequent sections of the GSAS-II help documentation describe: what the values shown in the GUI mean and what actions can be performed using the GUI, the menu commands and actions available for each type of data tree item, as well as any graphics that will be displayed and actions that can be performed graphically. 

## Data tree Histogram items

These constitute the data sets ("Histograms") to be used by GSAS-II for analysis. 
These are shown in the data tree as top-level entries with a prefix of:

 * [**PWDR**](./powder.md): Powder Diffraction data
 * [**HKLF**](./singlecrystal.md): Single Crystal data
 * [**PDF**](./pairdistribution.md): Pair Distribution Functions (derived from data)
 * [**IMG**](./image.md): 2D Diffraction Images
 * [**SASD**](./smallanglescattering.md): Small Angle data
 * [**REFD**](./reflectometry.md): Reflectometry data
 
The prefix in the entry is followed by a descriptive term or file name. Selection of these items may not produce much information in the [data window](./applicationwindow.md#Data_frame) but does visualize the data in the [graphics window](./applicationwindow.md#Plots). The histogram data items are described in subsequent sections of this help file. 

## Data tree Phase information

A [GSAS-II phase](./phaseoverview.md) is the description of a crystal structure, including unit cell parameters, symmetry and atom coordinates. Each phase is placed in the [data tree](./applicationwindow.md#Data_tree) as a child (subdata) tree entry in the phase. 

## Phase/Histogram Linking

Note that there is no limit to the number of phase and histogram entries that may be placed a project file, beyond that the computer being used must have enough memory to hold this information. Also, all the histogram and phase entries in project need not be utilized. Every phase can be linked to zero, one or more histograms. A single-crystal dataset can only be linked to one phase (or none), but a powder diffraction dataset can be linked to any number of phases, including zero. A phase that is not linked to a histogram is not used in refinements. Likewise, a histogram that is not linked to a phase is also not used. 
