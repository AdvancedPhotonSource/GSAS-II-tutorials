.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right

====================================
Customizing GSAS-II
====================================

There are many ways that GSAS-II operations can be tailored, if the way it operates "out of the box" is not ideal for how you use the program. In the File/Preferences menu (this is called menus is labeled as Settings on Macs, and is found both in the File menu, as well as the normal location for Settings as part of the first menu item). This menu offers access to >40 different options that change how GSAS-II operates, allowing aspects of the program to operate according to preferences of different users. 
Examples of customization options include plotting colors, default options for image masking and integration, locations for add-on programs and options used for debugging. A complete list of the available preference options are listed in file ``config_example.py`` where the contents of that file is
`documented here <https://gsas-ii.readthedocs.io/en/latest/GSASIIutil.html#config-example-py-configuration-options>`_.
Note that these preferences are saved locally in file ``config.py``.

GSAS-II is open source, so you may want to change other aspects of how GSAS-II operates to be more convenient for your own use. Should you implement something along those lines, we would be interested in making that available to others as a preference option. Please consider submitting a pull request on GitHub.
