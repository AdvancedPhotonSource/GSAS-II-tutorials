<a name="Phase-Atoms"></a>
<a name="_Atoms"></a>
# **Atoms** phase tab

This data tab holds the table of parameters for the atoms in this crystal structure model. The menu controls allow manipulation of the values, refinement flags as well as initiation calculations of geometrical values (distances & angles) among the atoms.

Some atom operations utilize or set the "viewpoint." This is the location in the 
graphics window's structure drawing that is marked by crossing , red, green and blue lines. 

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. **Atom selection from table** - These are controlled by the mouse and the Shift/Ctrl/Alt keys. Note that for most purposes (one exception is atom reordering which requires an Alt-Left-click on the rows), selection of any cell for an atom will work equivalently with selection of the entire row. Upon selection, the atoms will turn green in the structure drawing:

    * **Left Mouse Button (LMB)** – on a row number selects the atom.
    * **Shift+LMB** – on a row number selects all atoms from last selection to the selected row (or top is none previously selected).
    * **Ctrl+LMB** – on a row number selects/deselects the atom.
    * **Alt+LMB** – on a row number selects that atom for moving; the status line at bottom of window will show name of atom selected. Use Alt+LMB again to select a target row for this atom; insertion will be before this row and the table will be updated to show the change. NB: the Draw Atoms list is not updated by this change.

2. **Double-left click a Type column heading**: a dialog box is shown that allows you to select all atoms with that type.
3. **Double-left click a refine or I/A column heading**: a dialog box will be shown with choices to be applied to every atom in the list.
4. **Editing tools** – These are controlled by the mouse (Alt ignored, Shift & Ctrl allow selection of multiple cells but no use is made of them). An individual data item can be cut/pasted anywhere including from/to another document. Bad entries are rejected (yellow background). If any entry is changed, press Enter key or select another atom entry to apply the change.

    * **Name** – can change to any text string.
    * **Type** – causes a popup display of the Periodic Table of the elements; select the element/valence desired; the atom will be renamed as well.
    * **refine** – shows a pulldown of allowed refinement flag choices to be shown; select one (top entry is blank for no refinement).
    * **x,y,z** – change atom coordinate. Fractions (e.g. 1/3, 1/4) are allowed.
    * **frac,Uiso,Uij** – change these values; fractions (e.g. 1/3, 1/4) are allowed.
    * **I/A** – select one of I(sotropic) or A(nisotropic); the Uiso/Uij entries will change appropriately.

5. Menu '**Edit Atoms**' - The edit menu shows operations that can be performed on your selected atoms. The command will operated on the atoms selected prior with the left mouse button. If no atoms have been selected, a window will open to allow atoms to be selected.
    
    * **On selected atoms...** -

        1. **Refine selected** – A popup dialog box appears; select refinement flags to apply to all selected atoms.
        * **Modify parameters** – A popup dialog box appears with a list of atom parameter names; select one to apply to all selected atoms. Name will rename selected atoms according to position in table [e.g. Na(1) for Na atom as 1st atom in list in row '0']. Type will give periodic table popup; selected element valence will be used for all selected atoms and atoms names will be changed. I/A will give popup with choices to be used for all selected atoms. x,y,z will give popup for shift to be applied to the parameter for all selected atoms. Uiso and frac will give popup for new value to be used for all selected atoms.
        * **Set viewpoint** – Set the viewpoint to be position of 1st selected atom
        * **Move atom to viewpoint** – Move a single atom to the viewpoint location.
        * **Insert atom** – insert an H atom (name= Unk) at 0,0,0 before the selected atom, it is also drawn as an H atom in the structure plot (small white ball). The atom can then be edited to change the type, coordinates, etc.
        * **Insert viewpoint** – insert an H atom (name= Unk) before the selected atom with coordinates matching the location of the viewpoint, it is also drawn as an H atom in the structure plot.
        * **Calc H atoms** – insert H-atoms in standard positions bonded to the selected atoms. The positions used will be computed based on bonding patterns for the selected atoms.
        * **Delete atom** – selected atoms will be deleted from the atom list; they should also vanish from the structure drawing.
        * **Transform atoms** – A popup dialog box appears; select space group operator/unit cell translation to apply to the selected atoms. You can optionally force the result to be within the unit cell and optionally generate a new set of atom positions. You may also invert a noncentrosymmetric structure. NB: many of these operations only make sense if all atoms are selected, but this is not enforced. 
        * **Select all** – Selects all atoms for further changes. Atoms in drawing will turn green.
        * **Select from list** – A popup appears allowing selection of atoms for further changes. Selected atoms will turn green.
        * **Append atom** – add an H atom (name= Unk) at 0,0,0 to the end of the atom table, it is also drawn as an H atom in the structure plot.
        * **Append viewpoint** – add an H atom (name= Unk) to the end of the atom table with coordinates matching the location of the viewpoint; it is drawn as an H atom in the structure plot.
        * **Update H atoms** – Reset H-atoms according to bonding geometry; only applies to H-atoms initially placed via Calc H-atoms. Usually used after running a structure refinement.
        * **Assemble molecule** – move atoms to create single molecule, not appropriate for extended structures.
        * **Collect atoms** – move atoms to be closest to selected position
        * **Reload draw atoms** – reload drawing atoms from current atom list. Generally needed after a refinement.
        * **Reimport atoms** – resets the coordinates to values from any importable phase file (e.g. CIF, `.gpx`,...)

