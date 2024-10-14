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

The Sphinx documentation for the GSAS-II source code will be of
significant value for people attempting to work their way through the
codebase. This is found on the wonderful “Read The Docs” web
site. These documents are available in a number of ways:

* `Access online <https://gsas-ii.readthedocs.io>`_ (HTML)
* `Download as a PDF document
  <https://gsas-ii.readthedocs.io/_/downloads/en/latest/pdf/>`_ (~450 pages)
* `Download as an electronic book
  <https://gsas-ii.readthedocs.io/_/downloads/en/latest/epub/>`_ (Epub format). 

If you use any of the self-installer options (gsas2full, gsas2pkg or gitstrap.py), GSAS-II will be installed using https from https://github.com/AdvancedPhotonSource/GSAS-II.git. This is fine for downloading, but to be able to write to the repository, you will probably need to switch to using ssh,
the command for this is::

    git remote set-url origin git@github.com:AdvancedPhotonSource/GSAS-II.git

More on this is in the `Installing GSAS-II for code development <install_dev.html>`_ 
web page, which discusses changing the origin to your forked copy of GSAS-II.
