# GSAS-II Web Content

## Description
This repository contains the GSAS-II web content, which includes installation information for users, as well as tutorials that demonstrate how different functionality in GSAS-II works. 

## URLs
* **Home Page**: The GSAS-II home page [is here](https://advancedphotonsource.github.io/GSAS-II-tutorials/index.html), built from files in this repo. 

* **Tutorials**: It is best to access the tutorials from within GSAS-II using the Help->Tutorials menu (this will simplifies downloading the files needed to run the tutorials), but tutorials can also be accessed [from this link](https://advancedphotonsource.github.io/GSAS-II-tutorials/tutorials.html). The tutorials are also found in this repo.

* **Help Pages**: There are three HTML web pages used within GSAS-II for context-sensitive help. These files are stored in the [GSAS-II source code repo](https://github.com/AdvancedPhotonSource/GSAS-II), but for convenience, [they can also be accessed here](https://advancedphotonsource.github.io/GSAS-II-tutorials/help/gsasII-index.html).

## Repo Organization
Each tutorial is placed here in its own subdirectory. In that subdirectory, there will be a web page for that tutorial (extension .html or .htm) and two additional subdirectories, one named `data`, with the input file(s) needed for that tutorial and another with a name generated from the web page file name that contains images for the web page. 

In addition, there are a few special directories: 

### docs
The docs directory contains documentation for externally generated codes, such as
DIFFaX, NIST*LATTICE and PDFfit2.

### scripts
The scripts directory contains a script (makeGitTutorial.py) used to build the web page referenced above. 

### webdocs
Contains RestructuredText (.rst) files, used to produce the GSAS-II home page, installation instructions and related web content. 
