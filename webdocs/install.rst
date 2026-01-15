.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right

============================================ 
Installing GSAS-II: Overview
============================================

.. index:: Installation overview

GSAS-II requires a number of coordinated installation steps and there are many 
different ways this can be accomplished. One needs -- not only the necessary Python source 
code for GSAS-II -- but a Python interpreter that includes a number of "add-on" Python 
packages for additional capabilities. This much match the operating system for the 
computer where the software will be run. Further, GSAS-II requires that a small amount 
of its code be compiled, typically for speed and this must be matched both the computer 
OS and to the Python version. Here I outline different a few different approaches.

Most users of GSAS-II, particularly those using Windows and MacOS, are seeking
a simple way to install and run the software and can live 
with the idea that they may have duplicated Python installations (several hundreds of MB each) 
on their computer. The GSAS2MAIN self-installer provides simple installation and can be 
`downloaded from here
<https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/latest>`_. The
GSAS2MAIN self-installer also has the advantage that once GSAS-II is
installed, updates can be obtained from a command in the Help menu. 
More details on the GSAS2MAIN installation process are 
summarized by operating systems in the next few sections of this web
page, with links to more detailed instructions should those be
needed. Links to alternate
installation options follow after that, along with information needed
for anyone wishing to help develop GSAS-II.

.. index:: gsas2main installer

GSAS2MAIN installer for Windows
==================================

For Windows download file https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/download/v1.0.1/gsas2main-Latest-Windows-x86_64.exe and run it.
After the installer is started, you will have a choice for where to
install the software (the default is usually OK, but something like
``c:\software`` might be better, if your computer security allows that.)

You do not need to have administrator access to your computer to
install GSAS-II, and installing from an admin account is not
recommended, but apparently the newest windows security makes it
hard to install software that is not registered with Microsoft: I am
told you have to first right click, go to Properties, and check the “Unblock” box.

More complete installation instructions on the 
installation process with GSAS2MAIN on windows are linked below. 

.. index:: gsas2main windows details
.. toctree::
   :maxdepth: 1
	      
   install-g2f-win.rst


GSAS2MAIN installer for MacOS
==================================

For ARM (M1,...) MacOS use a command such as::
  
    g2="https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/download/v1.0.1/gsas2main-Latest-MacOSX-arm64.sh"
    curl -L "$g2" > /tmp/g2.sh; bash /tmp/g2.sh -b -p <install-loc>

For older Intel MacOS use a command such as:: 

    g2="https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/download/v1.0.1/gsas2main-Latest-MacOSX-x86_64.sh"
    curl -L "$g2" > /tmp/g2.sh; bash /tmp/g2.sh -b -p <install-loc>

  
* This ``MacOSX-x86_64.sh`` installer will also run on "Apple
  Silicon" processors, but runs significantly more slowly.
   
Note that in the above, `<install-loc>` is where you want to install
the software. (Use of ``~/g2main``, a subdirectory named ``g2main`` in
your home directory is a good choice.) After installation is complete,
you will be given a chance to place a shortcut for GSAS-II into the
MacOS dock. 

More complete installation instructions on the GSAS2MAIN
installation process on MacOS are linked below. 

.. index:: gsas2main MacOS details
.. toctree::
   :maxdepth: 3
 
   install-g2f-mac.rst

GSAS2MAIN installer for Linux
==========================================

Linux turns out to be the hardest system to provide pre-built
installers. Binary compatibility between Linux systems is not all that
good, due to incomtabilities in system libraries between
different Linux dists. Two GSAS2MAIN
installers are provided for Linux, with 
one built on an APS Redhat Enterprise server,  and the other
on an Ubuntu GitHub runner (24.04.2 LTS, last I
checked). Neither may be compatible with other Linux versions. 

There are several installation options, described in later sections of
this page, that should work with any Linux distribution. These include
use of :ref:`pixi <pixi installation>`, :ref:`pip <pip installation>`
or installing GSAS-II after Python is installed locally. 
The disadvantage of pixi and pip is that you will need to
update GSAS-II manually.

To install GSAS2MAIN in Linux using the GitHub runner  version, use a command such as::
  
  g2="https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/download/v1.0.1/gsas2main-Latest-Linux-x86_64.sh"
  curl -L "$g2" > /tmp/g2.sh; bash /tmp/g2.sh -b -p <install-loc>

