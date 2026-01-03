.. raw:: html

	 <style> .clear {clear: both;}</style>

.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right

.. index:: Installation via pixi

.. _pixi installation:
   
==============================================
Overview: Installing GSAS-II with pixi
==============================================

Due to royalty issues with use of Anaconda, Inc. conda packages (which
GSAS-II does not use; GSAS-II only uses conda-forge packages, which are
non-proprietary). Some sites are encouraging use of `pixi
<https://pixi.sh>`_, rather than
conda. The pixi installer can be used directly after downloading
GSAS-II from the GitHub site. The pixi program makes installation of
GSAS-II very easy. It installs Python and all packages
needed for GSAS-II and it also compiles GSAS-II locally, rather than
downloading pre-built binaries, which is of particular value for
Linux. It is also helpful for GSAS-II development (see below).

Installation of GSAS-II with pixi requires a few prerequisite steps,
depending on the platform. Note that on Windows and MacOS, pixi
installs gfortran, but on Linux this must be done before running pixi (typically with a
Linux package manager such as apt or dnf, etc.).

These are the steps that are typically needed to install GSAS-II using
pixi.:

* installation of the pixi program
* on Linux, installation of the gfortran (and gcc) compiler
* on MacOS, installation of Xcode command-line tools, needed to run compilers.
* installation of git (on MacOS this is accomplished via installation
  of Xcode command line tools)

Once the above is done, git is used to install the GSAS-II files, which
contain setup files needed by pixi. These commands will then install
GSAS-II, will run self-tests and will start the GUI::

        cd <install-location>
        git clone --depth 1 https://github.com/AdvancedPhotonSource/GSAS-II.git GSASII
        cd GSASII
        cd pixi
        pixi run install
        pixi run test
        pixi run ui

Note that ``pixi run install-editable`` (Linux/MacOS) or ``pixi run
install-editable-win`` (on Windows) is frequently a better choice than
``pixi run install``,  as discussed in the next section. 
 
        
---------------------------------------------------
GSAS-II pixi commands
---------------------------------------------------

More detailed descriptions of some commonly used pixi commands follow: 

``pixi run install``

     This will install GSAS-II into the ``pixi/.pixi`` directory where it will be
     used by exclusively by pixi. The GSAS-II Fortran, etc. files will be compiled
     and will be placed with other executable files used by Python.

``pixi run install-editable`` (Linux/MacOS)

``pixi run install-editable-win`` (on Windows)
     
     These commands will set up to run GSAS-II in the directory where
     the files are originally
     located. This is ideal for code development, as changes made in Python code will
     immediately effect operation, as soon as GSAS-II is restarted and git commands can
     be used to upload changes to GitHub. Likewise, git can be used to
     download updates, potentially using the self-update menu commands
     (Help/Update) that are part of GSAS-II's GUI. When the ``pixi run
     install`` command is used, one must after making changes or after
     use a manual update with git in order to access the changed
     files. 

After one of the above install commands is used, the following commands can be used:

``pixi run test``

    Runs the GSAS-II self-test suite (takes 1-2 minutes typically to complete.)
    See :ref:`example output here<example_pytest_output>`.

``pixi run ui``

    Starts the GSAS-II GUI. 

``pixi run python``

    Starts Python with the GSAS-II environment established. 

``pixi shell``

    Starts a shell (bash, cmd.exe,...) where conda, python, etc. are available to run.
    The GSAS-II environment is setup. This is a useful command for developing
    or running GSASIIscriptable scripts. 

---------------------------------------------------
Use of non-default pixi environments
---------------------------------------------------

By default, the commands above will install and run GSAS-II with
Python 3.13 (at the time this is written), but pixi can also set up
GSAS-II to run with alternate Python versions. Available options are
``py310``, ``py311``, and ``py312``. To use an alternate environment,
it should be added to every command, such as::
  
  pixi run -e py311 install-editable-win
  pixi run -e py311 test
  pixi run -e py311 ui
  pixi shell -e py311

---------------------------------------------------
Updating GSAS-II After pixi Installation
---------------------------------------------------

GSAS-II is updated very frequently, both to address bugs and to add
new features. You are recommended to update at least monthly and if
you encounter problems, before reporting that problem as a potential
issue. (It may have already been fixed.)

If you use the ``pixi run install`` command, you will need to issue the
following commands in a terminal window (Linux/Mac) or cmd.exe window
(Windows) to update GSAS-II::

        cd <install-location>
        cd GSASII
        cd pixi
        git pull
        pixi run install

If you used ``pixi run install-editable-win`` or ``pixi run
install-editable``  to install GSAS-II, the ``pixi run...`` command
does not need to be repeated. 
  
---------------------------------------------------
Use of pixi for GSAS-II Development
---------------------------------------------------
If you are interested in developing GSAS-II, where you will contribute
bug fixes and/or improvements to the codebase, you will likely want to make some
relatively minor changes to the above installation process: For git:

