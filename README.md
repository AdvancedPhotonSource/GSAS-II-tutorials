# GSAS-II Web Content

## Description
This repository contains files used to create GSAS-II web content, which includes installation/orientation information for users, as well as the GSAS-II tutorials, which are the primary form of documentation for how to use GSAS-II. 

## URLs
* **Home Page**: The GSAS-II home page [is here](https://advancedphotonsource.github.io/GSAS-II-tutorials/index.html), built from files in the [webdocs](https://github.com/AdvancedPhotonSource/GSAS-II-tutorials/tree/main/webdocs) directory of this repo. 

* **Tutorials**: When the tutorials will be run, It is best to access them from within GSAS-II using the Help->Tutorials menu (this will simplifies downloading the files needed to run the tutorials), but tutorials can also be accessed [from this link](https://advancedphotonsource.github.io/GSAS-II-tutorials/tutorials.html). The HTML, images and data files for the tutorials are found in this repo. Note that when new functionality is added to GSAS-II, it is customary to create a new tutorial. 

* **Help Pages**: There are three HTML web pages used within GSAS-II (plus a table of contents page) for context-sensitive help. These files are maintained in the [GSAS-II source code repo](https://github.com/AdvancedPhotonSource/GSAS-II/tree/master/GSASII/help), but for convenience, [they can also be accessed from the web pages](https://advancedphotonsource.github.io/GSAS-II-tutorials/help/gsasII-index.html).

## Repo Organization
Each tutorial is placed here in its own subdirectory. In that subdirectory, there will be a web page for that tutorial (extension .html or .htm) and two additional subdirectories, one named `data`, with the input file(s) needed for that tutorial and another with a name generated from the web page file name that contains images for the web page. 

In addition, there are a few special directories: 

* **docs**: The docs directory contains documentation for externally generated codes, such as
DIFFaX, NIST*LATTICE and PDFfit2.

* **scripts**: The scripts directory contains a script (`makeGitTutorial.py`) used to build the [tutorials table of contents page](https://advancedphotonsource.github.io/GSAS-II-tutorials/tutorials.html). Note that when a new tutorial is created, in addition to placing that in a new directory here, it needs to be added to the tutorials list, found in file [tutorialsIndex.py](https://github.com/AdvancedPhotonSource/GSAS-II/blob/master/GSASII/tutorialsIndex.py). This is used to display tutorials when the Tutorials menu commands is used and by `makeGitTutorial.py` as part of the "Build web documentation" GitHub Action. Note that this should probably be run manually as well to check in an updated .html file to git. 

* **webdocs**: Contains RestructuredText (.rst) files, used to produce the GSAS-II home page, installation instructions and related web content. 
