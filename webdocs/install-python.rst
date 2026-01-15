.. raw:: html

	 <style> .clear {clear: both;}</style>

.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right
	   
.. index:: Local Python installation

.. _InstallPython:
           
==================================================
GSAS-II Installation after Installing Python 
==================================================

-------------------------------------------
 Overview
-------------------------------------------

A small number of users/sites prefer to install Python
distributions directly, rather than use the previous installation
methods that install Python and GSAS-II together.
This can save disk space,
since one Python installation (preferably with virtual environments)
can be used for many different software installations. Also, the
versions of Python and its packages can be potentially optimized for
the computing environment being used, for example by using versions
that are distributed with the operating system. 
Independent of how Python is installed, multiple packages are needed, please see the
`discussion on Python package requirements
<https://gsas-ii.readthedocs.io/en/latest/packages.html#python-requirements>`_,
noting that the GSAS-II GUI requires at a minimum wxPython, matplotlib
(matplotlib-base is preferred over matplotlib unless matplotlib will
be used outside GSAS-II), PyOpenGL, NumPy and SciPy, while for
scripting use, only NumPy and SciPy are required, but many optional
packages allow GSAS-II to do much more.

Note that pre-compiled GSAS-II binaries are supplied for only a
a very limited number of Python and NumPy versions (found at
https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/latest). At
present that includes only Python 3.11/NumPy 1.26,  Python 3.12/NumPy
2.2, and  Python 3.13/NumPy 2.2. If you use any other versions, you
will need to compile GSAS-II locally (`see compilation information <compile.html>`_). 


The choices for how to install Python and packages come down to
distribution methods such as conda, pip, homebrew or Linux
distro-supplied installation. It is also possible to obtain Python and
all packages as source code and compile them locally, but expect that
to be quite time consuming. 

-------------------------------------------
 Python Installation Methods
-------------------------------------------

.. index:: Customized Python installation; Linux dists

Linux dists
-------------------

A small number of users or sites prefer to use Python distributions
supplied via a Linux distribution, such as from Ubuntu, Debian or
Redhat.  Alas, the names of the packages vary considerably between
Linux dists, but at a minimum install Python, NumPy, SciPy and when possible
wxPython with the dist supplied package manager (apt, dnf,
you, etc.). Any packages not available via the Linux dist can be
installed with pip.

Note that if your Linux dist does not supply wxpython, you will need
to install that with pip, which means that you will either need to
find a prebuilt wheel matching your OS or will need to
have the tools and packages needed to build wxpython. This is
discussed in more detail `in a previous section <install-pip.html>`_.

For most forms of Linux, it is not recommended that you try to use pre-compiled
binaries. This means that you will need to compile the GSAS-II
source code. To perform this compilation you will need to install
gfortran, gcc, cython and meson. (Note that cython and meson can be
installed via pip but gfortran and gcc should be installed from the
Linux package manager.) The ``gitcompile.py`` `described below
<#gitcompile>`_ provides a convenient way to download, compile and
install GSAS-II.

With a mixed installation, where some packages are installed from the
Linux dist and others from pip, do not use the pip command 
discussed  `in a previous section <install-pip.html>`_ to install
GSAS-II as that will reinstall all the Linux-dist Python packages from pip.

Some older notes on installation with the Raspberry Pi OS:
https://subversion.xray.aps.anl.gov/trac/pyGSAS/wiki/InstallPiLinux
may be useful. 

.. index:: Customized Python installation; conda

conda
----------

The conda-forge package management system provides Python and
considerable software. Use of the Anaconda distribution is not
recommended, as it does not include wxpython and there may be royalty
payment issues with Anaconda. You are recommended to install the
conda-forge package (which is the same thing as miniforge) from
`the conda-forge site <https://conda-forge.org/download/>`_.  The
miniforge package can also be found at
https://github.com/conda-forge/miniforge/releases/latest.  miniforge 
supplies Python and the conda package manager.

If GSAS-II will be the only Python software you will use, you can put
all the Python versions that GSAS-II wil use into the "base"
installation using a command such as this to install Python
and all the packages GSAS-II
will use::

         conda install python numpy wxpython scipy matplotlib-base pyopengl pycifrw git gitpython requests conda pybaselines pillow h5py imageio seekpath xmltodict zarr sympy -c conda-forge

Note that the packages starting with ``git`` are optional, but you are
encouraged to include the packages at least through ``pybaselines`` as
they add functionality to GSAS-II that is likely to be used. 
         
