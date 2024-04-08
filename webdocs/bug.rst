.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right

======================= 
Reporting GSAS-II Bugs
=======================

GSAS-II is being actively developed with new features regularly being added. Alas,
as new features are added or bugs are fixed, we inadvertently create bugs in things that previously worked. Unless we know about the bug, it will likely never be fixed. Usually we need sample data to reproduce the bug and so we know we have fixed it. Even if your bug is in the middle of a tutorial, please provide the GSAS-II project file so that we know exactly where the problem occurred (and so that we don't need to redo all the steps before that point so we can reproduce the problem.) Easy-to-find bugs tend to get fixed faster. 

**Important**: has the bug you are seeing already been fixed? Before reporting something as a bug, please update to the latest version of GSAS-II (see Help-->"Check for Updates") and test again to confirm that the problem still exists. If you report a bug with GSAS-II and your version is more than a few days old, we will probably ask you to update and confirm before we look at it. We do try to fix bugs as soon as we hear about them and sometimes have bug fixes posted within hours. 

With our transiton to GitHub, bugs and enhancement requests will be found in the `GitHub Issues Tracker <https://github.com/AdvancedPhotonSource/GSAS-II/issues>`_. This will help in finding and fixing problems as well as letting people know what has been fixed and avoid us pursuing duplicates. Having a a centralized list of things that people are asking for will also be useful and may help us grow community support. Finally, the issues tracker will keep a record of the bugs that have been fixed, how they were addressed and when. 

What to report
------------------

When reporting a bug,

 0) Please confirm you are using the newest GSAS-II version (see Help-->"Check for Updates"). We get kind-of-annoyed after spending an hour figuring out what is going wrong, only to discover that it is something that was fixed, last week or last month. 

 1) Attach your project (.gpx) file. Even when requesting an enhancement, providing that so that we have example data to work from is very helpful. If your file contains unpublished data that you would rather not post, please remove/replace information on atoms/composition so that your data will not be very informative. Alternately see if you can reproduce the problem with data that you can post. If there is no other choice, you can let us know to ask you directly for the .gpx file, which will not be posted.

 2) Note that .gpx files do not contain images, so problems in image processing will also require that you provide the relevant image(s).

 3) Another very helpful source of information when tracking down bugs will be the contents of the GSAS-II console (terminal) window, as that will usually show error messages and a trace of the Python commands involved. You can either highlight the contents and use copy-and-paste or provide a screen dump, At a minimum provide all lines beginning with "Traceback (most recent call..."], but ideally we would like to see all the pages from when GSAS-II is first started, which may require that you scroll up to give us a complete idea of what is going wrong.

    On occasion, we may ask to schedule a Zoom or Teams with you to see exactly what you are doing or to look further at a bug we cannot reproduce. 

How to report
------------------

Our preferred mechanism for bug reporting is to use the GitHub `Issues tracker <https://github.com/AdvancedPhotonSource/GSAS-II/issues>`_. If you do not already have an account on GitHub, you will need one (it's free) to create or comment on a report, but anyone can see what is there. When creating an issue report, please describe the problem and add files and images to help us duplicate and fix the problem (see above). We will accept bug reports by e-mail, but would rather not get them that way. 

 * **GitHub Issues Tracker**: https://github.com/AdvancedPhotonSource/GSAS-II/issues

 * **uploading files**: GitHub is very restrictive in the types of files that can be attached to a issue, but there are two ways to attach GSAS-II project (.gpx) files, as well as image and data files. They can be placed in a zip archive, which can be created through a number of freely available software products. The .zip can be attached to the GitHub issue.

   Alternately, on Mac and Linux computers the gzip program usually is installed as part of the basic OS and can be called as::

        gzip project.gpx

   which replaces the ``project.gpx`` file with a compressed version of the file ``project.gpx.gz``. The ``.gz`` files can also be attached to an issue. (To retain the original file use ``gzip -k`` in place of ``gzip``.)
