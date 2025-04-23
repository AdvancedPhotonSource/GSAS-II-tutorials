.. raw:: html

	 <style> .clear {clear: both;}</style>

.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right
	   
==============================================
 Installing GSAS-II for code development
==============================================

.. tip::

   At the time this is being updated (April 22, 2025), the default branch for GSAS-II has been changed from ``master`` to a branch called ``main``. Development tasks should be made on the ``main`` branch rather than ``master``, but if changes are made to ``master`` they can be merged into ``main`` on a case-by-case basis if requested.

While bug fixes are sometimes applied directly to the ``main`` branch (and previously the ``master`` branch). The better way to make changes to GSAS-II is to make a private copy of the ``main`` branch on GitHub; this private copy is called a "fork." When you have a working version with the changes or additions that you want to make, you then issue an invitation to have your changes incorporated into the ``main`` branch. That invitation is called a "pull request" on GitHub, as you wish to have your changes pulled into the central GSAS-II version. You are very much encouraged to try your hand at working on improvements and fixes to GSAS-II.

This documentation section describes the steps needed to "fork a copy" of the GSAS-II repository in your own GitHub account. This means you will establish a private copy of GSAS-II. When you have reached a good point to share what you have done, and provide a "pull request" it allows the GSAS-II developers access to your working version so that the changes can be considered and potentially included into the main distribution.

Note that since you can have multiple copies of GSAS-II installed on your computer, or use the git command to quickly switch between different versions of GSAS-II in a single installation (branches with git), it is easy to get back to the distributed version of GSAS-II, so there is no danger of breaking GSAS-II in some way that would be hard to fix. At worst you can discontinue work on a messed up branch and start again. 

The steps needed to establish a development version of GSAS-II are outlined below. I am still learning my way around some of this, so let me know about problems or better ways to do things.

---------------------------------------------------
 Create a GitHub account
---------------------------------------------------

It is free. Use this link: https://github.com/signup?source=login. 

---------------------------------------------------
 Establish a connection
---------------------------------------------------

You will need to establish an authorized connection between your computer and GitHub in order to have the ability to send files from your computer to GitHub.  While the files in GSAS-II are all publically available and do not need a GitHub account to be accessed, but if you have made changes and want to allow others to see what you have done, you need to provide authorization for git to upload those changed files to GitHub. This requires that the git program be given access your GitHub account. There are multiple ways to do this, as discussed here: https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github.

The method I have used has been to use ssh authentication. In a nutshell this requires creating a ssh public key (if one does not already exist) and providing that key to GitHub. To see if you already have an ssh key, see this: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys. If you do not, see https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent.

To upload the key you generated to GitHub, see this page: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account 

   For Windows with tortoiseGit and its default PuTTy ssh program, use program PuTTygen. If a key has been generated it will be shown; if not pressing the Generate button will create this. The public key can be copied and pasted into the Settings/SSH and GPG keys setting page. 
   
---------------------------------------------------
 create a fork of GSAS-II
---------------------------------------------------

There is GitHub documentation on creating a fork here: https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo
   
---------------------------------------------------
 Install GSAS-II from your forked copy
---------------------------------------------------

There are two choices here, you can create a GSAS-II installation directly from GitHub using the a git clone command. Or, you can install GSAS-II using one of the standard  installation methods (`see here <install.html>`_) and then switch the "upstream repository" associated with that to the forked copy.

Install directly from your forked copy
---------------------------------------------------

If you will clone GSAS-II directly, you will need to consider how git and Python are installed. One way to do this is to use the Python installed with one copy of GSAS-II, installed with the gsas2main self-installer, to run another. To do that you will need to use a command to make that Python available, as below.

  For Windows, if GSAS-II is installed at location ``C:\Users\Me\gsas2main`` then use this command to setup Python::

      C:\Users\Me\gsas2main\Scripts\activate

  For Linux and MacOS, if GSAS-II is installed at location ``~/G2/g2main`` then use this command to setup Python::

      source ~/G2/g2main/bin/activate 

  Note that once the above command has been run, in addition to the ``python`` command, one can also run ``git`` and ``conda``.

To clone GSAS-II from your forked copy use commands similar to the following::
    
    mkdir dev
    cd dev
    git clone git@github.com:MyRepo/GSAS-II.git
    cd GSAS-II

