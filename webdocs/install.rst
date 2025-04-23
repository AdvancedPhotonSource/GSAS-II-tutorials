.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right

============================================ 
Installing GSAS-II: Overview
============================================

.. index:: Installation overview

Running GSAS-II requires a number of coordinated installation steps and there are many different ways this can be accomplished. One needs not only the necessary Python source code for GSAS-II, but a Python interpreter that includes a number of "add-on" Python packages for additional capabilities. This much match the operating system for the computer where the software will be run. Further, GSAS-II requires that a small amount of its code be compiled, typically for speed and this must be matched both the computer OS and to the Python version. Here I outline different a few different approaches.

.. index:: gsas2main installer

GSAS2MAIN installer
=======================

Most users of GSAS-II are seeking a simple way to install and run the software and can live with the idea that they may have duplicated Python installations (several hundreds of MB each) on their computer. The GSAS2MAIN self-installer provides simple installation and can be `downloaded from here <https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/latest>`_. Brief installation instructions are outlined below with links to more complete instructions:

Windows
-----------

For Windows download file https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/download/v1.0.1/gsas2main-Latest-Windows-x86_64.exe and run it.
After the installer is started 
You will have a choice for where to install the software (the default is usually OK, but something like ``c:\software`` might be better, if your computer security allows that.)

More complete installation instructions `are here <install-g2f-win.html>`_.

MacOS
--------------------

For ARM (M1,...) MacOS use a command such as::
  
    g2="https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/download/v1.0.1/gsas2main-Latest-MacOSX-arm64.sh"
    curl -L "$g2" > /tmp/g2.sh; bash /tmp/g2.sh -b -p <install-loc>

For older Intel MacOS use a command such as:: 

    g2="https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/download/v1.0.1/gsas2main-Latest-MacOSX-x86_64.sh"
    curl -L "$g2" > /tmp/g2.sh; bash /tmp/g2.sh -b -p <install-loc>

  
Note that the ``MacOSX-x86_64.sh`` installer will also run on "Apple Silicon" processors, but significantly more slowly.
   
where:

 <install-loc> is where you want to install the software. (Use of ``~/g2main``, a subdirectory named ``g2main`` in your home directory is a good choice.) After installation is complete, you will be given a chance to place a shortcut for GSAS-II into the MacOS dock.

More complete installation instructions are provided for `MacOS separately <install-g2f-mac.html>`_.

Linux
--------------------

To install GSAS2MAIN in Linux use a command such as::
  
  g2="https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/download/v1.0.1/gsas2main-Latest-Linux-x86_64.sh"
  curl -L "$g2" > /tmp/g2.sh; bash /tmp/g2.sh -b -p <install-loc>
  
where:

 <install-loc> is where you want to install the software. (Use of ``~/g2main``, a subdirectory named ``g2main`` in your home directory is a good choice.) 

More complete installation instructions are provided for `Linux separately <install-g2f-linux.html>`_.


GSAS2MAIN Additional Details
----------------------------------------

The pages listed below go through the GSAS2MAIN installation process on each identified platform in much greater detail.

.. index:: gsas2pkg installer
.. toctree::
   :maxdepth: 3
	      
   install-g2f-win.rst
   install-g2f-mac.rst
   install-g2f-linux.rst
	      

GSAS2PKG Conda Package
=======================

Users who work extensively with Python and use the conda Python installer may prefer to utilize their existing conda installation to obtain GSAS-II along with the Python configuration that GSAS-II prefers. This can be done with this command (on all platforms)::

  conda create -n GSASII briantoby::gsas2pkg  -c conda-forge

This creates a conda virtual environment named ``GSASII`` (this can be changed) for use by GSAS-II. While it is also possible to install GSAS-II into the conda base environment, this is not recommended as it can create conflicts between Python and package versions needed by GSAS-II and those required by other packages. (If you choose to do this anyway, be sure to specify ``conda install python=3.11 briantoby::gsas2pkg`` as Python is likely to be pinned to a different version.)

After this command is run, use command ``conda activate GSASII`` to access the
conda environment that has been created. On Linux and MacOS computers, two shortcut commands will then be available in the path, The first command, ``gsasII.sh``, which will start GSAS-II. This can optionally be used as ``gsasII.sh project.gpx`` to open existing project file ``project.gpx`` in GSAS-II. The second command, ``reset-gsasII.sh``  will rarely be used. This command will download the latest version of GSAS-II and update to that version, replacing any locally modified files with the original versions. This can be used to update GSAS-II when the program will not start, so the normal Help->Update menu command cannot be accessed. (Shortcuts available with gsas2pkg v5.1+.)

Note that on MacOS, a Mac app is also created and is displayed in the Finder
`see steps 5 & 6 here <install.html#macos-gsas2main-installation-details>`_. This app can be used to start GSAS-II from the dock or desktop.

.. index:: Installing GSAS-II with gitstrap.py

Installing GSAS-II with separate Python Installation
======================================================

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

Note that you can also clone the GitHub repo. If you do this, the GSAS-II binary files
will not be installed. However, when GSAS-II is first run, it will provide an opportunity to do this. 

.. index:: Installing GSAS-II from GitHub

Installing directly from GitHub
==============================================

While all of the above approaches will clone a copy of the GSAS-II repository from GitHub, software developers may find it more convenient to clone the repo themselves. This will typically be done as part of a process where a copy of GSAS-II is forked on GitHub. This is described in a `separate page <install_dev.html>`_ (outline below). 

.. index:: Installing for development
.. toctree::
   :maxdepth: 3
	      
   install_dev.rst


Older installers
=================================

Previously GSAS-II was provided via an Advanced Photon Source-maintained subversion (svn) server, with differing installation processes. The subversion server is not longer being updated, so those installers should not be used because if GSAS-II is installed from subversion, you will not be able to update to the current GSAS-II version.
If you previously installed GSAS-II from that server, you will be
shown a message when trying to update that you should reinstall
GSAS-II as described above.

Likewise, the gsas2full installer was used to install GSAS-II from the
older ``master`` branch. Use of this installer is discouraged. If you
install GSAS-II from that branch, you will be
be offered the opportunity to add needed Python packages and switch to
the ``main`` branch when trying to update GSAS-II from the help menu.

Installation details
====================================

Most people will not need these details, but some specific
installation details are discussed in the topics below. Also note the
information `on compiling GSAS-II
<https://advancedphotonsource.github.io/GSAS-II-tutorials/compile.html>`_
if the distributed binaries cannot be used.

.. toctree::
   :maxdepth: 3
	      
   install-pip.rst
   proxy.rst

