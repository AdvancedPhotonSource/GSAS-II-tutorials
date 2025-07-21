This directory contains a draft version of the GSAS-II help pages
that have been converted from their MS-Word/HTML format into 
MarkDown. Web pages are generated with mkdocs


Status of work 7/20/2025:

The 41 .md files have all been looked at, though some more carefully
than others. 

The next step is to tabulate Anchors used in the .md files
(duplicates, missing names used in original .html)

Need python code that selects and opens new .html file based on anchor. 


Needs more work: 

menu commands not described or well described in
atoms, draw atoms & draw options. Should also describe the settings on
draw options. Also, how does one expand a drawing to multiple cells? I
always forget that trick!

Texture: are there places where capital greek letters should be used
to differentiate symbols (\Phi vs \phi) orientation angles?

image.md: Make gain map appears to be moved to Image
Controls/Calibrate/Multiimage gain map. Remove former? Units are not
correct I think, for GSAS-II to Fit2D and pyFAI conversions

It would be nice to generate a PDF of all pages. Could not get
https://mkdocs-to-pdf.readthedocs.io to work on MacOS, but perhaps on
Linux? There are other choices:
https://comwes.github.io/mkpdfs-mkdocs-plugin/index.html 
https://pypi.org/project/mkdocs-with-pdf/
Everything seems to depend on https://weasyprint.org/
