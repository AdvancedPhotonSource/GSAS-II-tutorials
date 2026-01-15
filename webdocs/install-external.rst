Installing Externally-developed Software
----------------------------------------------------------------------------

There are several publicly-available programs where GSAS-II provides an interface, but the software authors understandably would prefer that their software be downloaded by users directly from the authors' web sites, rather than be distributed as part of GSAS-II. Details on the installation of these optional programs is discussed below. Note that all are optional. Many users will not use any of them and it would be uncommon that anyone to use all of them.

**Dysnomia**
======================
  
    Computes enhanced Fourier maps with Maximum Entropy estimated
    extension of the reflection sphere. 
    
    The appropriate zip/dmg/tar file must be downloaded from
    https://jp-minerals.org/dysnomia/en/
    and the directory Dysnomia from that download must be placed
    in one of the following locations:
    
      * the user's home directory (``~/.``),
      * the directory ``~/.GSASII`` or
      * the ``GSASII`` directory where GSAS-II has been installed
        (this will be where the GSAS-II Python files are found).
        
    For Windows the home directory, ``~``, is usually
    taken from the USERPROFILE setting or a combination of HOMEPATH
    and HOMEDRIVE, so these directories will usually have form 
    ``C:\Users\``*YourUsername* or
    ``C:\Users\``*YourUsername*``\.GSASII``. 

**RMCProfile**
======================
  
    Provides large-box PDF & S(Q) fitting. The GSAS-II interface was originally
    written for use with release 6.7.7 of RMCProfile, but updates have
    been made for compatible with 6.7.9 as well.
    RMCProfile must be downloaded by the user from
    http://rmcprofile.org/Downloads or
    https://rmcprofile.pages.ornl.gov/nav_pages/download/

**fullrmc**
======================
  
    A modern software framework for large-box PDF & S(Q) fitting. Note
    that the GSAS-II implementation is not compatible with the last
    open-source version of fullrmc, but rather the version 5.0 must be
    used, which is distributed only as compiled versions and only for 64-bit
    Intel-compatible processors running Windows, Linux and
    MacOS. Download this as a single executable from website
    https://github.com/bachiraoun/fullrmc/tree/master/standalones. GSAS-II
    will offer to install this software into the binary directory when the fullrmc
    option is selected on the Phase/RMC tab.

**PDFfit2**
======================
  
    For small-box fitting of PDFs; see
    https://github.com/diffpy/diffpy.pdffit2?tab=readme-ov-file#-diffpypdffit2.
    This software is no longer developed, but it is
    being maintained with respect to new Python versions.

    The PDFfit2 developers recommend installing via conda, but
    it appears that pip installation is also possible. See
    https://pypi.org/project/diffpy.pdffit2/ for more information.
    It is possible to install PDFfit2 into the same
    conda environment that GSAS-II uses and if that is done, GSAS-II
    will use the package, but it is probably best to use a separate
    Python environment for PDFfit2, so that there is no possibility for
    conflict between package versions. When GSAS-II is run from a
    Python installation that includes the conda package manager (which
    is the case with the GSAS2MAIN installer), the GUI will offer an option to
    install PDFfit2 via a separate environment when the
    PDFfit2 option is selected on the Phase/RMC tab.
