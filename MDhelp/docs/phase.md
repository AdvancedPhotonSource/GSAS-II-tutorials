## Draw Options

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

The Draw Options window provides access to a number of items that control how the structure is displayed. If a map is available (Fourier of charge flipping), one can display a 10Åx10Å contoured slice centered at the viewpoint. Contouring done as lines, colors or lines & colors combined. 3-D contouring is also available as green (red for negative density) map grid points. One can also draw individual or stack of hkl planes across unit cell.

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

A drawing that shows the atoms of the crystal structure is generated. The way that the structure is displayed is determined according to the controls in this page as well as the options on the Draw Atoms page.

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

Use of the mouse buttons and key presses when viewing a crystal structure changes the view of the structure; see Atoms or Draw Atoms for details

## Draw Atoms

This gives a list of the atoms and bonds that are to be rendered as lines, van der Waals radii balls, sticks, balls & sticks, ellipsoids & sticks or polyhedra. There are four menus for this tab; Edit allows modification of the list of atoms to be rendered, Compute gives some options for geometric characterization of selected atoms, Restraints allows definition of 4 different types of restraints on the structure and Rigid body allows selection of atoms that form a previously defined rigid body.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. **Atom Selection from table**: select individual atoms by a left click of the mouse when pointed at the left most column (atom numbers) of the atom display; hold down the Ctrl key to add to your selection; a previously selected atom will be deselected; hold down Shift key to select from last in list selected to current selection. A selected atom will be highlighted (in grey) and the atoms will be shown in green on the plot. Selection without the Ctrl key will clear previous selections. A double left click in the (empty) upper left box will select or deselect all atoms.
2. **Atom Selection from drawing**: select an atom by a left click of the mouse while holding down the Shift key and pointed at the center of the displayed atom, it will turn green if successful and the corresponding entry in the table will be highlighted (in grey); any previous selections will be cleared. To add to your selection, use the right mouse button (Shift down); if a previously selection is reselected it is removed from the selection list. NB: beware of atoms that are hiding behind the one you are trying to select they may be selected inadvertently. You can rotate the structure anytime during the selection process.
3. **Double left click a Name, Type and Sym Op column heading**: a dialog box is shown that allows you to select all atoms with that characteristic. For example, selecting the Type column will show all the atom types; your choice will then cause all those atoms to be selected.
4. **Double left click a Style, Label or Color column**: a dialog box is shown that allows you to select a rendering option for all the atoms. For Color a color choice dialog is displayed that covers the entire color spectrum. Choose a color by any of the means available, press the "Add to Custom Colors", select that color in the Custom colors display and then press OK. NB: selecting Color will make all atoms have the same color and for Style "blank" means the atoms aren't rendered and thus the drawing will not show any atoms or bonds!
5. Menu '**Edit Figure**' - The edit menu shows operations that can be performed on your selected atoms. You must select one or more atoms before using any of the menu items. Most of these items can also be accessed by selecting one or more atoms and right-clicking the mouse.
    * **Atom style** – select the rendering style for the selected atoms
    * **Atom label** – select the item to be shown as a label for each atom in selection. The choices are: none, type, name or number. (NB: atom labelling slows drawing response time).
    * **Atom color** – select the color for the atom; a color choice dialog is displayed that covers the entire color spectrum. Choose a color by any of the means available, press the "Add to Custom Colors", select that color in the Custom colors display and then press OK.
    * **Reset atom colors** – return the atom color back to their defaults for the selected atoms.
    * **Edit atom radii** – modify atom radii used in the bond assignment algorithm.
    * **View point** – position the plot view point to the first atom in the selection.
    * **Select from list** – select atoms from a popup list of names.
    * **Add atoms** – using the selected atoms, new ones are added to the bottom of the list after applying your choice of symmetry operator and unit cell translation selected via a dialog display. Duplicate atom positions are not retained. Any anisotropic thermal displacement parameters (Uij) will be transformed as appropriate.
    * **Add sphere of atoms** – fill in all equivalent atoms that fall within a sphere of selected radius about selected atoms.
    * **Transform draw atoms** – apply a symmetry operator and unit cell translation to the set of selected atoms; they will be changed in place. Any anisotropic thermal displacement parameters (Uij) will be transformed as appropriate.
    * **Fill CN-sphere** – using the atoms currently in the draw atom table, find all atoms that belong in the coordination sphere around the selected atoms via unit cell translations. NB: symmetry operations are not used in this search; do Fill unit cell first.
    * **Fill unit cell** - using the atoms currently selected from the draw atom table, find all atoms that fall inside or on the edge/surface/corners of the unit cell. This operation is frequently performed before Fill CN-sphere.
    * **Complete molecule** – beginning with a selected atom, transform other atoms to equivalent positions that form a contiguous molecule. Not appropriate for continuous structures (a warning will appear)
    * **Create void map** – by using a grid of probe positions, locate points outside of normal contact distances within a structure. Result is a mesh of small blue points in structural voids (e.g. possible locations of missing water molecules).
    * **Delete atoms** – clear the entire draw atom table; it is then refilled from the Atoms table. You should do this operation after any changes in the Atoms table, e.g. by a structure refinement.
    * **Update draw atoms** – refresh the drawn atom positions from the Atoms list.
    * **Load selected atoms** - refresh the selected drawn atom positions from the Atoms list.

