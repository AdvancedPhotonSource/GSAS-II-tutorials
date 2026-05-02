<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="PWDR_Limits"></a>
#  PWDR **Limits** sub-data tree item (Powder Diffraction)

This data tree subentry window controls the limits in position to be used in any fitting for this powder pattern. The "original" values are obtained from the minimum & maximum values in the powder pattern. The "new" values determine the range of data that will be used in fitting, Tmax and Tmin. Tmin and Tmax will be either 2θ (deg.) for CW data or time (μsec) for TOF data. 

You can also designate areas of the pattern that should be "excluded", meaning that they will not be included in the refinement. This should be be done when there is a well-understood reason why that region is expected to have spurious intensities (such as scattering from a furnace). For the computed pattern (shown as a green line from a fit, no computed pattern is shown for data in an excluded region.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

You can change the 'new' values for Tmin and Tmax as needed. Change the upper (Tmax) and lower (Tmin) values by clicking on the appropriate vertical line and dragging it to the right or left, or by typing values into the data window, or using the "Set lower limit" or "Set upper limit" commands in the "Edit Limits" menu and then click on a point in the pattern.

The Limits plot is the only place where one can designate that sections of the data will not be used ("excluded regions").
You can add an excluded region using the "Add excluded region" command in the "Edit Limits" menu and then click on a point in the pattern. This creates region at that point. Edit the region by dragging the magenta lines or by editing the values in the data window.

### "**Edit Limits**" Menu Commands

**Copy**: This copies the limits shown for the selected pattern to other powder patterns. After using this menu command, a dialog box (Copy Parameters) will appear showing the list of available powder patterns, you can copy the limits parameters to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.

**Set lower limit**/**Set upper limit**: These menu items are used to select a location in the pattern to set as Tmin or Tmax. After using the menu command, click on a point in the pattern at the appropriate location.

**Add excluded region**: Select this menu item and click on a region to start a new excluded region, but do not release the button. Drag the mouse to the location where 
the excluded region ends and then release the mouse button. 
A pair of magenta lines is drawn to indicate a range that should be excluded. The magenta lines can be dragged, as described below to edit the region location. 

**Cancel Set**: Resets the "Add excluded region", "Set lower limit" or "Set upper limit" command so that no change is made. 

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

The plot is the largely the same as for the parent PWDR Powder Histograms tree entry 
[with many of the same plot actions](./powder.md#PWDR_plot_actions). 

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

The Limits plot employs mostly the [same key press commands](./powder.md#PWDR_keylist) as for the PWDR parent. However, tickmarks and the obs-calc position cannot be dragged and plotting 
can only be done in the native units of the dataset (\(2\theta\) or TOF). To set limits in Q or d-space mode, use the Background data tree entry. 

What is unique to the plot associated with the Limits data tree subentry is that the entire pattern is shown, including data outside the limits and regions that are ignored (this can be toggled with the "x" key).
Also, vertical lines are displayed for the fitting limits: green for the lower Tmin value and red for the upper Tmin value. Excluded regions are displayed with pairs of magenta vertical lines. 
All these vertical lines can be dragged to set limits or edit excluded regions.

One key press command, "e", is unique to Limits plots and another, "x", has a slightly different action:

 * "e" is used to define excluded regions (see below),
 * "x" toggles if data above/below data limits are shown (unique to Limits) as well as toggles if excluded regions are shown.

#### Draggable plot elements:

* The upper and lower Tmin values can be changed by clicking on the appropriate vertical line and dragging it to the right or left. 
* A of a limit drag beyond the end of the pattern will reset that limit to the original value. 

#### Excluded regions:

Excluded regions can be created by either of two methods, depending on the preference of the user: from the "Edit Limits"/"Add excluded region"
menu commands or with an "e" keypress. 

  * To create an excluded region using the keyboard, move the mouse to the starting position for the region and press the "e" keyboard key, then move to the end of the region and press the "e" key again. 
  * See above for a description of how to use the "**Add excluded region**" menu command.
  * Excluded regions can be modified by dragging the lines, if desired.
