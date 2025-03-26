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

The GSAS-II binaries are supplied on GitHub as "release" files, in
https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/latest. In
that location, the files are in tar archives named as
`prefix`\ _p\ `X.X`\ _n\ `Y.Y` where
`prefix` is noted below and `X.X` is the Python version and `Y.Y` is
the numpy version:

Prefix naming:

  * Windows-10: 64-bit Intel-compatible processors. [Prefix `win_64_`\ ]
  * MacOS: Intel processors. [Prefix `mac_64_`\ ]
  * MacOS: ARM processors, aka Apple Silicon (M1, etc). [Prefix `mac_arm_`\ ]
  * Linux: 64-bit Intel-compatible processors. [Prefix `linux_64_`\ ]
  * Linux: ARM processors (64-bit and 32-bit Raspberry Pi OS only).
    [Prefixes `linux_arm32_` and `linux_arm64_`\ ]

Some older binary files with combinations of older Python and
NumPy versions can be found in the older svn repository for GSAS-II:
https://subversion.xray.aps.anl.gov/trac/pyGSAS/browser/Binaries

Compiling with meson for Linux/MacOS
--------------------------------------------

Compiling GSAS-II binaries is quite simple on Linux and MacOS and a
bit more complex on Windows.
One needs to install the
Python meson and cython packages and a C compiler and the GFortran
compiler.

On Linux it probably best to use compilers supplied with the
dist using a commands such as `apt-get` or `yum`,
but it is also possible to install these compilers via conda
from conda-forge. The conda route has the advantage of not requiring admin privs.
For Linux, one can add the extra packages needed for compilation to
the Python environment used by GSAS-II. Below it is assumed that the
Python environment is managed with conda, but on Linux it is also
possible to utilize the distribution-supplied packages and/or PyPi
(pip). It is also possible to use separate environments for
compilation and for running GSAS-II. 

For Mac, while there are several ways to potentially install the tools
needed for compilation (for example homebrew) and one can use separate
environments for compilation and for running GSAS-II, below a single
environment is used and all software is loaded via conda.

Note that if the gsas2full installer is used, this can replace
steps (1) and (3), below. In that case use command::

    source .../g2full/bin/activate

to activate Python/conda, where `.../g2full` is the location where gsas2full was
installed. And in place of step (3) use command::

    cd .../g2full/GSAS-II
    
where again `.../g2full` is the location where gsas2full was installed. 

(1) Install an initial, bare-bones Python environment can be installed
using the miniforge installer from conda-forge at
https://github.com/conda-forge/miniforge/releases/latest. Then
activate Python/conda as instructed by the installer (or use command::

       source ~/miniforge3/bin/activate
where `~/miniforge3` is the location where miniforge was installed.)
Then use the conda command to install the following packages to run GSAS-II:

  python, numpy, matplotlib, scipy, wxpython, pyopengl, imageio, h5py,
  hdf5, pillow, requests, pycifrw, pybaselines, git, gitpython, conda

(see `the GUI requirement section of the Developers manual 
<https://gsas-ii.readthedocs.io/en/latest/packages.html#gui-requirements>`_.)

(2) Install the Python build routines and the compilers:

MacOS::

  conda install python numpy meson cython clang compilers git -c conda-forge

Linux::

   sudo apt-get gcc gfortran git # or use the yum command:
   yum install gcc-gfortran git

and for Linux::
   conda python numpy install meson cython -c conda-forge

Note that the GSAS-II binaries will be compiled to work with a
specific version of Python and numpy, if you have more than one conda
environment, and will use a different environment to compile vs. run
GSAS-II, you may want to pin the Python and numpy versions above by
specifying them in the conda command (such as using `python=3.13` and
`numpy=2.2` in place of `python` and `numpy` above) to match the
environment where GSAS-II will be run.
   
(3) Download the GSAS-II sources (if not already done) and move to the directory::

   cd <...> # select where you wish to install GSAS-II
   git clone https://github.com/AdvancedPhotonSource/GSAS-II.git --depth 1 -b main G2 
   cd G2

(4) Create a scratch directory to compile GSAS-II into::
     
     meson setup /tmp/GSASIIc

   Note that this command will fail if cython, GFortran and a c
   complier is not found. If the flang compiler is found, meson will
   use it, but the resulting binaries will not work properly. 
     
(5) Move to the setup directory and compile::
     
     cd /tmp/GSASIIc
     meson compile

(6) There are two choices for how to install the GSAS-II binaries to
   where they can be found by the software. If only one user will use 
   GSAS-II, use option (A), which also allows multiple GSAS-II installations to share a
   single set of binaries (should a user wish to keep multiple
   versions available). When GSAS-II is installed on a server
   or possibly multiple versions of GSAS-II will be installed that
   need to have different versions of the binaries, use option (B) and
   the GSAS-II binaries will be placed with the GSAS-II source files. 

  (A) Install the GSAS-II binaries so they can be used by the current user::

     meson compile local-install

   This command will copy the compiled files to `~/.GSASII/bin`, which
   is appropriate for when one user will access the GSAS-II
   program. It also allows multiple GSAS-II installations (should a
   user wish to keep multiple versions available).

  (B) Or when GSAS-II is installed on a server, the GSAS-II binaries
      can be placed with the GSAS-II source files installed with the
      git command (into .../G2)::

       meson compile system-install

   If the first command used was `cd ~/software` then GSAS-II was
   installed into `~/software/G2` and the binaries will be installed into
   `~/software/G2/GSASII/bin`. 
   
