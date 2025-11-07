.. raw:: html

	 <style> .clear {clear: both;}</style>

.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right
	   
.. index:: Installation via pip

.. _pip installation:

Overview: Installing GSAS-II with pip
=======================================

The "standard" method for installing Python and packages uses the
Python package installer and downloads packages from the Python
Package Index (PyPI). GSAS-II is not available on PyPI, but can still
be installed via pip. If you use pip, you are recommended to install GSAS-II into its
own virtual environment, so that it is independent of any other
software installations using Python.
For the commands below, the  ``python -m venv ~/G2-env``
and the ``source ~/G2-env/bin/activate`` create a virtual environment
in file `G2-env` in the user's home directory and then activate
that.

The advantage of installing GSAS-II with pip is that GSAS-II will be
fully integrated with Python. Python command such as ``import
GSASII.GSASIIscriptable`` will work without modifying the Python
path. Also, pip creates a shell command (``GSAS-II``) to start the GSAS-II
GUI. The disadvantage is that updating GSAS-II will require rerunning pip.

For Linux, a pip installation works quite well for scripting use,
particularly on HPC installations, where Python and compilers are
likely already installed, but for GUI use this installation process
will usually require considerable package downloads and then a build
for wxpython, which can require an hour or more to run.
Some Linux dists provide an install kit for wxpython,
which would be quick and easy to install, but pip will not find that.
Note that a possible alternative to the downloads and
compilation requires finding a matching wxpython wheel for your Linux version (see 
https://extras.wxpython.org/wxPython4/extras/linux/) and use that to
install (see https://wxpython.org/pages/downloads/ for details). 

Note that the commands below download and install GSAS-II in multiple
steps::

    git clone --depth 1 https://github.com/AdvancedPhotonSource/GSAS-II.git ~/G2
    cd ~/G2
    pip install .[gui,useful]

There is a single-step alternative to this, which downloads GSAS-II
with git and then performs the installation. This one step replaces the
three commands above::
    
    pip install GSAS-II[gui,useful] git+https://github.com/AdvancedPhotonSource/GSAS-II.git

I do not recommend using this because if the initial three steps are
used, GSAS-II can quickly be updated with the following commands. The
`git pull`
command will then only download the files that need an update not the
entire package::

    cd ~/G2
    git pull 
    pip install ~/G2[gui,useful]

Note that the default pip installation of GSAS-II installs the minimum
number of packages needed to run for scripting. As described in
the developers manual [Python requirements section]
(https://gsas-ii.readthedocs.io/en/latest/packages.html#python-requirements),
there are several optional packages that GSAS-II uses for some of its 
functionality and without these additional packages certain commands or options
will not work. An example is that GSAS-II can access content from the
internet, but only if the Python `requests` package is installed.
All of these optional packages can be installed by pip when GSAS-II is
installed by including ``[useful]`` on the command. Likewise, to
install GSAS-II with the Python packages required for running the GUI,
use ``[gui]`` and for both use ``[gui,useful]``. 

Examples of pip installation sequences
=======================================

Below are some sample commands that have been used to install GSAS-II
using pip on a few key OS versions.
    
Linux RHEL 9.6
----------------

These commands require admin access (sudo authorization)::

    sudo dnf install python3.11-devel
    sudo dnf install pip
    sudo dnf install gcc-c++
    sudo dnf install gfortran
    sudo dnf install libjpeg-turbo-devel libtiff-devel gstreamer1-plugins-base-devel libnotify-devel freeglut-devel  gtk3-devel.x86_64 SDL2-devel.x86_64

These commands can be run by any user account::
    
    python3.11 -m venv ~/G2-env
    source ~/G2-env/bin/activate
    pip install --upgrade pip
    pip install wxpython
    git clone --depth 1 https://github.com/AdvancedPhotonSource/GSAS-II.git ~/G2
    cd ~/G2
    pip install .[gui,useful]

RHEL 9.6 for scripting only
------------------------------

These commands require admin access (sudo authorization)::

    sudo dnf install python3.11-devel
    sudo dnf install pip
    sudo dnf install gfortran

These commands can be run by any user account::
    
    python3.11 -m venv ~/G2-env
    source ~/G2-env/bin/activate
    pip install --upgrade pip
    git clone --depth 1 https://github.com/AdvancedPhotonSource/GSAS-II.git ~/G2
    cd ~/G2
    pip install .[useful]

Optionally test the GSAS-II installation with these commands. See
below for interpreting the results::

    pip install pytest
    pytest

    
Linux Mint 21.2
--------------------------------

These commands require admin access (sudo authorization)::

    sudo apt-get update
    sudo apt install python3 pip python3-venv
    sudo apt install gfortran
    sudo apt install git
    sudo apt install dpkg-dev build-essential python3-dev freeglut3-dev
    sudo apt install libgl1-mesa-dev libglu1-mesa-dev libgstreamer-plugins-base1.0-dev
    sudo apt install libgtk-3-dev libjpeg-dev libnotify-dev libpng-dev libsdl2-dev
    sudo apt install libsm-dev  libtiff-dev libwebkit2gtk-4.0-dev  libxtst-dev

These commands can be run by any user account::

    python3 -m venv ~/G2-env
    source ~/G2-env/bin/activate
    git clone --depth 1 https://github.com/AdvancedPhotonSource/GSAS-II.git ~/G2
    cd ~/G2
    pip install wxpython
    pip install .[gui,useful]

Mint 21.2 for scripting only
--------------------------------

These commands require admin access (sudo authorization)::

    sudo apt-get update
    sudo apt install python3 pip python3-venv
    sudo apt install gfortran
    sudo apt install git

These commands can be run by any user account::

    python3 -m venv ~/G2-env
    source ~/G2-env/bin/activate
    git clone --depth 1 https://github.com/AdvancedPhotonSource/GSAS-II.git ~/G2
    cd ~/G2
    pip install .[useful]

Optionally test the GSAS-II installation with these commands::

    pip install pytest
    pytest

The output will look something like :ref:`this example output<example_pytest_output>`
where each of the 27 dot (`.`) characters above represents a test that ran
successfully. Any test that fails will show as a `F`. At present one
warning is generated that can be ignored. 

MacOS 14.3.1 (Sonoma)
------------------------------

These commands require admin access::

    xcode-select --install
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
    echo >> ~/.zprofile
    echo 'eval "$(/usr/local/bin/brew shellenv)"' >> ~/.zprofile
    eval "$(/usr/local/bin/brew shellenv)"
    brew install gfortran
    brew install git
    brew install python@3.13

These commands can be run by any user account::

    python3.13 -m venv ~/G2-env
    source ~/G2-env/bin/activate
    pip install --upgrade pip
    git clone --depth 1 https://github.com/AdvancedPhotonSource/GSAS-II.git ~/G2
    cd ~/G2
    pip install wxpython
    pip install ".[gui,useful]"

Start GSAS-II from the command-line by typing `GSAS-II` in the
terminal. To install it on dock, run this command::

    python ~/G2/GSASII/install/makeMacApp.py

The command will create an App to run GSAS-II and display it in the
finder. The App can be run from that location or create an alias to
move to another folder; do not move the App itself to another
location. 
    
Windows 11
------------------------------

I do not see a pressing need to use pip to install GSAS-II for windows
as there are plenty of other mechanisms that work just as well, if not
better. In any case, 
I was not able to get gfortran working properly with Windows in my
most recent attempt. To
install via pip would require
the following packages to be installed:

* A Python installation kit, such as
  https://www.python.org/ftp/python/3.13.9/python-3.13.9-amd64.exe
  from https://www.python.org/downloads/ and run the downloaded .exe.
  Click on "Add python.exe to
  PATH" at the bottom of the window before pressing "Install Now".

* git, using
  https://github.com/git-for-windows/git/releases/download/v2.51.2.windows.1/Git-2.51.2-64-bit.exe
  or more recent from https://git-scm.com/download/win. Run the
  downloaded .exe file. The default installation options should all be
  fine. 

* the gfortran and gcc compilers. There is plenty of information and
  packages for this (see
  https://fortran-lang.org/learn/os_setup/install_gfortran/), but
  Windows blocks downloading some of them. 
  I was not able to get one to install and correctly configure for linking.

Once that is done in a cmd.exe window use the following commands::

    python -m venv G2-env
    G2-env\Scripts\activate
    python -m pip install --upgrade pip
    pip install wxpython
    git clone --depth 1 https://github.com/AdvancedPhotonSource/GSAS-II.git G2
    cd G2
    PATH=%PATH%;%HOMEPATH%\gcc\bin
    pip install .[gui,useful]


