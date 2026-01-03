.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right

======================================
Notes for GSAS-II Developers
======================================

We welcome cooperation from people interested in developing or
extending GSAS-II. The code is open source and we are happy to review
submitted code or consider collaborations. The ideal mechanism for
contributions is to clone the
`GitHub repo <https://github.com/AdvancedPhotonSource/GSAS-II>`_ and
then create a pull request, but small changes can be considered via
e-mail.

Note that you can have multiple copies of GSAS-II installed on your
computer so that you can compare running a local development version
against the latest distribution. See the web page on
`Installing GSAS-II for code development <install_dev.html>`_ for more
details. 

---------------------------------------------------------- 
Developer's documentation
----------------------------------------------------------

The Sphinx documentation for the GSAS-II source code will be of
significant value for people attempting to work their way through the
codebase. This is found on the wonderful “Read The Docs” web
site. These documents are available in a number of ways:

* `Access online <https://gsas-ii.readthedocs.io>`_ (HTML)
* `Download as a PDF document
  <https://gsas-ii.readthedocs.io/_/downloads/en/latest/pdf/>`_ (~450 pages)
* `Download as an electronic book
  <https://gsas-ii.readthedocs.io/_/downloads/en/latest/epub/>`_ (Epub format). 

If you use any of the self-installer options (gsas2main, gsas2pkg or gitstrap.py), GSAS-II will be installed using https from https://github.com/AdvancedPhotonSource/GSAS-II.git. This is fine for downloading, but to be able to write to the repository, you will probably need to switch to using ssh,
the command for this is::

    git remote set-url origin git@github.com:AdvancedPhotonSource/GSAS-II.git

More on this is in the `Installing GSAS-II for code development <install_dev.html>`_ 
web page, which discusses changing the origin to your forked copy of GSAS-II.

---------------------------------------------------------- 
Developing GSAS-II inside VSCode
----------------------------------------------------------

Visual Studio Code (VSCode) is a code development environment that is
freely distributed on all major platforms where GSAS-II runs.
Yuanpeng Zhang (ORNL) has written some notes on how to
`make GSAS-II run in the VSCode debugger <https://iris2020.net/2025-04-21-gsasii_dev_new/>`_.

Note that if you have used the gsas2main installer to place GSAS-II at ``~/g2main`` then you can use the Python installation there (examples:
Mac/Linux, ``/Users/toby/G2/g2main/bin/python``;
Windows, ``c:\Users\toby\g2main\python.exe``)
to run the debugger, rather than install a new conda environment as he does. 

---------------------------------------------------------- 
Debug mode/IPython Code development
---------------------------------------------------------- 
   
One nice trick for working with GSAS-II is that if you locate a place
where you want to insert code into the program, you can run commands
in that namespace environment. To do this, two prerequisite steps are
needed. First, use the conda command to install iPython (this assumes
you have already used the activate command, as above):: 

    conda install ipython

Then run GSAS-II and use the Preferences command (File menu or on
MacOs on the first menu, named GSAS-II or python) and `set the debug
option to True`. One can then place a ``breakpoint()`` statement into
GSAS-II at a location where one wants to develop code. When that
statement is executed, GSAS-II will enter iPython but in the local
environment where your code will be executed, so you can see what
variables and functions are defined and try running code that can then
be placed into GSAS-II. Remember to remove the breakpoint statement
when you are done. 

Note that when the ``debug`` configuration setting is set to True, that
also turns on some potentially useful print statements. 

---------------------------------------------------
Testing code without restarting
---------------------------------------------------

One trick that can sometimes be used to test new GSAS-II routines without restarting GSAS-II is to insert code like this::

  from importlib import reload
  reload(G2mod)
  print('Reloading',G2mod)
  G2mod.NewRoutine()
  
into the location where a module is being called. This will cause the
GSAS-II module "``G2mod``" (for example ``G2sc`` for GSASIIscriptable
or ``G2G`` for GSASIIctrlGUI, etc.) to be reread from its Python file
just before it is run. In this way, code can be modified, saved and
tested without even needing to restart GSAS-II. Where this is not
possible (usually because one is testing with an object or because
global variables inside the module are reset by the reload), it is
still often quick to restart and retest development code.

It should be noted that this can occasionally cause problems in that
anything saved in that module (for example global variables) will be
reset to initial values when the module is reloaded. 

For safety, just in case one forgets to remove this, it is best to
have this code be executed only in debug mode::
    
        if GSASIIpath.GetConfigValue('debug'):
            print('Debug: reloading',G2gr, G2pwpl)
            from importlib import reload
            reload(G2pwpl)
            reload(G2gr)
        G2gr.UpdateGroup(G2frame,item)

---------------------------------------------------
Adding startup code
---------------------------------------------------

When doing repetitive testing, it can be time consuming to have to run
the same commands from the GUI each time that GSAS-II is started. In
debug mode, GSAS-II can run specific code when the program is started
by creating a file named ``debug_setup.py`` that is placed in the
directory with the rest of the GSAS-II files. As an example::

       import wx
       G2frame = wx.App.GetMainTopWindow()
       G2frame.OnRefine(None)

This triggers refinement of a .gpx file that is placed on the command
line. 
