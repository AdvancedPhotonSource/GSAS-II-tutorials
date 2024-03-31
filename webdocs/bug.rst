.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right

======================= 
Reporting GSAS-II Bugs
=======================

GSAS-II is being actively developed with new features regularly being added. Alas,
as new features are added or bugs are fixed, we inadvertently create bugs in things that previously worked. Unless we know about the bug, it will likely never be fixed. Usually we need sample data to reproduce the bug and so we know we have fixed it. Even if your bug is in the middle of a tutorial, please provide the GSAS-II project file so that we know exactly where the problem occurred (and so that we don't need to redo all the steps before that point so we can reproduce the problem.) Easy-to-find bugs tend to get fixed faster. 

Important: has the bug you are seeing already been fixed? Before reporting something as a bug, please update to the latest version of GSAS-II (see Help-->"Check for Updates") and test again to confirm that the problem still exists. If you report a bug with GSAS-II and your version is more than a few days old, we will probably ask you to update and confirm before we look at it. We do try to fix bugs as soon as we hear about them and sometimes have bug fixes posted within hours. 

Our preferred mechanism for bug reporting is to use the GitHub `Issues tracker <https://github.com/AdvancedPhotonSource/GSAS-II/issues>`_. Note that you can label your issue as an enhancement request, if you are asking for a new feature in GSAS-II. If you do not already have an account on GitHub, you will need one to use this (it's free), but there you can describe the problem and add files and images to help us duplicate and fix the problem. Others will be able to see the reported bugs, so that we don't end up working on duplicates. A public and active bug report may help us gain others in the community interested in supporting and expanding GSAS-II. Even if we only get useful comments, this will still be of help. Finally, the issues tracker will keep a record of the bugs that have been fixed, how they were addressed and when. Having a a centralized list of things that people are asking for will also be useful.

We will accept bug reports by e-mail, but would rather not get them that way. 

What to report
------------------

When reporting a bug,

 0) Please confirm you are using the newest GSAS-II version (see Help-->"Check for Updates"). We get kind-of-annoyed after spending hour figuring out what is going wrong, only to discover that it is something that was fixed, last week or last month. 

 1) Attach your project (.gpx) file. Even when requesting an enhancement, providing that so that we have example data to work from is very helpful. If your file contains unpublished data that you would rather not post, please remove/replace information on atoms/composition so that your data will not be very informative. Alternately see if you can reproduce the problem with data that you can post. If there is no other choice, you can let us know to ask you directly for the .gpx file.

 2) Note that .gpx files do not contain images, so problems in image processing will also require that you provide the relevant image(s).

 3) Another very helpful source of information when tracking down bugs will be the contents of the GSAS-II console (terminal) window, as that will usually show error messages and a trace of the Python commands involved. You can either highlight the contents and use copy-and-paste or provide a screen dump, At a minimum provide all lines beginning with "Traceback (most recent call..."]. but ideally we would like to see all the pages from when GSAS-II is first started, which maye require that you scroll up to give us a complete idea of what is going wrong.

On occasion, we may ask to schedule a Zoom or Teams with you to see exactly what you are doing or to look further at a bug we cannot reproduce. 
