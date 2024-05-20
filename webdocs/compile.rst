.. raw:: html

	 <style> .clear {clear: both;}</style>

.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right

.. index:: Compiling GSAS-II

====================== 
Compiling GSAS-II
======================

A small amount of GSAS-II code is written in Fortran and one routine in C, rather than Python, to provide improved computation speed. Other large and complex capabilities, such as the GSAS(-I) space group interpretation code and DIFFaX are also used as as Fortran code. This code must be compiled before it is run. Normally this is done for you, but on occasion it must be done locally.

The supplied binaries are placed in a subdirectory name with name
`prefix`\ _p\ `X.X`\ _n\ `Y.Y` where
`prefix` is noted below and `X.X` is the Python version and `Y.Y` is the numpy

  * Windows-10: 64-bit Intel-compatible processors. [Prefix `win_64_`\ ]
  * MacOS: Intel processors. [Prefix `mac_64_`\ ]
  * MacOS: ARM processors, aka Apple Silicon (M1, etc). [Prefix `mac_arm_`\ ]
  * Linux: 64-bit Intel-compatible processors. [Prefix `linux_64_`\ ]
  * Linux: ARM processors (64-bit and 32-bit Raspberry Pi OS only).
    [Prefixes `linux_arm32_` and `linux_arm64_`\ ]

Some older versions combinations of Python and
NumPy can be found in the older svn repository for GSAS-II:
https://subversion.xray.aps.anl.gov/trac/pyGSAS/browser/Binaries

The compilation process requires installation of the gcc and gfortran compilers. Others may be possible, but have not been tried. Also, the Python Scons package must be installed into Python. compilation is done with commands::

    cd fsource
    scons

The scons file captures the compilation options needed for the supported platforms, but to compile on other platforms, it may be necessary to modify the `Sconstruct` file to configure for the new platform.     

Installation of compilers is highly depend on the computer system being used, but in many cases they can be installed as a conda package, with a command such as::

      conda install gfortran_osx-64 scons

Use the ``conda search gfortran`` command to find the name for the package. 
On most linux systems, one can use a command such as ``sudo apt-get gfortran`` or ``yum install gcc-gfortran``. Also see https://gcc.gnu.org/wiki/GFortranBinaries for more information.

Note that the intent is that this Scons-based process will be replaced with one to run under meson in mid-2024. In the meantime, some older web pages discussing compiling GSAS-II may be of use:

 * https://subversion.xray.aps.anl.gov/trac/pyGSAS/wiki/CompilingWindows
 * https://subversion.xray.aps.anl.gov/trac/pyGSAS/wiki/InstallMacHardWay#CompilingFortranCode
 * https://subversion.xray.aps.anl.gov/trac/pyGSAS/wiki/InstallLinux#CompilingFortranCode

   
