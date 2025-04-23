April 2025: Transition from Master to Main Branch
==================================================

.. _master2main:

On April 22, 2025 GSAS-II made a transition from development on a branch named "master" to a branch named "main". Several months of changes are behind this transition, which is documented below.

* Meson for building: Prior to this transition, the scons utility had been used to compile GSAS-II source code (written in Fortran, cython and C) into binaries. This broke with Python 3.12. A new compilation mechanism based on meson was implemented. The initial work on this was done by Jerome Kieffer (ESRF) and additional help was obtained from Tom Caswell (NSLS-II/BNL). GSAS-II is now provided with Python 3.12 and 3.13 binaries.

* Rework of self-installers: The GSAS-II self-installer, previously called gsas2full and now renamed as gsas2main, was revisited and streamlined. There is also now a conda package, also named gsas2main (on channel briantoby), but this is intended only for internal use in the self-installer.

* self-tests: there is now a suite of scripts that test the GSAS-II compiled binaries as well as significant portions of the GSAS-II crystallographic computations. These are run automatically when changes are checked into the main branch. They are also used to test binaries created with meson and are used to test self-installers (gsas2main).

* GitHub actions: there are a series of scripts for `the source code repository< https://github.com/AdvancedPhotonSource/GSAS-II/actions>`_
and  for `the build repository<https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/actions>`_ for these tasks:
  
  (1) Run the self-tests (smoke test, ``smoke_test.yml``). This is run whenever there are code check-ins to main. 
  (2) Create and test self-installers (build & test self-installers, ``matrix_g2main-test.yml``). At present this is triggered manually.
  (3) Compile GSAS-II binaries (compile & test binaries, ``matrix_comp-test.yml``). At present this is triggered manually.
  (4) Create and test a self-installer for RHEL (Build & test (RHEL) gsas2main self-installer, ``g2main-redhat.yml``). At present this is triggered manually.
  (5) Build the GSAS-II conda package, (build gsas2pkg, ``gsas2pkg.yml``). Work on this is not yet complete.

* Internal file reorganization: The GSAS-II Python files have been reorganized so that GSAS-II can be installed into Python's normal installation location (site-packages) and so that routines can be accessed using ``import GSASII`` (or ``import GSASII.G2-module``). This required revision of internal imports from ``import GSASIIobj as G2obj`` to ``from . import GSASIIobj as G2obj`` (or ``from .. import...`` in the ``imports`` and ``exports`` subdirectories.) Tom Caswell (NSLS-II/BNL) did much of this. 

* External packages previously included in GSAS-II (PyCifRW and baselines) are now installed as Python packages
  
* A new "update" routine has be included in master that installs newly required Python packages (such as PyCifRW and baselines) and then switches branches and reinstalls shortcuts. This is called when one attempts to update the "master" branch once the last update to that branch has been installed.

* A file named ``GSASII.py`` was previously used to start the GUI. Having a file sharing a name with a package does not work, so that file was renamed as ``GSASIIGUI.py`` and a new file named ``G2.py`` is now used to start GSAS-II.

* Citations to software used in GSAS-II is now tracked in a centralized location and a new Help command provides a list of those references.

* The configuration settings, which were previously saved in a Python source file, ``config.py`` are now saved in a file named ``config.ini``. That file is located in a "user" area (``~/.GSASII``) rather than with the GSAS-II source code. When the new "main" version of GSAS-II is started, if no ``config.ini`` file is found then the contents of ``config.py`` is used to initialize ``config.ini``.

* Obsolete code removed. This includes the code previously used for subversion (svn).

* Scripting: several commands now can read input files supplied as a URL; preferred orientation correction now are available in the API.
