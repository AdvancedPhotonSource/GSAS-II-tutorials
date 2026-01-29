.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right

====================================
 Help: GSAS-II will not start
====================================

While I hope this never happens again, there have been occasions where a
version of GSAS-II is placed on the web that has an error that prevents the program from starting.
Once that version is installed, it is then not possible to access the
Help/Update menu command to obtain the different version of
GSAS-II. The same thing can also happen if you make changes to the
files yourself and introduce an error. Also, if you make changes to
the GSAS-II Python (.py) files, you may no longer be able to obtain updates.

A script is provided that can be used to reset any locally made
changes and then install the lastest version of GSAS-II. If you have
made changes that you wish to retain, you should make a copy of them
either using a utility to place a copy elsewhere, or you can use the
git stash, branch or commit commands. The commands below will
overwrite your changes with the latest GSAS-II version. 

On Windows
----------------

A Windows .BAT file is created in the directory where
GSAS-II is installed, named ``2Reset2FreshGSASII.bat``
Thus, if GSAS-II is installed in directory 
``C:\Users\toby\gsas2main`` the file will be named
``C:\Users\toby\gsas2main\2Reset2FreshGSASII.bat``.
This file will remove any changes you have made locally to the GSAS-II
files and will install the latest version of those files from the
GitHub server. The
file can run by locating them in the Windows File Explorer and
double-clicking on it or by typing the file name into the cmd.exe
window.

Note that the GSAS-II installers prior to 2026 did not create this
file or created a similarly named file that would not work. If the
file ``2Reset2FreshGSASII.bat`` is not present, download and reinstall
GSAS-II. You can use a new location and keep the old version or delete
the old version and install the new one in the location used
previously.

For now, the gsas2main installer will also create two other similar
files, ``G2_bootstrap.bat`` and ``G2_start.bat``. These have the
installation location hard-coded. The ``G2_bootstrap.bat`` file should
download and rerun the ``gitstrap.py`` updating GSAS-II, very
similarly to the ``2Reset2FreshGSASII.bat``script. The
``G2_start.bat`` simply starts the GSAS-II GUI. 

On MacOS and Linux
------------------------

At the time this is being written, an error prevents the script from
running, but this can be corrected by editing the ``reset-gsasII.sh``
file manually (see below). Note that this file is placed in the ``bin`` directory
immediately below the GSAS-II installation directory. Thus, if
GSAS-II is installed at location ``/Users/toby/G2/gsas2main`` then the
file will be named ``/Users/toby/G2/gsas2main/bin/reset-gsasII.sh``. (It
will appear in the path if conda is initialized.) Depending on the OS,
it may be possible to locate and run this file in a system-supplied
file browser, or type the file name into a terminal window. 

The error in the script is that the second line is incorrect. If the
lines appear as::

  # Commands to run GSAS-II load/update process
  source /bin/activate base
  /Users/toby/G2/gsas2main/bin/python /Users/toby/G2/gsas2main/gitstrap.py --reset

The second line should be changed as follows::

  # Commands to run GSAS-II load/update process
  source /Users/toby/G2/gsas2main/bin/activate base
  /Users/toby/G2/gsas2main/bin/python /Users/toby/G2/gsas2main/gitstrap.py --reset
