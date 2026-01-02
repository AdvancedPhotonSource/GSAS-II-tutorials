.. raw:: html

	 <style> .clear {clear: both;}</style>

.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right
	   
==============================================
 Installing GSAS-II for code development
==============================================

While the main developers (Bob and Brian) do most of their work by
applying changes directly to the distribution copy of GSAS-II (the
``main`` branch in repository AdvancedPhotonSource/GSAS-II -- I'll
call this the "main repo"), the better way to make changes to GSAS-II
is to fork (make a private copy) of this main repo on GitHub and then
make a request to have your changes included into this distribution
copy, which is called a "pull request". You are very much encouraged
to try your hand at working on improvements and fixes to GSAS-II.

By making a fork -- your personal copy of the main repo -- you can
make changes to the software on your computer where you can test them
and you can send those changes to that personal copy of the repo on
GitHub (so they are backed up and can be shared with others). When you
feel you are at a point where you are ready to contribute your
changes, you issue a pull request on GitHub and invite the main
developers to incorporate your changes into the main repo. Note that
it really matters, but a fork does not actually make a full copy of
the GSAS-II files, it only sets up a mechanism for tracking changes
between your version of and the central main version, which initially
start as identical.

Note that you can have multiple copies of GSAS-II installed on your
computer, so it is easy to have a copy of GSAS-II for development and
another with the distributed version of GSAS-II for use in your work
(and potentially to compare fuction between versions.) Alternately
with a single installation of GSAS-II and multiple branches, you can
use the git command to quickly switch between different versions of
GSAS-II. There is never any danger of breaking GSAS-II in some way
that would be hard to fix. At worst you can discontinue work on a
messed up branch and start again.

One note, related to two similarly named and related things that might
be confusing: The program **git** (invented by Linus Torvalds of Linux
fame) is used to track versions of software. It is open source and
free for commercial and non-commercial use. It is widely used and is
very powerful, to the point of sometimes being bewildering. I only use
a small fraction of its features. **GitHub** is a commercial website
(owned by Microsoft but largely run independently) that hosts software
development projects and offers considerable resources, such as
computer farms that can be used to build and test software.
Non-commercial use of GitHub for open-source software is free. Git is
used by GitHub to transfer source code between computers (such as your
laptop) and the GitHub web site. GitHub complements the power of git
and offers the "pull request" code development model that allows
people to make a copy (private fork) of a software package, but then
offer their changes back to the developers for incorporation into the
main development version.

This documentation section summarizes the steps needed to work with a
forked copy of the GSAS-II repository in your own GitHub account. The
steps needed to establish a development version of GSAS-II are
outlined below. I am still learning my way around some of this, so let
me know about problems or better ways to do things. Below is an
outline of the steps needed to work on development of GSAS-II.



---------------------------------------------------
 Create a GitHub account
---------------------------------------------------

It is free. Use this link: https://github.com/signup?source=login. (See https://docs.github.com/en/get-started/start-your-journey/ for more info.)

---------------------------------------------------
 Create a fork of GSAS-II
---------------------------------------------------

This is pretty easy.

 * Open https://github.com/AdvancedPhotonSource/GSAS-II in a browser

 * Log in (if needed). If you are logged in, it will show your
    personal icon in the upper right. If not, you see Sign in/Sign up in
    the upper right.

 * Click on the "fork" button. This is to the right of the line near
    the top of the page that says "AdvancedPhotonSource/GSAS-II (Public)"

 * Create the fork in your own GitHub account. 
    
There is GitHub documentation on creating a fork here:
https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/working-with-forks/fork-a-repo

---------------------------------------------------
Authorize a GitHub Connection
---------------------------------------------------

