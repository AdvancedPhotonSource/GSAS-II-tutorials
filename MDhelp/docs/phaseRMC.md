<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="Phase-RMC"></a>
# **RMC** phase tab

This tab is used for access to three different programs, [RMCProfile](#rmcprofile), [fullrmc](#fullrmc) and [PDFfit](#pdffit),
that are used for fitting structural models to pair distribution functions (PDF).
RMCProfile and fullrmc are "big box" modelling routines and PDFfit is a "small box" modelling routine. 
Select the program you wish to use from radio button at the top of the window. Three
different windows are displayed depending on that selection. 

[Tutorials](https://advancedphotonsource.github.io/GSAS-II-tutorials/tutorials.html) for using RMCProfile and PDFfit can be accessed from the Tutorials menu item in the GSAS-II Help menu. These routines all run as stand-alone applications which are initiated by GSAS-II. When finished, GSAS-II processes their output files to update parameters that are within the GSAS-II project. The two big box routines can have very long running times; they run as separate console programs. GSAS-II is active while they are running and can "interrogate" them for intermediate results. PDFfit has a short running time and GSAS-II is "locked out" until it finishes; its result can be examined after.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

**Operations** Menu –

   * **Setup RMC** – this builds the input files and python script (if needed) for running the selected PDF modeling program.
   * **Execute** – this executes the chosen program in a new console which will vanish when finishes (after a "press any key" command). When finished, GSAS-II will extract results and place them in appropriate places in the project.
   * **Stop run** – only valid for fullrmc; stops the RMC run & saves progress so it can be continued later.
   * **Plot** – this displays the resulting graphical output from the PDF modeling run. For RMCProfile and fullrmc this can be 5 or more plots, for PDFfit it is only the observed and calculated G(r) plot with a difference curve.

For each program, the setup page is similar. There is a block for "metadata" items for your convenience; they have no impact on the calculations. Next is timing controls for the big box programs (PDFfit has none). Then is structural information and finally the data section for the patterns to be fitted. The big box programs are for only single runs while PDFfit can be used to process a sequence of G(r) data collected as a function of, e.g., temperature (giving Sequential PDFfit2 results).

<a name="fullrmc"></a>
### fullrmc

The fullrmc program is a large-box pair distribution function modeling library developed by Bachir Aoun [Fullrmc, a Rigid Body Reverse Monte Carlo Modeling Package Enabled with Machine Learning and Artificial Intelligence", B. Aoun, Jour. Comp. Chem. (2016), 37, 1102-1111. [DOI: 10.1002/jcc.24304](https://doi.org/10.1002/jcc.24304)]. Extensive information about fullrmc is found, including a number of explanatory videos, along with older source code on GitHub: [https://bachiraoun.github.io/fullrmc/](https://bachiraoun.github.io/fullrmc/). Note that the GSAS-II implementation is not compatible with the open-source version of fullrmc, but rather the new version 5.0 must be used, which is distributed as a compiled versions for 64-bit Intel-compatible processors running Windows, Linux and MacOS from website [https://github.com/bachiraoun/fullrmc/tree/master/standalones](https://github.com/bachiraoun/fullrmc/tree/master/standalones). Note that an even newer and more powerful version of fullrmc is available for cloud computing by subscription at [https://fullrmc.com](https://fullrmc.com). 

When fullrmc is selected in this tab, GSAS-II will locate an executable for fullrmc using the [GSAS-II configuration variable](./others.md#config)  `fullrmc_exec`, which if defined points to a Python image with fullrmc. Otherwise GSAS-II will look in the following places, in the order specified, for a Python image for a file named `fullrmc5*64bit` (MacOS or Linux) or `fullrmc5*.exe` (Windows):

1. The location where GSAS-II is installed,
2. The location where Python is installed,
3. The location where the GSAS-II binaries are found,
4. the current default location
5. and all directories in the system path. 

<a name="rmcprofile"></a>
### RMCProfile
The [RMCProfile program](http://rmcprofile.org/) fits large-box atomic models to x-ray & neutron PDF and S(Q) "data" as well as other types of observations. 
When RMCProfile is selected in this tab, GSAS-II will see if an RMCProfile
executable can located using the [GSAS-II configuration variable](./others.md#config)  `rmcprofile_exec`, which if defined should have the name of the RMCProfile program. If that is not defined, the following locations are searched:

1. The location where GSAS-II is installed,
2. The location where Python is installed,
3. The location where the GSAS-II binaries are found,
4. the current default location
5. and all directories in the system path. 

<a name="pdffit"></a>
### PDFfit2
The [PDFfit2](https://www.diffpy.org/diffpy.pdffit2/) program fits small-box atomic models to x-ray & neutron PDFs.
When PDFfitis selected in this tab, GSAS-II will see if PDFfit2 can be loaded as a package in the current Python installation (use of PDFfit2 in this manner is not recommended as this invites conflicts in the packages used by GSAS-II and PDFfit2) if that fails, GSAS-II will attempt to use a Python executable for PDFfit2 using the [GSAS-II configuration variable](./others.md#config)  `pdffit_exec`, which if defined points to a Python image with PDFfit2fullrmc. Optionally, if the Python installation used with GSAS-II uses conda (which is the case for the [gsas2main installer](https://advancedphotonsource.github.io/GSAS-II-tutorials/install.html#gsas2main-installer)), GSAS-II can download and install a separate conda environment with PDFfit2 installed. 