This will create directory ``dev/GSAS-II`` with a copy of your fork. The GSAS-II Python files will be in ``dev/GSAS-II/GSASII``. Note that when the GSAS-II Python files are cloned from a GitHub repo, the GSAS-II binary files are not be downloaded. However, when GSAS-II is first run, it will provide an opportunity to do this, provided you have used supported combinations of Python and numpy. If not, you may compile the binary files yourself,
`as described here <https://advancedphotonsource.github.io/GSAS-II-tutorials/compile.html>`_. The
:ref:`section below on use of pixi <pixi installation>` provides an alternate way install GSAS-II including compilation of the binaries. It is both very quick and quite convenient. 

To run this copy of GSAS-II, you will use a command such as::

    python GSASII/GSASII.py
 
Use of that command can get tiresome, so you may want to set up a shortcut method to access your development version. Note that the GSAS-II installers (gsas2main &  gsas2pkg) run installation scripts to create shortcuts. This can also be done manually for your development version. See discussion of ``makeMacApp.py``, ``makeLinux.py`` and ``makeBat.py`` (for MacOS, Linux and Windows, respectively) in the `Developer's Documentation <https://gsas-ii.readthedocs.io/en/latest/GSASIIscripts.html#gsas-ii-misc-scripts>`_. If you will use your development version of GSAS-II for scripting GSAS-II, see this `note on scripting shortcuts <https://gsas-ii.readthedocs.io/en/latest/GSASIIscriptable.html#shortcut-for-scripting-access>`_.     

Converting an http: installation to ssh 
---------------------------------------------------

Note that if you set up for ssh authorization and clone using http rather than ssh, using a command like this::
    
      git clone https://github.com/MyRepo/GSAS-II.git

  you will need to change the upstream repo, as described in the next section.


Repurpose a standard GSAS-II installation
---------------------------------------------------

A potentially simpler way to set up a development version of GSAS-II is to run one of the installation scripts that are typically used inside the self-installers. 
This can greatly simply installation of the GSAS-II source code, but you then need to make some changes to work using your forked copy of GSAS-II. This requires changing the git settings to you to write your changes back to your copy of the repository and to access multiple branches.

  This can be done by editing the ``.../GSAS-II/.git/config`` file from::

   [remote "origin"]
	url = https://github.com/AdvancedPhotonSource/GSAS-II.git
	fetch = +refs/heads/master:refs/remotes/origin/master

  to::

   [remote "origin"]
	url = git@github.com:MyPersonalRepo/GSAS-II.git
	fetch = +refs/heads/*:refs/remotes/origin/*

  These changes can be done directly by editing this file. Alternately, these git commands will do the same thing::

     git config remote.origin.url git@github.com:MyPersonalRepo/GSAS-II.git 
     git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"

---------------------------------------------------
 Make changes and submit them
---------------------------------------------------

You are strongly encouraged to create a separate branch for each development project that you have with GSAS-II.

  The command to do this is::

     git checkout -b g2newfeature

  Note that this creates a branch named ``g2newfeature`` -- do choose a better name.

When your changes are complete and you are ready to communicate them back, you will commit them locally and use ``git push`` to upload them to GitHub. From the web interface to GitHub you can then submit that branch as a pull request to the main GSAS-II repository. Once you have submiited your pull request, you likely will want to switch to a different branch to do any further development work, as if changes are uploaded for the branch used for the pull request, those changes will be added to the code in the pull request.

.. _pixi installation:
   
==============================================
 Using Pixi to install GSAS-II
==============================================

The code in the ``main`` includes setup files for `Pixi <https://pixi.sh>`_, which is a package management tool for developers.  If one uses Git to install the GSAS-II files and installs the Pixi software, GSAS-II can be configured and installed very simply.
It is particularly convenient for GSAS-II software development. 
There are many ways to install Pixi, as listed `here <https://pixi.sh>`_, or by using the ``conda install pixi`` command, or homebrew, etc. 

Once pixi is installed, it can be used to setup and run GSAS-II, with commands as described below. These commands should be run from the ``<G2>/GSASII/pixi`` directory:

Linux/MacOS::
  
    cd <...>/GSASII/pixi

Windows:: 

    cd <...>\GSASII\pixi
    
---------------------------------------------------
GSAS-II installation via pixi
---------------------------------------------------

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

---------------------------------------------------
Commonly-used pixi commands
---------------------------------------------------

After one of the above install commands is used, the following commands can be used:

``pixi run test``

    Runs the GSAS-II self-test suite (takes 1-2 minutes typically to complete.)
    See :ref:`example output here<example_pytest_output>`.

``pixi run ui``

    Runs the GSAS-II GUI. 

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

