# GSAS-II data tree overview

GSAS-II creates projects that are saved in `.gpx` files. The GSAS-II data tree, which is shown on the left side of the main GSAS-II window shows a hierarchical index to the contents of a project. This index will usually have all of the entries listed below on the [Universal Data Tree Items](./commontreeitems.md) page, which are found in all types of GSAS-II projects and will also have at least one entry representing some sort of experimental data (or simulation) -- called a histogram -- and will likely have one or more phase entries. 

When you click on an entry in the data tree, the right side of the GUI will show the associated information with that section of the .gpx file, you may have access to additional menu commands and visualization information related to the selected data tree item may be shown in the [GSAS-II Graphics Window](./applicationwindow.md#Plots). 

Most of the subsequent sections of the GSAS-II help documentation describe: what the values shown in the GUI mean and what actions can be performed using the GUI, the menu commands and actions available for each type of data tree item, as well as any graphics that will be displayed and actions that can be performed graphically. 

Note that there is no limit to the number of phase and histogram entries that may be placed a project file, beyond that the computer being used must have enough memory to hold this information. Also, histogram and phase entries in project need not be utilized. Every phase can be linked to a histogram. (A single-crystal dataset can only be linked to one phase, but a powder diffraction dataset can be linked to any number of phases.) A phase that is not linked to a histogram is not used in refinements. Likewise, a histogram that is not linked to a phase is also not used. 

