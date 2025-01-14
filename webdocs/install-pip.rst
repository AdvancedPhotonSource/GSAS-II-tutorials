.. raw:: html

	 <style> .clear {clear: both;}</style>

.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right
	   
.. index:: Customized Python installation

==================================================
Customized Python Installation 
==================================================

Experienced system managers or code developers may wish to perform their own Python installations. Noting that the GSAS-II GUI requires at a minimum wxPython, matplotlib, PyOpenGL, NumPy and SciPy be installed, while for scripting use, only NumPy and SciPy are required.  For full functionality, several other optional packages are needed, as is `discussed in the GSAS-II Python package requirements <https://gsas-ii.readthedocs.io/en/latest/packages.html#gui-requirements>`_.
If Python versions other than those recommended are selected (Python=3.11 and NumPy=1.26), you will likely need to either locate older binaries and install them manually or run the compilation yourself (`see compilation information <https://advancedphotonsource.github.io/GSAS-II-tutorials/compile.html>`_). 

The choices for how to install Python and packages come down to distribution methods such as conda, pip, homebrew or Linux distro-supplied installation. It is also possible to obtain all as source code and compile them locally.

.. index:: Customized Python installation; conda

conda
----------

With conda, use commands such as this::

         conda install python=3.11  numpy=1.26 wxpython scipy matplotlib pyopengl pillow h5py imageio requests git gitpython -c conda-forge

or::

       conda create -n <envname> python=3.11  numpy=1.26 wxpython scipy matplotlib pyopengl pillow h5py imageio requests git gitpython -c conda-forge 

.. index:: Customized Python installation; pip

pip
--------

For pip (PyPI) installation, download and install Python from https://www.python.org/downloads/ (the 3.11 version is recommended) and then use a Python pip command similar to this::

     pip install numpy wxpython scipy matplotlib pyopengl pillow h5py imageio requests gitpython 

.. index:: Customized Python installation; homebrew

homebrew
---------------

Homebrew is one of several installers that will install a OS-specific complied software package or will download, compile and install the package from source code. See help information for that installer.

.. index:: Customized Python installation; Linux distro tools

Distro-supplied packages
---------------------------------

A small number of users or sites prefer to use Python distributions supplied via a Linux distribution, such as from Ubuntu, Debian or Redhat. As an example for how this is done, please see some older notes on installation with the Raspberry Pi OS:  https://subversion.xray.aps.anl.gov/trac/pyGSAS/wiki/InstallPiLinux.

With Redhat Enterprise Linux (RHEL) if you want to use RHEL-supplied
versions of Python, you can use this command to install a fairly old
version of Python::

  sudo yum install python3-wxpython4 python3-matplotlib python3-numpy python3-scipy python3-GitPython python3-requests python3-pillow python3-h5py  python3-pyopengl

As you will likely need to create your own binary files, you will also
likely need this as well::

  sudo yum install python3-scons python3-numpy-f2py

RHEL also supplies a Python 3.11 interpreter, but not very many
packages for that, so pip will be needed (this is pretty slow, FWIW)::
  
  sudo yum install python3.11 python3.11-numpy python3.11-scipy  python3.11-pip python3.11-wheel
  pip3.11 install wxpython 
  pip3.11 install matplotlib
  pip3.11 install pyopengl
