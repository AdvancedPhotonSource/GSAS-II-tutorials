<a name="Phase-Map_peaks"></a>
# **Map peaks** phase tab

This gives the list (magnitude, x y & z) of all peaks found within the unit cell from the last Fourier/charge flip map search, sorted in order of decreasing peak magnitude. In the crystal structure plot, each peak position,shown as a white to dark gray cross; the shade is determined from the magnitude for the peak relative to the maximum peak magnitude; some are connected by white sticks as possible bonds. Negative peaks are shown in orange.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

* **Peak Selection from table**: select individual atoms by a left click of the mouse when pointed at the left most column (atom numbers) of the atom display; hold down the Ctrl key to add to your selection; a previously selected atom will be deselected; hold down Shift key to select from last in list selected to current selection. A selected atom will be highlighted (in grey) and the atoms will be shown in green on the plot. Selection without the Ctrl key will clear previous selections. A left click in the (empty) upper left box will select or deselect all atoms.
* **Select the mag column** – the entries will be sorted with the largest at the top.
* **Select the dzero column** – the entries will be sorted with the smallest (distance from origin) at the top.
* **Select the dcent column** – the entries will be sorted with the smallest distance from the unit cell center at the top.
* Menu '**Map peaks**'  –
    
    * **Move peaks** – this copies selected peaks to the [Atoms](./phaseatoms.md) tab and the [Draw Atoms](./phasedrawatoms.md) tab. They will be appended as new atoms to the end of each list each with the name 'UNK' and the atom type as 'H'. They will also be drawn as small white spheres at their respective positions in the structure drawing. If inclusion of an atom into the model is appropriate, you should next go to the [Atoms](./phaseatoms.md) tab and change the atom type to whatever element you desire; it will be renamed automatically.
    * **View point** – this positions the viewpoint (large 3D RGB cross) at the 1st selected peak.
    * **View pt. dist.** – this calculates distance from viewpoint to all selected map peaks.
    * **Hide/Show bonds** – toggle display of lines (bonds) between peaks
    * **Calc dist/ang** – if 2 peaks are selected, this calculates the distance between them. If 3 peaks are selected this calculates the angle between them; NB: selection order matters. If selection is not 2 or 3 peaks this is ignored. Output is on the console window.
    * **Equivalent peaks** – this selects all peaks related to selection by space group symmetry.
    * **Invert peak positions** – inversion through cell center of map and all positions.
    * **Roll charge flip map** – popup allows shifting of the map & all peak positions by unit cell fractions; can be along combinations of axes.
    * **Unique peaks** – this selects only the unique peak positions amongst those selected; a popup allows selection of atom subset closest to x=0, y=0, z=0 origin or center.
    * **Save peaks** – saves the peak list as a csv file.
    * **Delete peaks** – this deletes selected peaks. The shading on the remaining peaks is changed to reflect any change in the maximum after deletion.
    * **Clear peaks** – this deletes all the peaks in the map peak list; they are also removed from the crystal structure drawing plot.
