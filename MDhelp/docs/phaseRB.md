<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="Phase-RB_Models"></a>
# **RB Models** phase tab

A rigid body is a collection of atoms that is treated as a group in GSAS-II. The position and orientation of the group can be refined and some other simplified parameters can also be varied, such as dihedral angles. Use of a rigid body requires two actions. First the rigid body must be defined for the project, see the [Rigid bodies tree item](./commontreeitems.md#Rigidbodies) for details on that. Then the rigid body must be inserted into a phase, which is done here, from the phases's RB Models tab. In this process, a number of parameters are defined for each body that determine how the rigid body is placed in the cell: the location in the cell for the rigid body origin, a rotation angle and orientation vector. These can be modified while being visualized, using the mouse by holding down the Alt key. 

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

A rigid body can be inserted into a phase using the "Locate & Insert Rigid Body" command in the "Edit Body" menu.

Once a body has been inserted into a structure, this tab provides access to the rigid body placement parameters, as well controls that determine how the rigid body is refined. Note that the selected rigid body can be positioned and oriented in the unit cell by holding down the Alt key (option on Mac) while "dragging" the mouse (moving the mouse while holding a mouse button down.) Dragging the mouse without the Alt key repositions the view of the cell.

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

Use of the mouse buttons when viewing a crystal structure changes the view of the structure. On a Mac with a one-button mouse, [some alternate actions must be used](./others.md#MacOS).

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

