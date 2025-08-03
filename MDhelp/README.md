This directory contains the files used to generate the GSAS-II help
files, which are on the web at
https://advancedphotonsource.github.io/GSAS-II-tutorials/help/ and are
placed into the GSAS-II source code (at
https://github.com/AdvancedPhotonSource/GSAS-II/tree/main/GSASII/help) 

To view the pages as they are being edited use this command inside
this directory::

    mkdocs serve
    
and then open the address that is shown in a web browser. Web pages
are rebuilt after any file is saved. 

Note that this requires the following packages: mkdocs,
          mkdocs-material, python-markdown-math, mkdocs-static-i18n, 
          mkdocs-to-pdf, & pymdown-extensions. All are available with
          pip. At least some with conda. Producing a .pdf also requires
          Google chrome or chromium. 
