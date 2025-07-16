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

These files have had only minor editing. A few need to be broken up:

    170 docs/cluster.md
     157 docs/datatree.md
     445 docs/histgramtree.md
     154 docs/image.md
      59 docs/pairdistribution.md
     629 docs/phase.md
      74 docs/powderpeak.md
      89 docs/reflectometry.md
      62 docs/sequential.md
      39 docs/singlecrystal.md
      94 docs/smallanglescattering.md

Removed internationalization (i18n from mkdocs.yml) because of error
message from mkdocs:

    (/tmp/py313) py3.13 MDhelp % mkdocs build
    ERROR   -  Config value 'plugins': Plugin 'i18n' option 'languages': Expected
           type: <class 'dict'> but received: <class 'list'>

when using:

    pip install mkdocs mkdocs-material python-markdown-math mkdocs-i18n

    Successfully installed babel-2.17.0 backrefs-5.9 certifi-2025.7.14 charset_normalizer-3.4.2 click-8.2.1 colorama-0.4.6 ghp-import-2.1.0 idna-3.10 jinja2-3.1.6 markdown-3.8.2 markupsafe-3.0.2 mergedeep-1.3.4 mkdocs-1.6.1 mkdocs-get-deps-0.2.0 mkdocs-i18n-0.4.6 mkdocs-material-9.6.15 mkdocs-material-extensions-1.3.1 packaging-25.0 paginate-0.5.7 pathspec-0.12.1 platformdirs-4.3.8 pygments-2.19.2 pymdown-extensions-10.16 python-dateutil-2.9.0.post0 python-markdown-math-0.9 pyyaml-6.0.2 pyyaml-env-tag-1.1 requests-2.32.4 six-1.17.0 urllib3-2.5.0 watchdog-6.0.0
