This directory contains a draft version of the GSAS-II help pages
that are being converted from their MS-Word/HTML format into 
MarkDown where web pages are generated with mkdocs

Status of work 7/16/2025:

These files have been revised, but need another pass to update #TBD
links once the anchors have been defined. There might be a few
additional links that need to be added:

      44 docs/index.md 
      14 docs/preface.md 
      60 docs/applicationwindow.md
     191 docs/mainmenu.md 
      95 docs/others.md 
      10 docs/datatree.md
     207 docs/commontreeitems.md
      32 docs/phaseRB.md
      51 docs/phaseRMC.md
      81 docs/phaseatoms.md
      70 docs/phasedata.md
      64 docs/phasedrawatoms.md
      14 docs/phasedrawopts.md
      11 docs/phasedysnomia.md
      96 docs/phasegeneral.md
      27 docs/phaseisodistort.md
      25 docs/phaselayers.md
      25 docs/phasemappeaks.md
      13 docs/phasemcsa.md
      25 docs/phaseoverview.md
      20 docs/phasepawley.md
     128 docs/phasetexture.md
      12 docs/phasewave.md
     154 docs/image.md 

In progress:

     445 docs/histgramtree.md 


These files have had only minor editing. histgramtree.md should
probably be broken up:

     170 docs/cluster.md
      59 docs/pairdistribution.md
      74 docs/powderpeak.md
      89 docs/reflectometry.md
      62 docs/sequential.md
      39 docs/singlecrystal.md
      94 docs/smallanglescattering.md

N.B. must use `mkdocs-static-i18n` not `mkdocs-i18n` as in `pip install mkdocs mkdocs-material python-markdown-math mkdocs-static-i18n`

Needs more work: menu commands not described or well described in
atoms, draw atoms & draw options. Should also describe the settings on
draw options. Also, how does one expand a drawing to multiple cells? I
always forget that trick!

Texture: are there places where capital greek letters should be used
to differentiate symbols (\Phi vs \phi) orientation angles?

image.md: Make gain map appears to be moved to Image
Controls/Calibrate/Multiimage gain map. Remove former? Units are not
correct I think, for GSAS-II to Fit2D and pyFAI conversions