6. Menu '**Compute**' –

    * **Show Distances & Angles** – compute distances and angles with esds (if possible) for selected atoms. A popup dialog box will appear with distance angle controls. NB: if atoms have been added or their type changed, you may need to do a Reset of this dialog box before proceeding.
    * **Save Distances & Angles** – same as the prior menu command, but writes the distance & angle result to a file with extension `.disagl`.
    * **Histogram bonds and angles** – plots histograms of bond lengths & angles about selected atoms.
    * **Apportion atom frac** – after selection of a 2nd element; this determines from atomic number and neutron scattering length the atom fractions of each type for selected atoms and presents results on the console.
    * **Density** – calculate density
    * **ISODISTORT mode values** – when a structure has been imported from ISODISTORT,  this will compute the mode displacements for the current atom positions and display them in a popup window.


<a name="Phase-mouse-plotopts"></a>
<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

A drawing of the crystal structure will be displayed in the [Graphics Window](./applicationwindow.md#Plots) only if the [Draw Options](./phasedrawopts.md) or [Draw Atoms](./phasedrawatoms.md) tab has been visited first prior to selecting the Atoms tab. When back at the Atoms tab, the following actions and keypress commands are available, when use of the mouse buttons changes the view of the structure and can be used to select atoms. On MacOS and a one-button mouse, [some alternate actions must be used](./others.md#MacOS)

* **Left drag**: Holding down left button rotates axes around screen x & y
* **Right drag**: Holding down right button translates the fractional coordinates assigned to the viewpoint (which is kept at the center of the drawing). The structure will appear to translate. The viewpoint can also be entered directly in the [Draw Options](./phasedrawopts.md)..
* **Middle drag**: Holding down center button rotates axes around screen z (direction perpendicular to screen).
* **Mouse Wheel**: Rotating the scroll wheel changes "camera distance" (zoom in/out)
* **Shift+Left Click**: Holding down the shift key while clicking on an atom with the left mouse button causes that atom to be selected (Shift + a Right click does the same). Any previously selected atoms will be reset. If two atoms are overlapped in the current view, then the top-most atom will usually be selected. Only atoms in the asymmetric unit can be selected from the plot in this way.
* **Shift+Right click**: Holding down the shift key while clicking on an atom with the right mouse button causes the atom to be selected if previously unselected and unselected if previously selected. Any previously selected atoms will be continue to be selected so shift-right click can be used to add atoms to the selection list. If two atoms are overlapped in the current view, then the top-most atom will usually be selected. Only atoms in the asymmetric unit can be selected from the plot in this way. (On a Mac, control+mouse click is an alternate way to do this.)
* **Key n**: Pressing the "n" key selects the next atom in the displayed atom list.
* **Key p**: Pressing the "p" key selects the previous atom in the displayed atom list.
* **Key c**: Pressing the "c" key sets the plot viewpoint at unit cell center. Also resets n/p selection item to the 1st atom.
* **Key s**: Pressing the "s" key brings up a (large) selection of color schemes for the slice contours. Default – "RdYlGn" (Green – positive, red – negative & yellow – zero).
* **Key k**: Pressing the "k" key cycles through the possible slice contouring options (none, lines, colors, lines+colors)
* **Key m**: Pressing the "m" key for an incommensurate structure creates a movie file of the change in the structure along the 4th dimension (tau). Movie controls are found in the GSAS-II Configuration Variables. Requires the imageio python package be available for import – it is not normally available in the GSAS-II version of python.
* **Key +**: Pressing the "+" (or "=") key steps the viewpoint in positive drawing z-direction (toward viewer). If structure is incommensurate, "+" steps the structure and map through the 4th dimension (+tau).
* **Key -**: Pressing the "-" key steps the viewpoint in negative drawing z-direction (away from viewer). If structure is incommensurate, "-" steps the structure and map through the 4th dimension (-tau).