* Depending on how you set up authorization to write to GitHub, you
  wish to use ssh rather than https access (``git@github.com:<repo>``
  rather than ``https://github.com/<repo>``).

* You will want to clone from your own fork of the GSAS-II repo
  rather than the main repository
  (``https://github.com/<your-fork>/GSAS-II.git``. or
  ``git@github.com:<your-fork>/GSAS-II.git`` rather than the
  AdvancedPhotonSource repo.)

* You may want to increase the ``--depth`` value or
  even omit that option, if you don't mind the increased amount of
  download time,  

With the pixi command:

* use ``install-editable`` (Windows, ``pixi run install-editable-win``) command
  rather than the ``install`` command. This means that the git-installed
  code is used to run GSAS-II, a copy made by pixi to the Python
  tree. With this "editable" option any changes you make to the
  GSAS-II codebase will be utilized as soon as the code is rerun. With
  use of ``install``, the ``pixi run install`` step must be rerun for any
  changes to be tested.
  Likewise, when the ``install-editable`` or ``install-editable-win``
  options are used, GSAS-II can be updated from the Help menu.  

Thus, for development, variants on the following commands are
recommended::
  
        cd <install-location>
        git clone --depth 500 git@github.com:<your-fork>/GSAS-II.git GSASII
        cd GSASII
        cd pixi
        pixi run install-editable
        pixi run test
        pixi run ui
  
---------------------------------------------------
Example use of pixi on different Operating Systems
---------------------------------------------------

MacOS
==================

Note that pixi is now configured both for newer "Apple Silicon" (ARM)
processor computers (M1, M2,...) as well as older Intel Macs. 

In a terminal window run the next command. It will open a window
asking you to confirm that you want to download and install the xcode
command-line tools. I believe if you run this from a non-admin account
you will be asked for to authorize this with an admin password::

    xcode-select --install

The following commands should also be run in a terminal window, but do
not require admin access::

    curl -fsSL https://pixi.sh/install.sh | bash
    exec zsh

With the above complete, use these commands to install GSAS-II::    
    
    git clone --depth 1 https://github.com/AdvancedPhotonSource/GSAS-II.git ~/G2
    cd ~/G2/pixi
    pixi run install
    pixi run test
    pixi run ui


Windows 11
==================

To install GSAS-II for windows with pixi, two tools are needed as
prerequisites, pixi and git. 

* Install git, using
  https://github.com/git-for-windows/git/releases/download/v2.51.2.windows.1/Git-2.51.2-64-bit.exe
  or more recent from https://git-scm.com/download/win. Run the
  downloaded .exe file. The default installation options should all be
  fine. This can be done using a browser or the following commands can
  be used in a cmd.exe window::

    curl -O -L https://github.com/git-for-windows/git/releases/download/v2.51.2.windows.1/Git-2.51.2-64-bit.exe
    .\Git-2.51.2-64-bit.exe

* install pixi. From a browser pixi it should be possible to download
  and install this file:
  https://github.caom/prefix-dev/pixi/releases/latest/download/pixi-x86_64-pc-windows-msvc.msi
  but I was unable to do this due to Windows security "features", but
  the following commands in a cmd.exe window did work::

    powershell -ExecutionPolicy ByPass -Command "irm -useb https://pixi.sh/install.ps1 | iex"
    
* Close the cmd.exe window (to get access to the newly-installed git
  and pixi programs) and open new cmd.exe window where these commands are entered::

    git clone --depth 1 https://github.com/AdvancedPhotonSource/GSAS-II.git G2
    cd G2\pixi
    pixi run install
    pixi run test
    pixi run ui

    
Linux Mint 21.2
==================

These commands should be run in a terminal, The first two require admin
access (sudo authorization). If you need to login to a separate
account to run sudo commands (which I consider a good security practice), you will
want to run only those first two commands from the admin account. The
``curl`` command to install pixi should be run from the account where
you will run GSAS-II::

    sudo apt-get update
    sudo apt install gfortran git
    curl -fsSL https://pixi.sh/install.sh | bash

Close the terminal window (to get access to the newly-installed pixi
program) and open a new terminal window where these commands are
entered::
  
    git clone --depth 1 https://github.com/AdvancedPhotonSource/GSAS-II.git ~/G2
    cd ~/G2/pixi
    pixi run install
    pixi run test
    pixi run ui

Ubuntu 22.04.2
----------------

See the instructions above for Linux Mint 21.2, except that curl needs
to be installed, so the second command should be changed to::

  sudo apt install gfortran git curl

  Linux RHEL 9.6
==================

The first command requires admin access (sudo authorization).  If you
need to login to a separate account to run sudo commands (which I
consider a good security practice), you will 
want to run this command from the admin account::

   sudo dnf install gfortran

The second command that downloads and installs pixi should be run from
the account where you will run GSAS-II::

    curl -fsSL https://pixi.sh/install.sh | bash
   
Close the terminal window (to get access to the newly-installed pixi
program) and open a new terminal window where these commands are
entered::
  
    git clone --depth 1 https://github.com/AdvancedPhotonSource/GSAS-II.git ~/G2
    cd ~/G2/pixi
    pixi run install
    pixi run test
    pixi run ui
