.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right

.. index:: Home
	   
====================================
GSAS-II Home Page
====================================

.. toctree::
   :caption: Contents
   :maxdepth: 1
   :numbered:     
      
   install.rst
   documentation.rst
   mailinglist.rst
   bug.rst
   developers.rst 
   compile.rst
   install-pip.rst
   proxy.rst

Welcome to the home page for GSAS-II, a unique and comprehensive open
source Python project for determination of crystal structures and
diffraction-based materials characterization for crystalline solids on
all scales, from perovskites through proteins, using both powder and
single-crystal diffraction and with both x-ray and neutron
probes. Refinements can combine measurements from laboratory and
synchrotron x-rays, as well as constant wavelength or time-of-flight
neutron sources. It provides structure solution and refinement, as
well as extensive visualization capabilities. 

GSAS-II is made available for free use (`see license <https://raw.githubusercontent.com/AdvancedPhotonSource/GSAS-II/master/LICENSE>`_) with open access to the `source code <https://github.com/AdvancedPhotonSource/GSAS-II>`_.  

.. tip::
    Please help us by citing:

     .. index:: Citation
    
    Toby, B. H., & Von Dreele, R. B. (2013). "GSAS-II: the genesis of a modern open-source all purpose crystallography software package". *Journal of Applied Crystallography*, **46**\(2), 544-549. doi:10.1107/S0021889813003531

       Note that some sections of the program utilize externally provided
       codes or reference later work, with citations provided
       as they are used. *Please* cite them as well.
 
Also, please do sign up for the GSAS-II mailing list `see below <mailinglist.html>`_.
We add new features to GSAS-II quite frequently, so we may break
things from time to time (`see bug reporting <bug.html>`_). Be
sure to use the ``Help-->Update`` capability frequently to stay abreast of
new features and fixes as they are added and please make sure to use
the latest version before reporting a bug to us, but *please* do report
bugs.

Installation overview
=======================

There are several different ways to install GSAS-II, as are outlined below. Most people will use the GSAS2FULL installer
 
.. toctree::
   :caption: Installation information:
      
   install.rst

Available Documentation
====================================

While there is no manual for GSAS-II, there is quite a bit of
web-based documentation, as listed below.

.. toctree::
      
   documentation.rst

Help: GSAS-II will not start
====================================

While I hope this never happens again, there have been occasions where a
version of GSAS-II has a bug that prevents the program from starting.
If this version is installed, it is then not possible to access the
Help/Update menu command to obtain the different version of
GSAS-II. The same thing can also happen if you make changes to the
files yourself and introduce an error. Also, if you make changes to
the GSAS-II Python (.py) files, you can no longer obtain updates. 

A script is provided that can be used to reset any locally made
changes and then install the lastest version of GSAS-II. If you have
made changes that you wish to retain, you should make a copy of them
either using a utility to place a copy elsewhere, or you can use the
git stash, branch or commit commands. The commands below will
overwrite your changes with the latest GSAS-II version. 

On windows
----------------

At present, two windows .BAT files are created in the directory where
GSAS-II is installed, one named `Reset2FreshGSASII.bat` the other
`start_G2_bootstrap.bat`. Thus, if GSAS-II is installed in directory 
`C:\Users\toby\gsas2full` the files will be named
`C:\Users\toby\gsas2full\Reset2FreshGSASII.bat` and
`C:\Users\toby\gsas2full\start_G2_bootstrap.bat`.
Either will restore the GSAS-II files, but the
`Reset2FreshGSASII` file, will ask you to confirm before acting. The
files can run by locating them in the Windows File Explorer and
double-clicking on it or by typing the file name into the cmd.exe
window. 

On MacOS/Linux
----------------

At the time this is being written, an error prevents the script from
running, but this can be corrected by editing the `reset-gsasII.sh`
file manually (see below). Note that this file is placed in the `bin` directory
immediately below the GSAS-II installation directory. Thus, if
GSAS-II is installed at location `/Users/toby/G2/gsas2full` then the
file will be named `/Users/toby/G2/gsas2full/bin/reset-gsasII.sh`. (It
will appear in the path if conda is initialized.) Depending on the OS,
it may be possible to locate and run this file in a system-supplied
file browser, or type the file name into a terminal window. 

The error in the script is that the second line is incorrect. If the
lines appear as::

  # Commands to run GSAS-II load/update process
  source /bin/activate base
  /Users/toby/G2/gsas2full/bin/python /Users/toby/G2/gsas2full/gitstrap.py --reset

The second line should be changed as follows::

  # Commands to run GSAS-II load/update process
  source /Users/toby/G2/gsas2full/bin/activate base
  /Users/toby/G2/gsas2full/bin/python /Users/toby/G2/gsas2full/gitstrap.py --reset


Mailing List
====================================

If you use  GSAS-II, please join the mailing list so we can tell you
about what is new and changing. 

.. toctree::

   mailinglist.rst

Reporting Bugs
====================================

If something is not working properly in GSAS-II, please let us
know. If we don't know its broken, its not going to be
fixed. Information on how to report bugs is here. 

.. toctree::

   bug.rst


Information for code developers  
====================================

We encourage you to improve GSAS-II or to use the code in your own
projects. Some starting information is here:

.. toctree::

   developers.rst 

Installation details
====================================

Most people will not need these details, but some specific
installation details are discussed in the topics below.

.. toctree::
   :maxdepth: 3
	      
   compile.rst
   install-pip.rst
   proxy.rst