If you plan to use supplied GSAS-II binaries, you should specify the
Python and NumPy versions, as in the next command, but you should
consider adding packages you will need for compilation, ``gfortran``, ``meson``
and ``cython``::

  conda install python=3.12 numpy=2.2 wxpython scipy matplotlib-base pyopengl pycifrw git gitpython requests conda pybaselines pillow h5py imageio seekpath xmltodict zarr sympy -c conda-forge
  
You are recommended to install Python into a conda virtual environment
for GSAS-II so that it will be independent of any other Python
configurations that you might want to have. The command to do this is
similar to the previous::

  conda create -n <envname> python=3.12 numpy=2.2 wxpython scipy matplotlib-base pyopengl pycifrw git gitpython requests conda pybaselines pillow h5py imageio seekpath xmltodict zarr sympy -c conda-forge

Note that if you will be compiling GSAS-II binaries yourself, you can
omit the version numbers on python and numpy.


.. index:: Customized Python installation; pip

pip
--------

For pip (PyPI) installation, download and install Python from
https://www.python.org/downloads/ (the 3.13 version is
recommended). Alternately, on Windows, it is also possible to use the
winget command. Once Python is installed, you can then use a Python
pip command similar to this:: 

     pip install numpy wxpython scipy matplotlib pyopengl pycifrw gitpython requests pybaselines pillow  h5py imageio seekpath xmltodict zarr sympy

Also see the more detailed  discussion on pip `in a previous section <install-pip.html>`_.

.. index:: Customized Python installation; homebrew

homebrew installer
----------------------

Homebrew is one of several installers that will install a OS-specific
complied software package or will download, compile and install the
package from source code. It is available for MacOS and Linux. See
help information `for that installer <https://brew.sh/>`_.

.. index:: Customized Python installation; uv

uv installer
---------------

The `uv <https://docs.astral.sh/uv/>`_ installer is available on
Windows, Linux and MacOS and will install a OS-specific complied
software package or will download, compile and install the package
from source code. I have not used it for GSAS-II, but it looks 
very promising. See help information `for uv <https://docs.astral.sh/uv/getting-started/installation/>`_.

-----------------------------------------------------------
GSAS-II Installation after Python Installation
-----------------------------------------------------------

While in previous sections of this documentation, mechanisms for
installing GSAS-II along with Python have been explored via the `the
GSAS2MAIN installer <install.html>`_, the `pixi
installer <install_pixi.html>`_, and the `pip
installer <install-pip.html>`_, if Python will be installed prior to 
GSAS-II, different approaches must be used. Two scripts are supplied
that perform all needed steps, but it is possible to do this
manually. 

.. _gitstrap:

.. index:: Installing GSAS-II with gitstrap

Using the gitstrap.py installer
-------------------------------------------

A simple way to install GSAS-II with a supplied Python environment
uses the ``gitstrap.py`` script provided for this purpose. This will
also download pre-compiled GSAS-II binary files, so it requires
specific combinations of Python and NumPy versions. Use
commands such as these (on any platform) to install GSAS-II::

  cd G2
  curl -L -O https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/raw/main/install/gitstrap.py
  python gitstrap.py

