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


Below is the e-mail sent to the GSAS-II mailing list concerning the above changes.

    From: GSAS-II <gsas-ii-bounces@aps.anl.gov> on behalf of Toby, Brian H. via GSAS-II <gsas-ii@aps.anl.gov>
    Date: Wednesday, April 23, 2025 at 12:08 PM
    To: gsas-ii@aps.anl.gov <gsas-ii@aps.anl.gov>
    Subject: [GSAS-II] Change to GSAS-II

    Hi everyone,

    GSAS-II has had a significant reorganization “under the hood” (or “under the bonnet” depending on your style of English). The goal of this was to bring the structure of the directories into the standard way that Python software is organized, which allows GSAS-II to be installed like other GSAS-II packages. This will be advantageous for sites that install GSAS-II on a central software server, such as ORNL and BNL as they will be able to use standard tools. It should also be helpful for people using GSAS-II as a scripting environment or incorporating parts of GSAS-II into their own software. My hope is that it will have very minor impact on most users. The old version was maintained in branch called “master” and the new one was started several months back as “main”. As of today, “main” is now the default and “master” is being retired. If you have problems, please do report them.

    If you installed GSAS-II from one of the gsas2full installers, when you next update to the latest GSAS-II version you will get version 5806. (This is the last update and version number for “master”). When you ask for the next update after 5806, you should automatically be switched to the “main” branch, which will also update shortcuts and install some Python packages. If you are installing GSAS-II in the future, please use the gsas2main installers (rather than the older gsas2full ones). This is documented in the installation instructions.

    While there are many hundreds of changes between “main” and “master,” one that is most likely to be noticed are that GSAS-II now has two types of version numbers. When we developed in svn, a consecutive number (that started with 1) was assigned for every change to the code. When we moved to GitHub, we continued using consecutive numbering of versions, but only incremented the number when a significant change was made. Automatic build systems want version numbers in the form x.y.z so version 5806 is now also noted as version v5.3.0. Minor changes that warrant a change to the consecutive version number will be noted by a change in the final digit of the new version number (e.g. v5.3.0 to v5.3.1) while more major changes will be noted by changing the second digit v5.3.x to v5.4.0). Nothing warranting going from v5 to v6 is planned, at least not at present.

    Another change that might affect users is that previously a file named GSASII.py was used to start the GUI. This had to be changed due to a naming conflict, so the file used to start GSAS-II is now G2.py. This will break shortcuts used to start GSAS-II, but should be addressed by the update process. A major addition is that GSAS-II now has scripts on GitHub that create the self-installers and build binaries (now using meson). There are also testing routines there, so we have a better chance to know when a change introduces a bug in the computations (not alas in the GUI) or the binaries/self-installers have problems. Many more details about the changes are listed here: https://advancedphotonsource.github.io/GSAS-II-tutorials/master2main.html

    Shoutouts on this transition go to Jerome Keiffer (ESRF) for meson and especially to Tom Caswell (BNL) who helped considerably.

    Brian  