(7) (Optional) Clean up:

   rm -rf /tmp/GSASIIc

(8) (Optional) Run Self-tests::

     conda activate base
     conda install pytest
     cd .../G2
     python -m pytest .../G2/tests

  Note that `base` above may need to be replaced with the name of the
  environment that was used if not base and `.../G2` here and below will be the
  location used to install GSAS-II in step (2).

(9) (Optional) Create shortcuts:

  Linux::
    
    python .../G2/GSASII/install/makeLinux.py 

  MacOS::
    
    python .../G2/GSASII/install/makeMacApp.py 

Compiling with meson for Windows
--------------------------------------------

Compiling GSAS-II binaries is bit more complex on Windows because
separate Python environments *must* be used for compilation and
running GSAS-II (it appears that inclusion of git and GFortran in the
same installation causes problems with accessing libraries needed by the compiler). 
There are other ways potentially to install the tools
needed for compilation, but use of conda will be much simpler, but
will require use of command-line commands (in a cmd.exe window, the
commands have not been worked out if they will done with PowerShell). 

Note that if the gsas2full installer is used, this can replace
steps (1) and (2), below. In that case, use command::

    ...\g2full\Scripts\activate

to activate Python/conda, where `...\\g2full` is the location where gsas2full was
installed. And in place of step (3) use command::

    cd ...\g2full\GSAS-II
    
where again `...\\g2full` is the location where gsas2full was installed. 

1. Install miniforge

  An initial, bare-bones Python environment can be installed
  using the miniforge installer from conda-forge at
  https://github.com/conda-forge/miniforge/releases/latest. Run the
  downloaded `.exe` file. Once that has completed use command::

        ...\miniforge3\Scripts\activate

  where `...\\miniforge3` is the location where miniforge was
  installed to enable the Python/conda environment. Or in the start
  menu use the "Start miniforge prompt" command which does the same
  thing.

  Use this command to install the following packages to run GSAS-II
  (note this is a very long line)::

    conda install python numpy matplotlib wxpython pyopengl scipy git gitpython PyCifRW pillow conda requests hdf5 h5py imageio zarr xmltodict pybaselines seekpath pywin32 -c conda-forge -y
 
  (see `the GUI requirement section of the Developers manual 
  <https://gsas-ii.readthedocs.io/en/latest/packages.html#gui-requirements>`_
  for more info.)

2. Download the GSAS-II sources (if not already done) and move to the directory::

     cd <...> # select where you wish to install GSAS-II
     git clone https://github.com/AdvancedPhotonSource/GSAS-II.git --depth 1 -b main G2 
     cd G2

3. Install the Python build routines and the compilers. Note that this
   is done in separate environment that is located in directory
   `..\\compile` relative to GSAS-II::
     
     conda create -p ..\compile meson cython gcc gfortran python numpy -c conda-forge -y

 4. Create a scratch directory to compile GSAS-II into::
     
    conda activate ..\compile
    meson setup ..\tmp
     
5. Move to the setup directory and compile::
     
     cd ..\tmp
     meson compile

6. There are two choices for how to install the GSAS-II binaries to
   where they can be found by the software. If only one user will use 
   GSAS-II, use option (A), which also allows multiple GSAS-II installations to share a
   single set of binaries (should a user wish to keep multiple
   versions available). When GSAS-II is installed on a server
   or possibly multiple versions of GSAS-II will be installed that
   need to have different versions of the binaries, use option (B) and
   the GSAS-II binaries will be placed with the GSAS-II source files. 
 
  (A) Install the GSAS-II binaries so they can be used by the current user::

     meson compile local-install

   This command will copy the compiled files to `.GSASII\\bin` in the
   Home directory (usually `c:\\Users\\<your name>`), which
   is appropriate for when one user will access the GSAS-II
   program.
   
  (B) Or when GSAS-II is installed on a server, the GSAS-II binaries
      can be placed with the GSAS-II source files::

       meson compile system-install

   If the first command used was `cd software` then GSAS-II was
   installed into `software\\G2` and the binaries will be installed into
   `software\\G2\\GSASII\\bin`. 
   
7. Clean up::

     cd ..
     rmdir /s tmp
     rmdir /s compile

8. Create shortcuts::
    
    python G2\GSASII\install\makeBat.py 

9. (Optional) Run Self-tests::

     conda activate base
     conda install pytest
     python -m pytest G2\tests


Compiling with Scons
---------------------------

Compilation with scons (as opposed to meson, as discussed above) is not
recommended and will be removed from GSAS-II in the future. It will
work only with Python 3.11 or older and only with the `master`
branch. Do not use GSAS-II will fail with Python earlier than 3.7 and may have
some errors even with Python 3.8.

The compilation process requires installation of the gcc and GFortran
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