That version will not run on APS Redhat Enterprise Linux systems, for
RHEL install with the alternate installer using command::

  g2="https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/download/v1.0.1/gsas2main-rhel-Latest-Linux-x86_64.sh"
  curl -L "$g2" > /tmp/g2.sh; bash /tmp/g2.sh -b -p <install-loc>

where:

 <install-loc> is where you want to install the software. (Use of
 ``~/g2main``, a subdirectory named ``g2main`` in your home directory
 is a good choice.)

More complete installation instructions on the GSAS2MAIN
installation process on linux are below. 

.. index:: gsas2main MacOS details
.. toctree::
   :maxdepth: 3
	      
   install-g2f-linux.rst

Installing GSAS-II via pixi
======================================================

The pixi installation system runs quickly and has become quite
popular. It is a good choice
for Linux, as it compiles GSAS-II source code locally. The most
significant disadvantage is that It interferes with GSAS-II's
self-updating process,
unless the ``pixi run install-editable`` option is used. 
GSAS-II uses pixi internally to install the software to run
self-tests every time a change is made to GSAS-II.

.. index:: pixi installation
.. toctree::
   :maxdepth: 1
	      
   install_pixi.rst

Installing GSAS-II via pip
======================================================

The "standard" method for installing Python and packages uses the
Python package installer and downloads packages from the Python Package Index (PyPI)

.. index:: pip installation
.. toctree::
   :maxdepth: 1

   install-pip.rst

Separate Python & GSAS-II Installation
======================================================

There are some users and sites that wish to use GSAS-II with Python
that is installed independently of GSAS-II. This can save disk space and
may provide some optimization. The web page below describes different
mechanisms for installing Python and then
options for installing GSAS-II after Python is installed. 

.. toctree::
   :maxdepth: 2
	      
   install-python.rst

.. index:: Compiling GSAS-II

Compiling GSAS-II
======================================================

If using GSAS-II on some Linux dists, or with versions of Python/numpy other than
what we support, it may be necessary (or a site policy) to compile the
GSAS-II binaries locally rather than download them. A script is
supplied (``gitcompile.py``) that downloads GSAS-II and 
compiles the GSAS-II source files (see :ref:`gitcompile`). Alternately, it is possible to
build and install GSAS-II with pixi (see :ref:`pixi installation`) or
pip (see :ref:`pip installation`). This can also be done manually, as
described in the page listed below. 

.. toctree::
   :maxdepth: 2
	      
   compile.rst


.. index:: Installing GSAS-II with gitstrap.py

           
Externally-developed software
==============================================

GSAS-II provides interfaces to use a number of programs developed by
others. Some are included with GSAS-II, some are accessed over the web
and others must be installed 
separately. These are all discussed in some detail in the `Developer's Documentation
<https://gsas-ii.readthedocs.io/en/latest/packages.html#supported-externally-developed-software>`_.
Installation details for the programs that must be installed by users
is included in the section below. 

.. toctree::
   :maxdepth: 2
	      
   install-external.rst

Installation Info for Developers
==============================================

While all of the above approaches will clone a copy of the GSAS-II
repository from GitHub, software developers may find it more
convenient to clone the repo themselves. This will typically be done
as part of a process where a copy of GSAS-II is forked on GitHub. This
is described in a `separate page <install_dev.html>`_ (outline
below). 

.. index:: Installing for development
.. toctree::
   :maxdepth: 3
	      
   install_dev.rst

Proxy Issues
======================================

Some sites funnel all web access through a special routing called
a web proxy. For some details on how this needs to be addressed, see here:

.. toctree::
   :maxdepth: 3
   
   proxy.rst

Older Installers
=================================

Previously GSAS-II was provided via an Advanced Photon Source-maintained 
subversion (svn) server, with differing installation processes. GSAS-II 
is not longer being updated on the APS subversion server, so those installers 
should not be used. If GSAS-II is installed from subversion, 
you will not be able to update to the current GSAS-II version and
you will be
shown a message when trying to update that you should reinstall
GSAS-II as described above.

Likewise, the gsas2full installer was used to install GSAS-II from the
older ``master`` branch on GitHub. Use of this installer is strongly discouraged 
as it will provide a much older version of GSAS-II. If you
install GSAS-II from that branch, you will be
be offered the opportunity to add needed Python packages and switch to
the ``main`` branch when trying to update GSAS-II from the help menu.
