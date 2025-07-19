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

In progress (being broken up into sections by tab):

     629 docs/phase.md 


These files have had only minor editing. A few need to be broken up:

     170 docs/cluster.md
     445 docs/histgramtree.md
     154 docs/image.md
      59 docs/pairdistribution.md
      74 docs/powderpeak.md
      89 docs/reflectometry.md
      62 docs/sequential.md
      39 docs/singlecrystal.md
      94 docs/smallanglescattering.md

N.B. must use `mkdocs-static-i18n` not `mkdocs-i18n` as in `pip install mkdocs mkdocs-material python-markdown-math mkdocs-static-i18n`