6. Menu '**Compute**' - The compute menu gives a choice of geometric calculations to be performed with the selected atoms. You must select the appropriate number of atoms for these to work and the computation is done for the atoms in selection order.

    * **View pt. dist.** - this calculates distance from view-point to all selected draw atoms; result is given on the console window.
    * **Dist. Ang. Tors.** – when 2-4 atoms are selected, a distance, angle or torsion angle will be found for them. The angles are computed for the atoms in their selection order. The torsion angle is a right-hand angle about the A2-A3 vector for the sequence of atoms A1-A2-A3-A4. An estimated standard deviation is given for the calculated value if a current variance-covariance matrix is available. The result is shown on the console window; it may be cut & pasted to another application (e.g. Microsoft Word).
    * **Best plane** – when 4 or more atoms are selected, a best plane is determined for them. The result is shown on the console window; it may be cut & pasted to another application (e.g. Microsoft Word). Shown are the atom coordinates transformed to Cartesian best plane coordinates where the largest range is over the X-axis and the smallest is over the Z-axis with the origin at the unweighted center of the selection. Root mean square displacements along each axis for the best plane are also listed. The Z-axis RMS value indicates the flatness of the proposed plane. NB: if you select (e.g. all) atoms then Best plane will give Cartesian coordinates for these atoms with respect to a coordinate system where the X-axis is along the longest axis of the atom grouping and the Z-axis is along the shortest distance. The origin is at the unweighted center of the selected atoms.

7. Menu '**Restraints**' – Individual restraints may be generated by selecting atoms and the corresponding restraint type from the menu

    * **Add bond restraint** – for selected atom pair (A-B).
    * **Add angle restraint** – for selected atom triple (A-B-C)
    * **Add plane restraint** – for selected 4 or more atoms
    * **Add chiral restraint** – for selected 4 atoms; chiral atom first followed by 3 other atoms; if selected in righthand sequence, chiral volume will be > 0.

8. Menu '**Rigid body**'/'**Define rigid body**' – assign a previously defined rigid body to selected atoms.

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

A drawing that shows the atoms of the crystal structure is generated. The atoms are displayed according to the controls in the in this page as well as options on the Draw Options page.

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

Use of the mouse buttons and key presses when viewing a crystal structure changes the view of the structure:

* **Left drag**: Holding down left button rotates axes around screen x & y
* **Right drag**: Holding down right button translates the fractional coordinates assigned to the viewpoint (which is kept at the center of the drawing). The structure will appear to translate. The viewpoint can also be entered directly in the Draw Options.
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

## RB Models

There are two actions associated with rigid bodies. First the rigid body must be defined for the project, see the Rigid bodies tree item for details on that. Then the rigid body must be inserted into a phase, which is done from each phases's RB Models tab. In this process, a number of parameters are defined for each body that determine how the rigid body is placed in the cell: the location in the cell for the rigid body origin, a rotation angle and orientation vector. These can be modified while being visualized, using the mouse by holding down the Alt key.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

A rigid body can be inserted into a phase using the "Locate & Insert Rigid Body" command in the "Edit Body" menu.

Once a body has been inserted into a structure, this tab provides access to the rigid body placement parameters, as well controls that determine how the rigid body is refined. Note that the selected rigid body can be positioned and oriented in the unit cell by holding down the Alt key (option on Mac) while "dragging" the mouse (moving the mouse while holding a mouse button down.) Dragging the mouse without the Alt key repositions the view of the cell.

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

Use of the mouse buttons when viewing a crystal structure changes the view of the structure:

* **Left drag**: Holding down left button rotates axes around screen x & y
* **Right drag**: Holding down right button translates the fractional coordinates assigned to the viewpoint (which is kept at the center of the plot). The structure will appear to translate. The viewpoint can also be entered directly in the Draw Options.
* **Middle drag**: Holding down center button rotates axes around screen z (direction perpendicular to screen).
* **Mouse Wheel**: Rotating the scroll wheel changes "camera distance" (zoom in/out).

Use of the Alt key causes the above mouse movements to reposition the rigid body rather than change the view of the crystal structure. This can be done when the rigid body is being added to a model or later by selecting the body.

When the rigid body is being initially inserted into a structure, both the rigid body and the crystal structure are displayed. The rigid body will be displayed with a "Balls-and-Sticks" model but bonds will be drawn in green. It is useful to plan for this by preselecting the atoms in the Draw Atoms list and to have atoms displayed as "Sticks" or "Balls-and-Sticks" etc. so that it is easy to differentiate positions of atoms already in the model from the new rigid body location.

When the rigid body has already been placed in the model, the rendering of the structure works a bit differently. As the rigid body is repositioned via Alt+mouse drag, all atoms in the Draw Atoms array are deleted and only the atoms in the asymmetric unit are displayed. The mode used to draw them will depend on the selection made on this window; (the default selection is "Balls-and-Sticks".) When the mouse button is released, if the "Fill cell" option is selected, the symmetry replicants of the atoms in the asymmetric falling inside the unit cell are placed into the Draw Atoms array.

Actions to reposition the rigid body in either mode are:

* **Alt+Left drag**: Holding Alt (Opt on Mac) while dragging the mouse with the left button down rotates the rigid body around screen x & y axes
* **Alt+Middle drag**: Holding Alt while dragging the mouse with the middle button down rotates the rigid body around screen z (out of screen) axis. On the Mac hold down the Alt and Command buttons together.
* **Alt+Right drag**: Holding Alt while dragging the mouse with the right button down (use Control+Opt on Mac with a single-button mouse) translates the rigid body in the screen x & y directions (rotate the plot to see and move in the rigid body in the third direction.) Selecting the "Lock" checkbox next to the origin location, or unselecting the "Refine?" button locks the origin from being changed via mouse dragging when the location should be fixed by symmetry.

## Texture

