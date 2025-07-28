<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="Phase-Draw_Atoms"></a>
# *Draw Atoms* phase tab

Visiting this tab causes a drawing of the crystal structure to be displayed in the [Graphics Window](./applicationwindow.md#Plots) 

The contents of this tab is a list of the atoms that are displayed. These may be  rendered as lines, van der Waals radii balls, sticks, balls & sticks, ellipsoids & sticks or polyhedra. Bonds, as shown in the structure drawing, are determined by the atomic radii settings. There are four menus for this tab:

 * **Edit** allows modification of the list of atoms to be rendered, 
 * **Compute** gives some options for geometric characterization of selected atoms,
 * **Restraints** allows definition of 4 different types of restraints on the structure and
 * **Rigid body** allows selection of atoms that form a previously defined rigid body.


<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

The commands and operations here determine what atoms are included in the structure drawing and how those atoms are displayed. Note that options for display type are by atom, so van der Waals, ball & stick and polyhedral display, for example, can all be mixed in a single display. Note that when atoms are added to the list, the anisotropic thermal displacement parameters (Uij) for atoms created by symmetry operations will be transformed as appropriate. Note that any atom positions that duplicate atoms already in the list are not retained. 

There are two convenient ways to use the capabilities here. Select atoms and then select a menu item, typically from the **Edit Figure** menu. Alternately, right-click on the table and you will be offered a list of commands that can be performed on the selected atoms. 

### Atom Selection
Atoms may be selected by a number of methods: 

1. **Atom Selection from table**: select individual atoms by a left click of the mouse when pointed at the left most column (atom numbers) of the atom display; hold down the Ctrl key to add to your selection; a previously selected atom will be deselected; hold down Shift key to select from last in list selected to current selection. A selected atom will be highlighted (in grey) and the atoms will be shown in green on the plot. Selection without the Ctrl key will clear previous selections. A double left click in the (empty) upper left box will select or deselect all atoms.
2. **Atom Selection from drawing**: select an atom by a left click of the mouse while holding down the Shift key and pointed at the center of the displayed atom, it will turn green if successful and the corresponding entry in the table will be highlighted (in grey); any previous selections will be cleared. To add to your selection, use the right mouse button (Shift down); if a previously selection is reselected it is removed from the selection list. NB: beware of atoms that are hiding behind the one you are trying to select they may be selected inadvertently. You can rotate the structure anytime during the selection process.
3. **Double left click a Name, Type and Sym Op column heading**: a dialog box is shown that allows you to select all atoms with that characteristic. For example, selecting the Type column will show all the atom types; your choice will then cause all those atoms to be selected.
4. **Double left click a Style, Label or Color column**: a dialog box is shown that allows you to select a rendering option for all the atoms. For Color a color choice dialog is displayed that covers the entire color spectrum. Choose a color by any of the means available, press the "Add to Custom Colors", select that color in the Custom colors display and then press OK. NB: selecting Color will make all atoms have the same color and for Style "blank" means the atoms aren't rendered and thus the drawing will not show any atoms or bonds!
5. **Select from list** menu command (see below). A list of atoms is displayed and one can select using checkmark buttons. This will be offered automatically when a menu command requires selected atoms and none have been selected.

Note that on a Mac with a one-button mouse, [some alternate actions must be used](./others.md#MacOS) for selection.

### Menu '**Edit Figure**'  Contents
The edit menu shows operations that can be performed on your selected atoms. If you have not selected any atoms using any of the menu items, you will be presented with a window where you can select atoms. 

Many of the options below can also be accessed after selecting one or more atoms by right-clicking the mouse on the table. 

   * **Atom style** – select the rendering style for the selected atoms
   * **Atom label** – select the item to be shown as a label for each atom in selection. The choices are: none, type, name or number. (NB: atom labelling slows drawing response time).
   * **Atom color** – select the color for the atom; a color choice dialog is displayed that covers the entire color spectrum. Choose a color by any of the means available, press the "Add to Custom Colors", select that color in the Custom colors display and then press OK.
   * **Reset atom colors** – return the atom color back to their defaults for the selected atoms.
   * **Edit atom radii** – modify atom radii used in the bond assignment algorithm.
   * **View point** – position the plot view point to the first atom in the selection. The view point is shown as crossing red, blue and green lines and this is placed at the center of the plot diagram in all three dimensions. 
   * **Select from list** – select atoms from a popup list of names.
   * **Add atoms** – using the selected atoms, additional atoms are added to the bottom of the list after applying your choice of symmetry operator and unit cell translation to the *selected atom* coordinates. Through use of this command, usually  after the **Fill unit cell** and/or **Complete molecule** commands, makes it possible to display multiple unit cells. 
   * **Add sphere of atoms** – fill in all atoms that fall within a sphere of selected radius about selected atom(s).
   * **Add box of atoms** – Not yet implemented
   * **Transform draw atoms** – apply a symmetry operator and unit cell translation to the set of selected atoms; they transformed atoms will replace the original atoms in the draw atoms list. 
   * **Fill CN-sphere** – using the atoms currently in the draw atom table, find all atoms that belong in the coordination sphere around the selected atoms via unit cell translations. NB: symmetry operations are not used in this search; do **Fill unit cell** first.
   * **Fill unit cell** - using the atoms currently selected from the draw atom table, find all atoms that fall inside or on the edge/surface/corners of the unit cell. This operation is frequently performed before Fill CN-sphere.
   * **Complete molecule** – beginning with a selected atom, transform other atoms to equivalent positions that form a contiguous molecule. Not appropriate for continuous structures (a warning will appear if the command is not completing)
   * **Create void map** – by using a grid of probe positions, locate points outside of normal contact distances within a structure. Result is a mesh of small blue points in structural voids. These could indicate possible locations of missing solvent molecules or voids in porous materials. 
   * **Delete atoms** – Remove selected atoms from the draw atom table. If you remove all atoms, the table is then refilled from the Atoms table. You should do this operation after any changes to the contents of the Atoms table, e.g. if atoms are added or deleted.
   * **Update draw atoms** – refresh the drawn atom positions from the Atoms list,  You should do this operation after any changes to the contents of the Atoms table, e.g. by a structure refinement. This operates on all atoms and ignores any previous atom selection. 
   * **Load selected atoms** - refresh the selected  atom positions in the draw atoms list from the Atoms list.

### Menu '**Compute**'  Contents

The compute menu gives a choice of geometric calculations to be performed with the selected atoms. You must select the appropriate number of atoms for these to work and the computation is done for the atoms in selection order.

   * **View pt. dist.** - this calculates distance from view-point to all selected draw atoms; result is given on the console window.
   * **Dist. Ang. Tors.** – when 2-4 atoms are selected, a distance, angle or torsion angle will be found for them. The angles are computed for the atoms in their selection order. The torsion angle is a right-hand angle about the A2-A3 vector for the sequence of atoms A1-A2-A3-A4. An estimated standard deviation is given for the calculated value if a current variance-covariance matrix is available. The result is shown on the console window; it may be cut & pasted to another application (e.g. Microsoft Word).
   * **Best plane** – when 4 or more atoms are selected, a best plane is determined for them. The result is shown on the console window; it may be cut & pasted to another application (e.g. Microsoft Word). Shown are the atom coordinates transformed to Cartesian best plane coordinates where the largest range is over the X-axis and the smallest is over the Z-axis with the origin at the unweighted center of the selection. Root mean square displacements along each axis for the best plane are also listed. The Z-axis RMS value indicates the flatness of the proposed plane. NB: if you select (e.g. all) atoms then Best plane will give Cartesian coordinates for these atoms with respect to a coordinate system where the X-axis is along the longest axis of the atom grouping and the Z-axis is along the shortest distance. The origin is at the unweighted center of the selected atoms.

### Menu '**Restraints**' Contents

Individual restraints may be generated by selecting atoms and the corresponding restraint type from the menu.

   * **Add bond restraint** – for selected atom pair (A-B).
   * **Add angle restraint** – for selected atom triple (A-B-C)
   * **Add plane restraint** – for selected 4 or more atoms
   * **Add chiral restraint** – for selected 4 atoms; chiral atom first followed by 3 other atoms; if selected in righthand sequence, chiral volume will be > 0.

### Menu '**Rigid body**'  Contents

 * **Define rigid body**' - Assign a previously defined rigid body to selected atoms.

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

A drawing that shows the atoms of the crystal structure is generated. The atoms are displayed according to the controls in the in this page as well as options on the [Draw Options](./phasedrawopts.md) page.

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

Use of the mouse buttons and key presses when viewing a crystal structure changes the view of the structure; this is [described on the Atoms tab](./phaseatoms.md#Phase-mouse-plotopts).