You will need to establish an authorized connection between your
computer and GitHub in order to have the ability to send files from
your computer to GitHub. Note that the files in the GSAS-II repo are
all publicly available and do not require a GitHub account to be
accessed, but to copy changed files from your own computer back to
GitHub, you need to provide authorization for git to upload those
changed files to your GitHub account. This requires that the git
program be given access your GitHub account. This can be done via
https or ssh. See
https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/about-authentication-to-github
for more details.

   * Authenticating with https requires setting up a "`Personal Access Token <https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens>`_" on the GitHub site and optionally configuring git to use a `credential helper <https://github.com/git-ecosystem/git-credential-manager/blob/release/docs/install.md>`_ to help manage the password. The git repo will be accessed using an address starting with ``https://github.com/``.  I don't yet have any experience with using tokens this for this type authorization. 

   * Authenticating with ssh requires generating two "keys" one public and one private. The public key is provided to sites where you want to log into and the ssh protocol verifies that the two keys match. When ssh access is used, the git repo will be accessed using an address starting with ``git@github.com:``. This is discussed further below. 

   * GitHub provides their own software, the `GitHub CLI (command-line interface) <https://cli.github.com>`_, that can also be used to authorize access (see https://cli.github.com/manual/gh_auth_login). I have not used this for authorization. 

.. _gitauthenticate:

Authenticating with ssh
--------------------------

You may already have an ssh key and if not on MacOS and Linux you
likely already have the software needed to create them. On Windows, a
bit more effort is needed.

* To check if you already have an ssh key, see this: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/checking-for-existing-ssh-keys. 

* If you do not have an ssh key, see https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent.

     For Windows with tortoiseGit and its default PuTTy ssh program, use program
     PuTTygen. If a key has been generated it will be shown; if not pressing the
     Generate button will create this. The public key can be copied and pasted into
     the Settings/SSH and GPG keys setting page.

* To upload the key you generated to GitHub, see this page: https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account 
   
---------------------------------------------------
 Running GSAS-II from your forked copy
---------------------------------------------------

In order to develop GSAS-II, one must be able to run the program with
the files that are being modified.
  
There are a few ways that one can set up to run GSAS-II from a forked copy of the repo:

* Install GSAS-II from the main repo and then switch that code to use your own fork.

* Install GSAS-II directly from your repo

* Use git to install a copy of your repo, but run it using Python from
   a previously installed GSAS-II version.

These each will be discussed further below.

Switching a GSAS-II Installation
---------------------------------

From the `previous sections <install.html>`_, one can use the
GSAS2MAIN installer or the `pixi installer <install_pixi.html>`_ on
Linux or MacOS with the ``install-editable`` option (not yet available
for Windows). The installation methods where `Python is installed
independently of GSAS-II <install-python.html>`_, such as use of the
`gitstrap.py <install-python.html#using-the-gitstrap-py-installer>`_
and `gitcompile.py
</install-python.html#using-the-gitcompile-py-installer>`_ installers
will also work as GSAS-II is run directly from the git repo.

.. tip::
   
   If using pixi, be sure to use the ``pixi run install-editable`` command (Windows,
   ``pixi run install-editable-win``) to install GSAS-II. With ``pixi run install``
   because the files used to run GSAS-II are versions present when the install
   command was last run, not the latest versions. If you modified the repo
   files, you would need to rerun the ``pixi run install``  command to
   see the latest changes. Likewise, do not use pip to install GSAS-II for the
   same reasons. 

  One could possibly modify the installed GSAS-II files, in a
   directory along the lines of
   ``.../pixi/.pixi/envs/default/Lib/site-packages/GSASII``, but then
   changed files would need to be copied over to the git repo and
   would be at risk for an accidental overwrite if the install command
   were used. 

Once GSAS-II is installed and is running, one uses git to change the
GSAS-II files over to the version in your copy of the repo. Before
doing that note if you will be using `ssh or https access
<gitauthenticate>`_ to GitHub. With ssh access you will use these
commands::

  cd GSAS-II
  git remote add myG2 git@github.com:<your-fork>/GSAS-II.git
  git fetch myG2
  git checkout -B mywork myG2/main

While with https access the commands will be::

  cd GSAS-II
  git remote add myG2 https://github.com/<your-fork>/GSAS-II.git
  git fetch myG2
  git checkout -B mywork myG2/main

In the above ``<your-fork>`` will need to be the name of the GitHub
Account where your fork can be found (example: ``briantoby``) and
``myG2`` is a name you choose to reference that repo and ``mywork`` is
a name you choose to reference your development version in that repo.
Feel free to select names you prefer. Once the above has been done,
you can switch between the repo git with commands::

  git checkout main

for the main repo and::
   
  git checkout mywork

for the version associated with your fork of the repo. Note that if
you have made changes to the files you will need to save them either
through the ``git commit`` or ``git stash`` commands before you can
use the ``git checkout`` command.


Install GSAS-II directly from your forked repo
---------------------------------------------------

If you are on MacOS or Linux, you can use steps indicated in the `pixi
installer <install_pixi.html>`_ to install pixi. Again, knowing if you
will use `ssh or https access <gitauthenticate>`_ to GitHub. With ssh
access, the commands to download GSAS-II and install it and Python (as
well as compile) and will be::

  git clone --depth 1 git@github.com:<your-fork>/GSAS-II.git ~/G2
  cd ~/G2/pixi
  pixi run install-editable

while with https access, those commands will be::

  git clone --depth 1 https://github.com/<your-fork>/GSAS-II.git ~/G2
  cd ~/G2/pixi
  pixi run install-editable


Install GSAS-II directly from your repo after installing Python
----------------------------------------------------------------------------

If you want to use the git repo directly, you will need to install
Python and create GSAS-II binaries, which can be done as described
in :ref:`InstallPython`. The ``gitstrap.py`` and ``gitcompile.py``
routines can be used, but git must be used to download files from your
repo before those scripts are run. Examples follow::

  curl -L -O https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/raw/main/install/gitstrap.py
  git clone --depth 1 git@github.com:<your-fork>/GSAS-II.git G2
  python gitstrap.py --loc=G2

Note that the above commands download gitstrap.py to your current
working directory and create a G2 subdirectory where GSAS-II will be
installed. Alternately with https::

  curl -L -O https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/raw/main/install/gitcompile.py
  git clone --depth 1 https://github.com/<your-fork>/GSAS-II.git GSAS-II
  python gitcompile.py

these commands will place GSAS-II files in the default location
(``GSAS-II``) so the location need not be specified in the
``gitcompile`` step. Finally, the full path for the installation can
be specified in both, such as::
  
  curl -L -O https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/raw/main/install/gitcompile.py
  git clone --depth 1 git@github.com:<your-fork>/GSAS-II.git ~/myGSASII
  python gitcompile.py --loc=~/myGSASII

Install GSAS-II directly from your repo using GSAS2MAIN Python
----------------------------------------------------------------------------
  
If you have installed GSAS-II from GSAS2MAIN and wish to use that
Python and the GSAS-II binaries, that is also possible.

* For Windows, if GSAS-II is installed at location ``C:\Users\Me\gsas2main`` then use this command to setup Python::

      C:\Users\Me\gsas2main\Scripts\activate

* For Linux and MacOS, if GSAS-II is installed at location ``~/G2/g2main`` then use this command to setup Python::

      source ~/G2/g2main/bin/activate 

Note that once the above command has been run, in addition to the
``python`` command, one can also run ``git`` and ``conda``.

To clone GSAS-II from your forked copy use commands similar to the following::
    
    mkdir dev
    cd dev
    git clone --depth 1 git@github.com:<your-fork>/GSAS-II.git
    cd GSAS-II

or with https the third command will be:

  git clone --depth 1 https://github.com/<your-fork>/GSAS-II.git

Before GSAS-II can be run, it is also necessary to provide GSAS-II
binaries, which can be done by copying the binary directory,
GSASII-bin, from the GSAS2MAIN installation to the equivalent location
in the development installation. Alternately the GSASII-bin directory
can be moved to ~/.GSASII (%HOMEPATH%\.GSASII on Windows).

----------------------------------------------------------------------------
 Running the development version of GSAS-II
----------------------------------------------------------------------------

If GSAS-II is run from a directly installed version of Python or a
copy of Python installed with GSAS2MAIN, you will use a command such
as::

    python GSASII/G2.py
 
to start GSAS-II. Use of that command can get tiresome, so you may
want to set up a shortcut method to access your development version.
Note that the GSAS-II installers (GSAS2MAIN) run installation scripts
to create shortcuts. This can also be done manually for your
development version. See discussion of ``makeMacApp.py``,
``makeLinux.py`` and ``makeBat.py`` (for MacOS, Linux and Windows,
respectively) in the `Developer's Documentation
<https://gsas-ii.readthedocs.io/en/latest/GSASIIscripts.html#gsas-ii-misc-scripts>`_.
If you will use your development version of GSAS-II for scripting
GSAS-II, see this `note on scripting shortcuts
<https://gsas-ii.readthedocs.io/en/latest/GSASIIscriptable.html#shortcut-for-scripting-access>`_.

----------------------------------------------------------------------------
 Converting an https installation to ssh 
----------------------------------------------------------------------------

Note that if you have cloned using https using a command like this::
    
      git clone https://github.com/MyRepo/GSAS-II.git

but later set up for ssh authorization, you will need to change the
upstream repo, as described in the next section. This can be done by
editing the ``.../GSAS-II/.git/config`` file from::

   [remote "origin"]
	url = https://github.com/AdvancedPhotonSource/GSAS-II.git
	fetch = +refs/heads/master:refs/remotes/origin/master

  to::

   [remote "origin"]
	url = git@github.com:MyPersonalRepo/GSAS-II.git
	fetch = +refs/heads/*:refs/remotes/origin/*

These changes can be done directly by editing this file. Alternately,
these git commands will do the same thing::

     git config remote.origin.url git@github.com:MyPersonalRepo/GSAS-II.git 
     git config remote.origin.fetch "+refs/heads/*:refs/remotes/origin/*"

---------------------------------------------------
 Making branches and pull requests
---------------------------------------------------

You are strongly encouraged to create a separate branch for each
development project that you have with GSAS-II.

The command to do this is::

     git checkout -b g2newfeature

  Note that this creates a branch named ``g2newfeature`` -- do choose a better name.

When your changes are complete and you are ready to communicate them
back, you will commit them locally and use ``git push`` to upload them
to GitHub. From the web interface to GitHub you can then submit that
branch as a pull request to the main GSAS-II repository. Once you have
submiited your pull request, you likely will want to switch to a
different branch to do any further development work, as if changes are
uploaded for the branch used for the pull request, those changes will
be added to the code in the pull request.

---------------------------------------------------
Developer tricks
---------------------------------------------------

Note that the `Notes for GSAS-II Developers <developers.html>`_ has other useful information and development tricks. 
