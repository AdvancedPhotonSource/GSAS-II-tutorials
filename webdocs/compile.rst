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

The vast majority of GSAS-II's code is written in Python, but where
speed or complex analysis is
needed a small amount of code is written in other languages. There are
several small routines in Fortran used for speed, as well as the
complex codes for space group
analysis code (taken from the original GSAS package) and the DIFFaX
code, for faulted materials, has also been incorporated.
There is also one routine
for image analysis written in C and one for magnetic k-vector
analysis, written in Cython. There are also two small stand-alone
programs used for the NIST*LATTICE unit cell analysis capability.
All of these routines must be compiled to provide dynamic-link
libraries and executable programs, which we refer to collectively as the GSAS-II
binaries. Versions of these must match the operating system where they
will be run and must also match the version of Python and numpy module
that they will be used with. Most users will install versions of the GSAS-II
binaries that have been distributed with GSAS-II, but they can be
compiled by users and in some cases that will be necessary. The
documentation here discusses these files.

Note that there are two methods used for compiling GSAS-II. For Python
3.11 and earlier, a build process with a utility called `Scons` was used, but this
stopped working for GSAS-II with Python 3.12 and a new build process
using the `meson` tool was implemented. At present, there are two
branches for GSAS-II. The `master` branch uses Scons and the
`main` branch uses meson. The master branch is the current default
branch but will eventually be retired in favor of the newer `main`
branch. 

Supplied Binary Files
---------------------------

The GSAS-II binaries are supplied on GitHub as "release" files, 
https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/latest. In
that location, the files are in tar archives named `prefix_pX.X_nY.Y.tgz`

The supplied binaries are placed in a subdirectory name with name
`prefix`\ _p\ `X.X`\ _n\ `Y.Y` where
`prefix` is noted below and `X.X` is the Python version and `Y.Y` is the numpy

  * Windows-10: 64-bit Intel-compatible processors. [Prefix `win_64_`\ ]
  * MacOS: Intel processors. [Prefix `mac_64_`\ ]
  * MacOS: ARM processors, aka Apple Silicon (M1, etc). [Prefix `mac_arm_`\ ]
  * Linux: 64-bit Intel-compatible processors. [Prefix `linux_64_`\ ]
  * Linux: ARM processors (64-bit and 32-bit Raspberry Pi OS only).
    [Prefixes `linux_arm32_` and `linux_arm64_`\ ]

Some older binary files with combinations of older Python and
NumPy versions can be found in the older svn repository for GSAS-II:
https://subversion.xray.aps.anl.gov/trac/pyGSAS/browser/Binaries

Compiling with meson
---------------------------

Compiling GSAS-II binaries is quite simple. One needs to install the
Python meson and cython packages and a C compiler and the Gfortran
compiler. On Linux it probably best to use compilers supplied with the
dist using a commands such as `apt-get` or `yum`,
but these compilers can be installed via conda
from conda-forge and the latter does not require admin privs.
On windows and MacOS, the easist way to obtain them
is via their conda packages.

Windows::

  conda install meson cython gcc gfortran -c conda-forge

MacOS::

  conda install meson cython clang compilers  -c conda-forge

Linux::

   sudo apt-get gcc gfortran  # or use the yum command
   yum install gcc-gfortran
   conda install meson cython -c conda-forge
  
Once meson and the tools are installed, the following steps are needed
to build the GSAS-II binaries.

1. Download the GSAS-II sources (if not already done) and move to the directory::

   cd <...> # select where you wish to install GSAS-II
   git clone git@github.com:AdvancedPhotonSource/GSAS-II.git --depth 1 -b main G2 
   cd G2

2. Create a scratch directory to compile GSAS-II into::
     
     meson setup /tmp/GSASIIc

     Note that this command will fail if cython, gfortran and a c
     complier is not found. If the flang compiler is found, meson will
     use it, but the resulting binaries will not work properly. 
     
3. Move to the setup directory and compile::
     
     cd /tmp/GSASIIc
     meson compile

4. (A) Install the GSAS-II binaries so they can be used by the current user::

   meson compile local-install

   This command will copy the compiled files to `~/.GSASII/bin`, which
   is appropriate for when one user will access the GSAS-II
   program. It also allows multiple GSAS-II installations (should a
   user wish to keep multiple versions available).
   
4. (B) Or when GSAS-II is installed on a server, the GSAS-II binaries
can be placed with the GSAS-II source files installed with the git
command (into .../G2)::

   meson compile system-install

   If the first command used was `cd ~/software` then GSAS-II was
   installed into `~/software/G2` and the binaries will be installed into
   `~/software/G2/GSASII/bin`. 
   
5. Clean up:

   rm -rf /tmp/GSASIIc   

6. (Optional) Create shortcuts:

  Windows::
    
    python .../G2/GSASII/install/makeBat.py 

  Linux::
    
    python .../G2/GSASII/install/makeLinux.py 

  MacOS::
    
    python .../G2/GSASII/install/makeMacApp.py 

   
Compiling with Scons
---------------------------

Compilation with scons (as opposed to meson, as discussed above) is not
recommended and will be removed from GSAS-II in the future. It will
work only with Python 3.11 or older and only with the `master`
branch. GSAS-II will fail with Python earlier than 3.7 and may have
some errors even with Python 3.8.

The compilation process requires installation of the gcc and gfortran
compilers. Others will probablu not work. Also, the Python Scons
package must be installed into Python. compilation is done with
commands::

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