This will create a directory named G2 wherever you start running the
commands and will use git to clone the
AdvancedPhotonSource/GSAS-II repo placing all files in subdirectory
``G2/GSAS-II`` (on Windows ``G2\GSAS-II``. The script does the following things:

 * Checks that the Python installation has the packages that GSAS-II
   needs to run (`see here for details
   <https://gsas-ii.readthedocs.io/en/latest/packages.html#python-requirements>`_).
 * Installs the GSAS-II files from the GitHub repo
 * Downloads and installs the appropriate binary files from the
   `GSAS-II releases <https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases>`_
 * Does a byte-compile on all ``.py`` files
 * Creates shortcuts/icons for starting GSAS-II (OS specific)

If GSAS-II was previously installed, the ``gitstrap.py`` will update
that installation with the current version. This is a useful
alternative to the Help/Update command (which will cannot be used when
GSAS-II will not start after a bad update.) Note that there are a
number of options that can be used with the 
script. If GSAS-II will not start due to changes that you have made, the ``--reset``
option is useful. The command ``python gitstrap.py --reset`` overwrites any
changes that have been made to GSAS-II files locally with the original
versions of the files. The other options are not likely to be needed,
but can be seen with ``python gitstrap.py --help``. Note that the
``gitstrap.py`` is used inside the GSAS2MAIN self-installers.

.. _gitcompile:

.. index:: Installing GSAS-II with gitcompile

Using the gitcompile.py installer
-------------------------------------------

A simple way to install GSAS-II with a supplied Python environment
and compile the GSAS-II binaries 
uses the ``gitcompile.py`` script provided for this purpose. This will
also download pre-compiled GSAS-II binary files, so it requires
specific combinations of Python and NumPy versions. Use
commands such as these (on any platform) to install GSAS-II::

  cd G2
  curl -L -O https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/raw/main/install/gitcompile.py
  python gitcompile.py

This will create a directory named G2 wherever you start running the
commands and will use git to clone the
AdvancedPhotonSource/GSAS-II repo placing all files in subdirectory
``G2/GSAS-II`` (on Windows ``G2\GSAS-II``. The script does the following things:

 * Checks that the Python installation has the packages that GSAS-II
   needs to run (`see here for details
   <https://gsas-ii.readthedocs.io/en/latest/packages.html#python-requirements>`_)
   and for compilation.
 * Installs the GSAS-II files from the GitHub repo
 * Compiles and installs the appropriate binary files from the
   Fortran, C and Cython sources using meson. 
 * Does a byte-compile on all ``.py`` files
 * Creates shortcuts/icons for starting GSAS-II (OS specific)

If GSAS-II was previously installed, the ``gitcompile.py`` will update
that installation with the current version. This is a useful
alternative to the Help/Update command (which will cannot be used when
GSAS-II will not start after a bad update.) Note that there are a
number of options that can be used with the 
script. If GSAS-II will not start due to changes that you have made, the ``--reset``
option is useful. The command ``python gitcompile.py --reset`` overwrites any
changes that have been made to GSAS-II files locally with the original
versions of the files. The other options are not likely to be needed,
but can be seen with ``python gitcompile.py --help``


GSAS2PKG Conda Package
-------------------------------------------

Users who work extensively with Python and use the conda Python installer may prefer to utilize their existing conda installation to obtain GSAS-II along with the Python configuration that GSAS-II prefers. This can be done with this command (on all platforms)::

  conda create -n GSASII briantoby::gsas2pkg  -c conda-forge

This creates a conda virtual environment named ``GSASII`` (this can be
changed) for use by GSAS-II. While it is also possible to install
GSAS-II into the conda base environment, this is not recommended as it
can create conflicts between Python and package versions needed by
GSAS-II and those required by other packages. (If you choose to do
this anyway, be sure to specify ``conda install python=3.13
briantoby::gsas2pkg`` as Python is likely to be pinned to a different
version.) Note that it runs the ``gitstrap.py`` installer (see :ref:`gitstrap`).

After this command is run, use command ``conda activate GSASII`` to access the
conda environment that has been created. On Linux and MacOS computers, two shortcut commands will then be available in the path, The first command, ``gsasII.sh``, which will start GSAS-II. This can optionally be used as ``gsasII.sh project.gpx`` to open existing project file ``project.gpx`` in GSAS-II. The second command, ``reset-gsasII.sh``  will rarely be used. This command will download the latest version of GSAS-II and update to that version, replacing any locally modified files with the original versions. This can be used to update GSAS-II when the program will not start, so the normal Help->Update menu command cannot be accessed. 

Note that on MacOS, a Mac app is also created and is displayed in the Finder
`see steps 5 & 6 here <install.html#macos-gsas2main-installation-details>`_. This app can be used to start GSAS-II from the dock or desktop.

.. _manual compile:

.. index:: Installing GSAS-II manually


Installing GSAS-II manually 
-------------------------------------------

There is no requirement that GSAS-II be installed from the
``gitstrap.py`` or the ``gitcompile.py`` scripts, but to do this
manually one must:

* run the git command to download GSAS-II (see `the pixi
  section <install_pixi.html>`_ for more information on using the git
  command. 

* download and expand the GSAS-II binaries from  the `GSAS-II releases
  <https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases>`_
  and move them to a location where GSAS-II will find them. 

Or

* make sure that the compilers and tools needed to build the GSAS-II
  binaries are installed (gfortran, gcc, cython and meson).

* run the meson command (see :ref:`Compiling GSAS-II`)

*  move the the GSAS-II binaries to a location where GSAS-II will find them. 
