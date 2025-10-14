.. index:: Installing with pixi

.. _pixi installation:
   
==============================================
 Using Pixi to install GSAS-II
==============================================

The code in the ``main`` includes setup files for `Pixi <https://pixi.sh>`_, which is a package management tool for developers.  If one uses Git to install the GSAS-II files and installs the Pixi software, GSAS-II can be configured and installed very simply.
It is particularly convenient for GSAS-II software development. 
There are many ways to install Pixi, as listed `here <https://pixi.sh>`_, or by using the ``conda install pixi`` command, or homebrew, etc. 

Once pixi is installed, it can be used to setup and run GSAS-II, with commands as described below. These commands download GSAS-II from GitHub, install it, including compiling the files locally, then runs the self-tests and then finally starts the GSAS-II GUI:: 

        cd <install-location>
        git clone --depth 1 git@github.com:AdvancedPhotonSource/GSAS-II.git
        cd GSAS-II/pixi
        pixi run install
        pixi run test
        pixi run ui

The pixi program makes all this very easy. Developers will likely want to clone from their own fork of the repo (see above) and may want to use variants on these commands, such as add `--no-single-branch` so that all branches are available and/or change the `--depth` value or even omit that option.  (Any of these increase the download time significantly.)
Also note the `install-editable` or `install-editable-win` options below. This allows that git-installed code is used to run GSAS-II rather than copies. With this "`editable" option you can make changes to GSAS-II and then restart it and see the impact of your changes immediately [with a bit of tampering, sometimes one can use `importlib.reload()` and see changes as soon as they are saved]. If the normal install process is used, the changes will be seen only after repeating the `pixi run install` step.

---------------------------------------------------
GSAS-II pixi commands
---------------------------------------------------

Details on commonly-used commands with pixi follow: 

``pixi run install``

     This will install GSAS-II into the ``pixi/.pixi`` directory where it will be
     used by exclusively by pixi. The GSAS-II Fortran, etc. files will be compiled
     and will be placed with other executable files used by Python.

``pixi run install-editable`` (Linux/MacOS)

``pixi run install-editable-win`` (on Windows)
     
     This will set up to run GSAS-II in the directory where the files are originally
     located. This is ideal for code development as changes in Python code will
     immediately be seen as soon as GSAS-II is restarted and git commands can
     be used to upload changes to GitHub. Note the slightly different version of
     this command for Windows.

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

By default, the commands above will install and run GSAS-II with Python 3.13 (at the time this is written), but pixi can also setup GSAS-II to run with alternate Python versions. Available options are ``py310``, ``py311``, and ``py312``. To use an alternate environment, it should be added to every command, such as
``pixi run -e py311 install-editable-win``, 
``pixi run -e py311 test``, 
``pixi run -e py311 ui`` or 
``pixi shell -e py311``.