This tab is used to control settings used for a texture study of a material. This type of characterization usually requires diffraction data recorded with multiple detector orientations (the number of orientations will depend on sample and material symmetry). Do not confuse this with applying a [preferred orientation correction](./phase.md#preferred_orientation) (found in the ["Data" tab](#data)) in a structural study. The sample orientation relative to the detector axes is specified here and the detector orientation is specified for each histogram as goniometer omega, chi, phi and azimuth values (details below). These values must be specified.

Texture analysis using GSAS-II employs spherical harmonics modeling, as described by Bunge, "Texture Analysis in Materials Science" (1982), and implemented by Von Dreele, J. Appl. Cryst., 30, 517-525 (1997) in GSAS. The even part of the orientation distribution function (ODF) via the general axis equation

$$
A(x,y) = 1 + \sum_{L=2}^{N_L}{\frac{4\pi}{2L+1}} \sum_{m=-L}^{L} \sum_{n=-L}^{L} C_L^{mn} k_L^m(y) k_L^n(h)
$$

is used to give the intensity corrections due to texture. The two harmonic terms, \(k_L^m(y)\) and \(k_L^n(h)\) , take on values according to the sample and crystal symmetries, respectively, and thus the two inner summations are over only the resulting unique, nonzero harmonic terms. These unique terms are automatically selected by GSAS-II according to the space group symmetry and the user chosen sample symmetry. The available sample symmetries are cylindrical, 2/m, mmm and no symmetry. The choice of sample symmetry profoundly affects the selection of harmonic coefficients. For example, in the case of cylindrical sample symmetry (fiber texture) only \(k_L^0(y)\) terms are nonzero so the rest are excluded from the summations and the set of \(C_L^{0n}\) coefficients is sufficient to describe the effect on the diffraction pattern due to texture. The crystal harmonic factor, \(k_L^n(h)\), is defined for each reflection, h, *via* polar and azimuthal coordinates \((\phi, \beta)\) of a unit vector coincident with h relative to the reciprocal lattice. For most crystal symmetries, \(\phi\) is the angle between h and the n-th order major rotation axis of the space group (usually the c-axis) and \(\beta\) is the angle between the projections of h and any secondary axis (usually the a-axis) onto the normal plane.  In a similar way the sample harmonic factor, \(k_L^m(y)\), is defined according to polar and azimuthal coordinates \((\psi, \gamma)\) of a unit vector coincident with the diffraction vector relative to a coordinate system attached to the external form of the sample. For example, in the case of a rolled steel plate having mmm symmetry, the polar angle, \(\Psi\), is frequently measured from the normal direction (ND, parallel to K<sub>s</sub>) and g is then measured from the rolling direction (RD, parallel to I<sub>s</sub>) in the TD (transverse direction, parallel to J<sub>s</sub>) - RD plane.  Thus, the general axis equation becomes

$$
A(\phi,\beta,\psi,\gamma) = 1 + \sum_{L=2}^{N_L}{\frac{4\pi}{2L+1}} \sum_{m=-L}^{L} \sum_{n=-L}^{L} C_L^{mn} k_L^m(\psi, \gamma) k_L^n(\phi, \beta)
$$

Note that this version of the general axis equation differs from that shown in Von Dreele (1997) in that the assignment of m and n are reversed.

In a diffraction experiment the crystal reflection coordinates \((\phi, \beta)\) are determined by the choice of reflection index (hkl) while the sample coordinates \((\Psi, \gamma)\) are determined by the sample orientation on the diffractometer. To define the sample coordinates \((\Psi, \gamma)\), we have defined an instrument coordinate system (I, J, K) such that K is normal to the diffraction plane and J is coincident with the direction of the incident radiation beam toward the source. We further define a standard set of right-handed eulerian goniometer angles \((\Omega, X, \Phi)\) so that \(\Omega\) and \(\Phi\) are rotations about K and X is a rotation about J when \(\Omega = 0\). Finally, as the sample may be mounted so that the sample coordinate system (\(I_s, J_s, K_s\)) does not coincide with the instrument coordinate system (I, J, K), we define three eulerian sample rotation offset angles \((\Omega_s, X_s, \Phi_s)\) that describe the rotation from (\(I_s, J_s, K_s\)) to (I, J, K).  The sample rotation angles are defined so that with the goniometer angles at zero \(\Omega_s\) and \(\Phi_s\) are rotations about K and \(X_s\) is a rotation about J.  The zeros of these three sample rotation angles can be refined as part of the Rietveld analysis to accommodate any angular offset in sample mounting. For the specific case of cylindrical sample symmetry, the cylinder axis is coincident with Ks as is the 2-fold in 2/m sample symmetry. After including the diffraction angle, \(\Theta\), and a detector azimuthal angle, A, the full rotation matrix, \(M\), is

$$
M = - \Theta A \Omega X (\Phi + \Phi_s) X_s \Omega_s
$$

By transformation of unit Cartesian vectors (100, 010 and 001) with this rotation matrix, the sample orientation coordinates \((\Psi, \gamma)\) are given by

$$
cos(y) = M \begin{pmatrix}
0 \\
0 \\
1
\end{pmatrix}
$$

and

$$
tan(\gamma) = M \begin{pmatrix}
0 \\
1 \\
0
\end{pmatrix}/ M
\begin{pmatrix}
1 \\
0 \\
0
\end{pmatrix} 
$$

The harmonic terms, \(k_L^m(\psi, \gamma)\) and \(k_L^n(\phi, \beta)\), are developed from (those for \(k_L^m(\psi, \gamma)\) are similar)

$$
k_L^n(\phi, \beta) = \frac{1}{\sqrt{2\pi}} e^{in\beta} \bar{P}_L^n(cos(\phi))
$$

where the normalized associated Legendre functions, \(\bar{P}_L^n(x)\), are defined via a Fourier expansion as

$$
\bar{P}_L^n(cos(\phi)) = \sum_{s=0}^L {a'}_L^{ns} sin(s \phi)
$$

for n even and

$$
\bar{P}_L^{ns}(cos(\phi)) = \sum_{s=0}^L {a'}_L^{ns} sin(s \phi)
$$

for n odd.  Each sum is only over either the even or odd values of s, respectively, because of the properties of the Fourier coefficients, \({a'}_{L}^{ns}\). These Fourier coefficients are determined so that the definition

$$
\bar{P}_L^{n}(cos(\phi)) = \bar{P}_L^{n}(x) = \sqrt{\frac{(L+n)!}{(L-n)!}} \sqrt{\frac{2L+1}{2}} \frac{(-1)^{L-n}}{2^L L!} (1-x^2)^{-n/2} \frac {d^{L-n}}{dx^{L-n}} (1-x^2)^L
$$

is satisfied. Terms of the form \( cos(n\beta) \bar{P}_L^n(cos{n\beta})\) and \(sin(n\beta) \bar{P}_L^n(cos{\phi})\) are combined depending on the symmetry and the value of n (or m) along with appropriate normalization coefficients to give the harmonic terms \(k_L^n(\phi,\beta)\) and \(k_L^m(\psi,\gamma)\). For cubic crystal symmetry, the term \(k_L^n(\phi,\beta)\) is obtained directly from the Fourier expansion

$$
k_L^n(\phi, \beta) = \sum_{j=0}^L B_L^{nj} \bar{P}_L^n (cos{\phi}) cos{n\beta}
$$

using the coefficients, \(B_L^{nj}\) , as tabulated by Bunge (1982).

The Rietveld refinement of texture then proceeds by constructing derivatives of the profile intensities with respect to the allowed harmonic coefficients, \(C_L^{mn}\), and the three sample orientation angles, \(\Omega_s, X_s, \Phi_s\) Ws, Cs, Fs, all of which can be adjustable parameters of the refinement. Once the refinement is complete, pole figures for any reflection may be constructed by use of the general axis equation, the refined values for \(C_L^{mn}\) and the sample orientation angles \(\Omega_s, X_s, \Phi_s\).

$$
J = 1 + \sum_{L=2}^{N_L} \frac{1}{2L+1} \sum_{m=-L}^{L} \sum_{n=-L}^{L} |C_L^{mn}|^2
$$

The magnitude of the texture is evaluated from the texture index by

If the texture is random then J = 1, otherwise J > 1; for a single crystal J = \(\infty\).

In GSAS-II the texture is defined in two ways to accommodate the two possible uses of this correction. In one, a suite of spherical harmonics coefficients is defined for the texture of a phase in the sample; this can have any of the possible sample symmetries and is the usual result desired for texture analysis. The other is the suite of spherical harmonics terms for cylindrical sample symmetry for each phase in each powder pattern ("histogram") and is usually used to accommodate preferred orientation effects in a Rietveld refinement. The former description allows refinement of the sample orientation zeros, \(\Omega_s, X_s, \Phi_s\), but the latter description does not (they are assumed to be zero and not refinable). The sample orientation angles, \(\Omega, X, \Phi\) are specified in the Sample Parameters table in the GSAS-II data tree structure and are applied for either description.

Some useful examples:

**1. Bragg-Brentano laboratory powder diffractometer**

The conventional arrangement of this experiment is to have a flat sample with incident and diffracted beams at equal angles (theta) on opposite sides of the sample. The sample is frequently spun about its normal to improve powder statistics and impose cylindrical symmetry on any preferred orientation (texture). Thus, the diffraction plane (source, diffraction vector & detector) contains the K-vector which is parallel to the diffraction vector and \(\Omega, X, \Phi = 0\).

**2. Debye-Scherrer diffractometer with point detector(s)**

The usual arrangement here is to have a capillary sample perpendicular to the diffraction plane. The capillary may be spun about its cylinder axis for powder averaging and to impose cylindrical symmetry on the texture which is perpendicular to the diffraction plane. Thus, \(\Omega,\Phi = 0\) and \(X = 90\).

**3. Debye-Scherrer diffractometer with 2D area detector**

The area detector is presumed to be directly behind the sample with the incident beam somewhere near the center of the detector. The detector axes are defined (for a synchrotron) with the X-axis toward the synchrotron ring and the Y-axis vertical "up"; one views the detector image as if looking from the x-ray source. The sample is assumed to be a capillary (which may be spun to impose cylindrical symmetry), although other sample shapes may be used, and is aligned with the cylinder axis horizontal. Integration of the image from a series of "caked" slices gives a set of powder patterns, each assigned an azimuthal angle where zero is along the X-axis. Thus, at azimuth=0 the diffraction plane is horizontal and contains the cylinder axis so \(\Omega\), X, \(\Phi\) = 0.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. Menu '**Texture/Refine **texture' – refines the spherical harmonics texture model using the previously determined values of Prfo for all histogram reflection sets as demonstrated in 2DTexture tutorial.
2. **Texture settings** - The texture index, J is shown on the 1st line.
    
    * The Texture model can be chosen from ['cylindrical', 'none', 'shear - 2/m', or 'rolling – mmm'].
    * The Harmonic order (even integer 0-34), refine flag & show coefficients flag are next.
    * The Texture plot type is one of:
        * **Axial pole distribution** which simulates the intensity of a reflection during a phi scan.
        * **pole figure** where a projection of the probability of finding a pole (hkl) is plotted as a function of sample orientation.
        * **inverse pole figure** where a projection of the probability of finding all poles (hkls) is plotted for a selected sample orientation.
        * **3D pole distribution** that shows the probability of finding a pole (hkl) is plotted as a function of sample orientation.

    For Axial distribution, pole figure and 3D pole distribution one must next select the hkl of the desired pole, for Inverse pole figure one must select a sample direction (typically 0 0 1).

    One can choose the contour (pole & inverse pole figures) color scheme (default "Paired") and make a CSV file of the image for import into other software.

    * The spherical harmonics coefficients are shown next; they may be edited. They may be cleared by setting harmonic order to zero and then back to desired value.
    * The sample orientation angle zeros \((\Omega_s, X_s, \Phi_s)\) are shown with their individual refinement flags.

## Map peaks

This gives the list (magnitude, x y & z) of all peaks found within the unit cell from the last Fourier/charge flip map search sorted in order of decreasing peak magnitude. The crystal structure plot shows each peak position as a white to dark gray cross; the shade is determined from the magnitude for the peak relative to the maximum peak magnitude; some are connected by white sticks as possible bonds. Negative peaks are shown in orange.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

* **Peak Selection from table**: select individual atoms by a left click of the mouse when pointed at the left most column (atom numbers) of the atom display; hold down the Ctrl key to add to your selection; a previously selected atom will be deselected; hold down Shift key to select from last in list selected to current selection. A selected atom will be highlighted (in grey) and the atoms will be shown in green on the plot. Selection without the Ctrl key will clear previous selections. A left click in the (empty) upper left box will select or deselect all atoms.
* **Select the mag column** – the entries will be sorted with the largest at the top.
* **Select the dzero column** – the entries will be sorted with the smallest (distance from origin) at the top.
* **Select the dcent column** – the entries will be sorted with the smallest distance from the unit cell center at the top.
* Menu '**Map peaks**'  –
    
    * **Move peaks** – this copies selected peaks to the Atoms list and the Draw Atoms list. They will be appended to the end of each list each with the name 'UNK' and the atom type as 'H'. They will also be drawn as small white spheres at their respective positions in the structure drawing. You should next go to the Atoms page and change the atom type to whatever element you desire; it will be renamed automatically.
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

## Pawley reflections

This gives the list of reflections used in a Pawley refinement; for them to be used the 'Do Pawley refinement' flag must be set (see General), otherwise they are ignored.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

* Menu '**Operations**' –

    * **Pawley settings** – allows setting of Pawley parameters as shown on the General tab.
    * **Pawley create** – this creates a new set of Pawley reflections, over writing any preexisting Pawley set. They are generated with d-spacings larger than the limit set as 'Pawley dmin' in the General tab for this phase. By default, the refine flags are not set and the Fsq(hkl) = 100.0.
    * **Pawley estimate** – this attempts an estimate of Fsq(hkl) from the peak heights of the reflection as seen in the 1st powder pattern of those shown as 'Use' in the Data tab for this phase.
    * **Pawley update** – process Pawley reflection set for negative intensities. These are set to ½ its absolute value for noncentrosymmetric space groups (0.3 otherwise); the refine flag is turned off. One should repeat Pawley refinement and then do Refine all and an additional refinement. Repeat as needed to remove negative intensities. Set Pawley neg. wt. (see Pawley settings) to further suppress negatives.
    * **Refine all** – sets all refine flags
    * **Refine none** – clears all refine flags
    * **Toggle selection** – toggles all refine flags

* You can change the refine flags either by clicking on the box or by selecting one and then selecting the column (a single click on the column heading). Then type 'y' to set the refine flags or 'n' to clear the flags. You should not refine those reflections that are below the lower limit or above the upper limit of the powder pattern otherwise you will have singular matrix errors in your Pawley refinement (adds to the refinement time as bad parameters are removed). Reflections that fall inside excluded regions may also result in refinement singularities.
* You can delete an individual reflection from the Pawley set by selecting its row (will be highlighted) and then pressing the Delete key (this is not reversable & only deletes the 1st one selected).
* You can change the individual Fsq(hkl) values by selecting it, typing in the new value and then pressing enter or selecting somewhere else in the table.
Layers

This is used to set up stacking fault models for simulations of x-ray diffraction patterns. See for example the Stacking Faults-I tutorial. The computations are done by a modified version of DIFFaX. See M.M.J. Treacy, J.M. Newsam and M.W. Deem, Proc. Roy. Soc. Lond. 433A, 499-520 (1991) for more information on DIFFaX and please cite this if you use this section of GSAS-II.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. Menu '**Operations**' –

    * **Load from DIFFaX file** – load parameters from a DIFFaX input file
    * **Copy phase cell** – copy the lattice parameters from a selected phase (usually transformed from average unit cell)
    * **Simulate pattern** – run DIFFaX to simulate selected pattern
    * **Fit pattern** – refine stacking fault parameters to fit observed pattern (not available yet)
    * **Sequence simulations** – do a sequence of simulations incrementing a selected stacking fault parameter

2. Show a plot of the 2D diffraction pattern for the stacking model – look for streaks.
3. Select Laue symmetry
4. Reference unit cell – filled by Copy phase cell and is the stacking fault block dimensions (NB: refine inactive)
5. Layer width (a & b) – outer dimensions of crystallite; used for broadening calculations (NB: refine inactive)
6. Next are descriptions of the layers to be used in the calculations. They can be created atom-by-atom or imported from another GSAS-II gpx file. If a layer is already present, then the new layer can be the same; give it a different name.
7. The layers stack according to probability rules – these are presented in tables in the next section
8. You can specify specific layering sequences as a sequence of layer numbers (begins with 1).
9. Finally, you can set the type of sequence and the number of layers to use in the simulation

You can draw the layer structures as well as sequences of layers to check on how they fit together; see the Plot boxes for this.

## Wave Data

This tab displays the modulation functions used for incommensurate structures; it will not appear if the structure is commensurate (i.e. 3D). They include modulations on atom site fractions, positions and thermal motion parameters. If the structure is magnetic, atom moment modulation parameters are also shown.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. Select an atom from the Atoms list; the pulldown shows them by name. The display will show the assigned modulations, if any.
2. Add a modulation wave and define its type; window will be redrawn showing allowed coefficients (white background) and symmetry fixed or dependent coefficients (gray background).
3. Select a modulation wave to refine. Holds can be used to fix individual coefficients (see Constraints).
4. Delete a modulation wave.
5. If a 4D map is available (Fourier or charge flip), a contour plot showing density modulation along tau for a selected 3D axis of the selected atom. The +/- keys can be used to adjust the phase offset of the map so it matches the calculated modulation curve.

## MC/SA

This tab displays Monte Carlo/Simulated Annealing model parameters and results. Each rigid body is described by a location (fractional x,y,z) and a quaternion description for the orientation (rotation angle & 3D vector) along with possible bond torsion angles on side chains. Each parameter has a defined range. The MC/SA controls on the General tab further limit the MC/SA run. Selection of a result shows a drawing of the structure with unit cell contents for visualization.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. Modify the preferred orientation model (currently not operational)
2. **MC/SA** Menu –
    * **Add atom** – add an isolated atom to the MC/SA model
    * **Add rigid body** – add a previously defined rigid body, which may have adjustable internal torsion angles.
    * **Clear rigid bodies** – removes rigid bodies from the MC/SA model
    * **Clear results** – clears table of MC/SA results from a previous set of MC/SA trials.

## RMC

This displays 3 different setups each for RMCProfile, fullrmc and PDFfit as selected by a radio button at the top of the window. RMCProfile and fullrmc are "big box" modelling routines and PDFfit is a "small box" modelling routine; all for fitting structural models to pair distribution functions (PDF). Tutorials for using RMCProfile and PDFfit can be found in the GSAS-II Help; fullrmc is currently under construction. These routines all run as stand-alone applications which are initiated by GSAS-II. When finished, GSAS-II processes their output files to update parameters that are within the GSAS-II project. The two big box routines can have very long running times; they run as separate console programs. GSAS-II is active while they are running and can "interrogate" them for intermediate results. PDFfit has a short running time and GSAS-II is "locked out" until it finishes; its result can be examined after.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

**Operations** Menu –
    * **Setup RMC** – this builds the input files and python script (if needed) for running the selected RMC program.
    * **Execute** – this executes the chosen RMC program in a new console which will vanish when finishes (after a "press any key" command). When finished, GSAS-II will extract results and place them in appropriate places in the project.
    * **Stop run** – only valid for fullrmc; stops the RMC run & saves progress so it can be continued later.
    * **Plot** – this displays the resulting graphical output from the RMC run. For RMCProfile and fullrmc this can be 5 or more plots, for PDFfit it is only the observed and calculated G(r) plot with a difference curve.

For each program, the setup page is similar. There is a block for "metadata" items for your convenience; they have no impact on the calculations. Next is timing controls for the big box programs (PDFfit has none). Then is structural information and finally the data section for the patterns to be fitted. The big box programs are for only single runs while PDFfit can be used to process a sequence of G(r) data collected as a function of, e.g., temperature (giving Sequential PDFfit2 results).

### fullrmc

The fullrmc program is a large-box pair distribution function modeling library developed by Bachir Aoun [Fullrmc, a Rigid Body Reverse Monte Carlo Modeling Package Enabled with Machine Learning and Artificial Intelligence", B. Aoun, Jour. Comp. Chem. (2016), 37, 1102-1111. [DOI: 10.1002/jcc.24304](https://doi.org/10.1002/jcc.24304)]. Extensive information about fullrmc is found, including a number of explanatory videos, along with older source code on GitHub: [https://bachiraoun.github.io/fullrmc/](https://bachiraoun.github.io/fullrmc/). Note that the GSAS-II implementation is not compatible with the open-source version of fullrmc, but rather the new version 5.0 must be used, which is distributed as a compiled versions for 64-bit Intel-compatible processors running Windows, Linux and MacOS from website [https://github.com/bachiraoun/fullrmc/tree/master/standalones](https://github.com/bachiraoun/fullrmc/tree/master/standalones). Note that an even newer and more powerful version of fullrmc is available for cloud computing by subscription at [https://fullrmc.com](https://fullrmc.com). When fullrmc is selected in this tab, GSAS-II use the GSAS-II configuration variable `fullrmc_exec`, which if defined points to a Python image with fullrmc. Otherwise GSAS-II will look in the following places, in the order specified, for a Python image for a file named `fullrmc5*64bit` (MacOS or Linux) or `fullrmc5*.exe` (Windows):

1. The location where GSAS-II is installed,
2. The location where Python is installed,
3. The location where the GSAS-II binaries are found,
4. the current default location
5. and all directories in the system path. 

## ISODISTORT

This displays the setup for using the web-based application, [ISODISTORT](https://iso.byu.edu/iso/isodistort.php), to identify the possible mode distortions of a parent structure. To use it you must be connected to the internet. Two ISODISTORT Methods are supported in GSAS-II: Method-1 identifies all possible subgroups that result from simple mode distortions that are associated with a single irreducible representation. Method-4 is more useful in that it finds the mode decomposition of a parent structure to give a specified distorted structure and is set up to find only atom displacement modes. See help pages for [ISODISTORT](https://iso.byu.edu/iso/isodistort.php) for more information. The ultimate product of using ISODISTORT is a special cif file with constraints describing the mode distortions; this is imported into GSAS-II to form a new phase with these constraints.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

If this is a freshly created phase (not an imported ISODISTORT cif) then you can choose the Method (4 is default) and select parent structure and distorted child structure (for Method 4).

If you chose Method 1 & run ISODISTORT, a table of possible substructures is displayed; a cif file with mode distortion constraints can be produced from your selection. The table can be filtered by crystal class.

If this is a phase imported from an ISODISTORT cif file, the mode displacements are shown with sliders to allow visualization of the displacements in a drawing of the crystal structure (prepare this first before trying a slider). A structure refinement using this phase will employ the mode distortions as constraints on the atom coordinates; there should be as many as there are free variable coordinates in the structure. The values (in Å) represent the largest atom shift associated with the mode; shown is a list of atom coordinates affected by each mode.

* **Operations** menu –
    * **Run ISODISTORT** – run this from the web site with the controls as shown.
    * **Make cif file** – active after table from Method 1 is displayed; generate cif file by ISODISTORT web site with mode distortion constraints.
    * **Make PDFfit phase** – active when mode distortions are shown. Makes new phase specific for fitting PDF data via PDFfit2.
    * **Show modes** – active when mode distortions are shown. Displays mode names & values.
    * **Show relationships** - active when mode distortions are shown. Displays constraint equations associated with mode distortions.

## Dysnomia

This is displayed if the **Use Dysnomia** box in the General tab is checked. [Dysnomia](https://doi.org/10.1017/S088571561300002X) is a maximum entropy method for improving Fourier density maps. The Dysnomia tab gives controls for its operation.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

* **Operations** menu –
    * **Load from Dysnomia file** – as previously saved set of controls.
    * **Save Dysnomia file** – saves data needed to run Dysnomia
    * **Run Dysnomia** – execute the routine from GSAS-II (not a separate console). Replaces existing map with one improved by maximum entropy.
