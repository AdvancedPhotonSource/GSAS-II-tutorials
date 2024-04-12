.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right

======================= 
Installation overview
=======================

Running GSAS-II requires a number of coordinated installation steps and there are many different ways this can be accomplished. One needs not only the necessary Python source code for GSAS-II, but a Python interpreter that includes a number of "add-on" Python packages for additonal capabilities. This much match the computer where the software will be run. Further, GSAS-II requires that a small amount of its code be compiled, typically for speed and this must be matched both the computer OS and to the Python version. Here I outline different a few different approaches.

GSAS2FULL installer
=======================

Most users of GSAS-II are seeking a simple way to install and run the software and can live with the idea that they may have duplicated Python installations (several hundreds of MB each) on their computer. The GSAS2FULL self-installer provides that and can be `downloaded from here <https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/latest>`_. Brief installation instructions are outlined below with links to more complete instructions:

Windows
-----------

For Windows download file https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/download/v1.0.1/gsas2full-Latest-Windows-x86_64.exe and run it.
After the installer is started 
You will have a choice for where to install the software (the default is usually OK, but something like ``c:\software`` might be better, if your computer security allows that.)

More complete installation instructions `are here <install-g2f-win.html>`_.

MacOS and Linux
--------------------

For MacOS and Linux use a command such as:: 

  g2="https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/download/v1.0.1/gsas2full-Latest-<platform>"
  curl -L "$g2" > /tmp/g2.sh; bash /tmp/g2.sh -b -p <install-loc>

where:

 * <platform> is replaced by ``Linux-x86_64.sh`` for Linux, ``MacOSX-arm64.sh`` for MacOS with "Apple Silicon"  (M1, etc.) processors and ``MacOSX-x86_64.sh`` is for older Intel-based machines. Note that the ``MacOSX-x86_64.sh`` installer will run on "Apple Silicon" processors, but significantly more slowly. 
 * <install-loc> is where you want to install the software. (Use of ``~/g2full`` (a subdirectory named ``g2full`` in your home directory is a good choice.) After installation is complete, you may be asked if you want to place a shortcut for GSAS-II into the MacOS dock.

More complete installation instructions are provided for `MacOS <install-g2f-mac.html>`_ and `Linux <install-g2f-linux.html>`_.


GSAS2PKG Conda Package
=======================

Users who work extensively with Python and use the conda Python installer may prefer to utilize their existing conda installation to obtain GSAS-II along with the Python configuration that GSAS-II prefers. This can be done with this command (on all platforms)::

  conda create -n GSASII briantoby::gsas2pkg  -c conda-forge

This creates a conda virtual environment named ``GSASII`` (this can be changed) for use by GSAS-II. While it is also possible to install GSAS-II into the conda base environment, this is not recommended as it can create conflicts between Python and package versions needed by GSAS-II and those required by other packages. (If you choose to do this anyway, be sure to specify ``conda install python=3.11 briantoby::gsas2pkg`` as Python is likely to be pinned to a different version.)

After this command is run, use command ``conda activate GSASII`` to access the
conda environment that has been created. On Linux and MacOS computers, two shortcut commands will then be available in the path, The first command, ``gsasII.sh``, which will start GSAS-II. This can optionally be used as ``gsasII.sh project.gpx`` to open existing project file ``project.gpx`` in GSAS-II. The second command, ``reset-gsasII.sh``  will rarely be used. This command will download the latest version of GSAS-II and update to that version, replacing any locally modified files with the original versions. This can be used to update GSAS-II when the program will not start, so the normal Help->Update menu command cannot be accessed. (Shortcuts available with gsas2pkg v5.1+.)

Note that on MacOS, a Mac app is also created and is displayed in the Finder
`see steps 5 & 6 here <install.html#macos-gsas2full-installation-details>`_. This app can be used to start GSAS-II from the dock or desktop.

Installing GSAS-II after Python Installation
=============================================

A small number of users or sites prefer to use Python distributions supplied via other routes (such as Debian packages) or using `PyPi <https://pypi.org>`_, etc. or prefer to handle use of conda on their own. Some discussion on Python installation is
`found here <install-pip.html>`_. Independent of how Python is installed, multiple packages are needed, please see the
`discussion on Python package requirements <https://gsas-ii.readthedocs.io/en/latest/packages.html#gui-requirements>`_, noting that the GSAS-II GUI requires at a minimum wxPython, matplotlib,
PyOpenGL, NumPy and SciPy, while for scripting use, only NumPy and SciPy are required.  For full functionality, several other optional packages are needed.
If versions other than those recommended are selected (Python=3.11 and NumPy=1.26), you will likely need to either locate older binaries and install them manually or compile them yourself (`see compilation information <https://advancedphotonsource.github.io/GSAS-II-tutorials/compile.html>`_). 

A simple way to install GSAS-II with a supplied Python environment uses the ``gitstrap.py`` script provided for this purpose. Use these commands (on any platform) to install GSAS-II::

  cd ~/G2
  curl -L -O https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/raw/main/install/gitstrap.py
  python gitstrap.py

This will place the install script in directory ``~/G2`` (which you may wish to change) and will place all GSAS-II files in subdirectory ``~/G2/GSAS-II``

Installation for GSAS-II Software Developers
==============================================

While all of the above approaches do clone a copy of the GSAS-II repository from GitHub, software developers will likely wish to clone the repo themselves. This will also require This is done
from 
``git@github.com:AdvancedPhotonSource/GSAS-II.git`` or ``https://github.com/AdvancedPhotonSource/GSAS-II.git``.

If the repo is cloned at ``~/myProjects/myGSASII`` then the local copy of GSAS-II can be 
run as a GUI using::

  python ~/myProjects/myGSASII/GSASII/GSASII.py

Installation scripts used inside the above-listed approaches can still be used for GitHub repo installation. See discussion of makeMacApp.py, makeLinux.py and makeBat.py (for MacOS, Linux and Windows, respectively) in the `Developer's Documentation <https://gsas-ii.readthedocs.io/en/latest/GSASIIscripts.html#gsas-ii-misc-scripts>`_.
Also, to simplify use of your local clone of the GSAS-II repo when scripting GSAS-II, see this `note on scripting shortcuts
<https://gsas-ii.readthedocs.io/en/latest/GSASIIscriptable.html#shortcut-for-scripting-access>`_. 

Older methods
=================================

Previously GSAS-II was provided via an Advanced Photon Source-maintained subversion (svn) server, with differing installation processes. While the installers for those processes are still available. Also, updates will be provided for those past svn installations for the immediate future. However, it is encouraged that users reinstall GSAS-II via one of the above methods. When svn updates will be phased out, GSAS-II will provide warning messages.

.. include:: install-g2f-win.rst

.. include:: install-g2f-mac.rst

.. include:: install-g2f-linux.rst

	     
