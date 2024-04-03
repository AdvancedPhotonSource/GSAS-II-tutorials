.. raw:: html

	 <style> .clear {clear: both;}</style>

.. image:: ./images/gsas2.png
   :scale: 25 %
   :alt: GSAS-II logo
   :align: right

========================================================
Detailed Description of the Linux Installation Process
========================================================
The exact details for how the installation is performed will depend on "flavor" of Linux in use. Here I am using Ubuntu.

1) In a terminal window paste the commands::

     g2="https://github.com/AdvancedPhotonSource/GSAS-II-buildtools/releases/download/v1.0.1/gsas2full-Latest-Linux-x86_64.sh"
     curl -L "$g2" > /tmp/g2.sh; bash /tmp/g2.sh -b -p ~/g2full

   as seen to right. Note that I have chosen to install in location ``~/g2full`` (which is subdirectory ``g2full`` in my home directory), but you can install this where you prefer.
   
.. image:: ./linux_inst_images/1.png
   :scale: 25 %
   :alt: commands in terminal window 
   :align: right

.. raw:: html

	 <div class="clear"></div>
	   
2) This will run for a few minutes (or longer depending on download speeds) and then the conda installation process will start, with the display of lots of text. At the end, the terminal window will appear as seen to the right. Note the addition of the GSASII file on the desktop (this may not happen on all Linux desktop managers.). The installation has been completed. 

.. image:: ./linux_inst_images/2.png
   :scale: 25 %
   :alt: completion commands in terminal window 
   :align: right

.. raw:: html

	 <div class="clear"></div>
	   
3) Note the red "X" on the desktop icon and the "grayed-out" colors. This is because by default new icons are disabled. Right-click on the icon and select "Allow launching" from the menu. The "X" disappears and colors return to normal, as seen in the upper right.

   Clicking on the icon will open GSAS-II. Likewise a GSAS-II project (.gpx) file can be dragged onto the icon to open that file in GSAS-II.

.. image:: ./linux_inst_images/3.png
   :scale: 25 %
   :alt: activate terminal icon
   :align: right