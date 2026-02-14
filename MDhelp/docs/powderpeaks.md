<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="PWDR_Peak_List"></a>
#  PWDR **Peak List** subdata tree item (Powder Diffraction)

The Peak List data tree entry is used to fit diffraction peaks at refined or user-supplied positions (not generated from a unit cell). Peak positions and intensities may be selected for individual refinement. There are four modes available here for treatment of peak widths: 
1) Gaussian ($\sigma^2$) and Lorentzian (\(\Gamma\)) peak widths may be varied individually, 
2) the width values may be generated from the the appropriate profile terms in the Instrument Parameters tree item (U, V & W for \(\sigma^2\); X & Y for \(\Gamma\)), where those terms may optionally be refined. 
3) It is possible to mix refinement of XY terms and fit a few individual  (\(\Gamma\)) peak widths, but this is not possible with the UVW terms. When any individual ($\sigma^2$) peak widths are fit, it is not possible to refine the U, V or W terms. Note that when individual widths are refined, the fitted values override the values that would be generated from the UVW/XY terms, except as noted in the next mode.
4)It is possible to turn off the setting of individual (\(\sigma^2\) or \(\Gamma\) peak width values) peak width  If  are refined, then those value(s) in the table are used as the refinement starting point. If values are not refined, then normally the unvaried widths are determined from the appropriate Instrument Parameters profile terms and are placed in the table prior to fitting. When the "Gen unvaried widths" menu item is turned off, the unvaried peak with values are not computed from the Instrument Parameters; this must be turned on  (the default mode) to vary Instrument Parameters.

Note that the Gaussian full-width at half-maximum is given by 

$$FWHM = \sqrt{8 * \ln 2 * \sigma^ 2}$$

while \(\Gamma\) is the Lorentzian FWHM. The \(\sigma^2\) values (peak variances) are in units of centidegrees\(^2\) (centidegrees are degrees*100) for CW data or microseconds\(^2\) for TOF data; \(\Gamma\) has units of centidegrees or microseconds. Except in very unusual circumstances, instrumental broadening is Gaussian and will be a slowly-changing function of Q and sample broadening is strictly Lorentzian and while this may be only a function of Q, it can vary from peak to peak if the sample is a mixture of phases, or anisotropic peak broadening is present. Thus, it makes sense to fit Gaussian widths only using the U, V & W terms and indeed the software will not allow those terms to be varied if 
*any* 
individual peak \(\sigma^2\) terms are varied as this usage would not make sense physically. 
This is different for X & Y and individual peak \(\Gamma\) values. The refinement of X & Y, while fitting of *some* individual peak \(\Gamma\) values is allowed and this can make sense physically, but note that one should have a sufficient number of peaks that are not being fit individually and these peaks should be distributed over a wide range in Q when X & Y are fit simultaneously.

For peak fitting, the background is generated using the parameters in the Background data tree entry. Also, the range of data used in the fit is set from the Limits tree item. In both cases these are the same values that are used in Rietveld fits. Note that optionally the parameters on the Background and in the Instrument Parameters tree items may be refined during peak fitting, but in the case of U, V & W, these values cannot be refined if any individual \(\sigma^2\) values are fit. 
 
<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

There are three ways to interact with Peak List data tree item: through its menu, labeled Peak Fitting, through interaction with the peak list table, and through interactions with the plot.

The following interactions are available with the peak table:

* You can change individual peak coefficient values. Enter the value then press Enter or Tab or click the mouse elsewhere in the Peak List window. This will set the new value.
* You can change the individual refine flags by clicking on the individual check boxes.
* You can change all refine flags in a column by clicking on a single flag and then click on the column label above. (The entire column should then be highlighted in blue.) Type 'y' to set the refine flags or 'n' to clear the flags. You can also change flags for an entire column by double-clicking on the column label, which brings up a menu where "Y" or "N" can be selected.
* You can delete peaks in the Peak List by selecting a row by clicking on the row label to the left (multiple selection of rows is allowed). Selected rows will be highlighted in the plot (see below). Then press the Delete or backspace key. (Note that peaks can also be deleted from the plot, see below.)
* You can highlight a peak in the plot by double-clicking on the row label (to the left) for a peak.
* Pressing "d" in the plot window causes the next peak in the table (or the first if none are selected) to be selected and causes that peak to be highlighted in the plot; pressing "u" causes the previous peak in the list to be highlighted. 

### "**Command**" Menu Commands

The menu for Peak Fitting contains the following commands:

* **Set sel. ref flags** - If one or more rows of peaks are selected by clicking on the peak label to the left, this menu item can be used to set the refinement flags for the selected reflections.

* **Set all ref flags** - This sets refinement flags for all peaks in the table.

* **Auto search** - This fills the table with peak positions. These are selected based on peak tops that are substantially above background. Noisy data will give spurious peaks, and small peaks or shoulders will necessarily not be found. Examine results & modify as needed.

* **UnDo** - Resets peak parameters, background and instrument parameter values varied in the last peak fitting refinement back to their original values. Use this to recover from a failed refinement. Note: only one previous refinement is saved, so this cannot be pressed twice to return to the refinement before the previous.

* **PeakFit** - Performs a least squares fit of the peaks in Peak List to the data. Any peak parameters, background parameters and instrument parameters with refine checked will be varied in this refinement. The refinement will proceed until convergence. We suggest you vary the peak intensities along with the background first (the default), then vary the position and instrument parameters after. The order will depend on how poor is the initial estimate of the instrument parameters (U, V, W, X, Y & SH/L). To determine how to proceed, examine in detail the powder pattern difference curve displayed in the GSASII Plots window. If individual peaks show peak widths that are widely different, their individual \(\sigma^2\) and \(\Gamma\) parameters may be refined. If the refinement results in negative peak coefficients, these will be highlighted in red. If this happens, you should use the UnDo menu item (above) to return to the refinement and reconsider your choice of parameters to be varied.

* **Peakfit one cycle** - Perform a single cycle of least squares refinement. This can be used in difficult cases to get a refinement started toward convergence.

* **Reset sig and gam** - This resets the values of \(\sigma^2\) and \(\Gamma\) in the table to those computed from the instrument parameters U, V, W, X & Y.

* **Peak copy** - Copy the current set of peaks to other histogram(s).

* **Seq PeakFit** - Fit peaks for multiple histograms; results will be in [Sequential peak fit](./sequential.md) results.

* **Clear peaks** - This removes all the peaks from the Peak List.

* **Move selected peak** - A peak may be moved using the following process: select it in the table by clicking on its label (to left), use this menu item. The peak line will then follow movement of the mouse in the plot window. Click with the left mouse button to set a new position. Click with the right mouse button to delete that peak. Click outside the axes to abort the move and return to the previous position. (Note that peak movement is also possible with the plot window, see below.)
<a name="GenUnvariedWidths"></a>

* **Gen unvaried widths** - This determines how \(\sigma^2\) and \(\Gamma\) values are treated when unvaried. When this item is checked (the default mode), unvaried Gaussian (\(\sigma^2\)) and Lorentzian (\(\Gamma\)) peak widths will be generated from the the appropriate profile terms in the Instrument Parameters tree item (U, V & W for \(\sigma^2\) X & Y for \(\Gamma\)). This allows those Instrument Parameters to be refined. If this mode is changed and the "Gen unvaried widths" mode is unchecked the the \(\sigma^2\) and \(\Gamma\) peak widths are used as supplied, but then it is not possible to refine Instrument Parameters. This mode will not affect \(\sigma^2\) and \(\Gamma\) values that have their refine flag checked.

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

The plot is the largely the same as for the parent PWDR Powder Histograms tree entry 
[with the same plot actions](./powder.md#PWDR_plot_actions) and [same key press commands](./powder.md#PWDR_keylist). Specific to this plot are the peak positions that are shown as vertical dashed blue lines. To show that a peak is selected, it is highlighted in yellow and the blue line is made wider. The upper and lower data limits are shown as red and green dashed vertical lines, respectively, and can be dragged to change the fitting range. 

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

For all actions involving mouse clicks such as those below, be sure that the Zoom/Pan buttons are not selected on the Plot window, as the mouse will be used for zooming or panning, not the desired action.

* You can add peaks to the Peak list using the mouse on the plot by: position the cursor pointer onto a cross for an observed point and pressing the left mouse button. The selected peak will be added to the Peak List in the appropriate position to keep peaks sorted and a blue vertical line will be plotted on that position. We recommend that you begin picking peaks from the right side of the pattern; that way the tool tip won't be in your way as you select peaks.
* You can delete peaks using the mouse on the plot by positioning the pointer on the blue line for the peak to be deleted and then pressing the right mouse button. The blue line should vanish, and the corresponding peak will be removed from the Peak List.
* You can move a Peak List item using the mouse on the plot: position the pointer on the blue line for the peak you wish to move and then hold the left mouse button down, dragging the line to the desired position. When the mouse button is released, the peak line will be drawn in the new position.
* The fit limits can be changed from the plot either here or in the Limits data tree. Change the upper and lower Tmin/Tmax values by clicking on the appropriate vertical line and dragging it to the right or left.
* Highlight each peak in the list successively using the "d" keyboard key to move down the list or "u" to move up the list. 


### "**Extra Peak**" Mode

When working with full-pattern fits, it is sometimes useful to pay attention only to the peaks that are not being indexed and fit by the full pattern fit. One reason for this may be to learn more about a phase that is not currently being fit or with magnetic scattering, one may have fit the chemical ("nuclear") structure and one needs to identify the additional peaks that are seen at a temperature below a magnetic phase transition in order to understand the lowered symmetry of the magnetic lattice. Similarly one may wish to explore a phase transition lowering of symmetry. In "Extra Peak mode", individual peak fitting is performed not on the diffraction data, but rather on the "difference curve," the observed pattern with the computed pattern subtracted. A separate peak list is kept for these "extra peaks". This "Extra Peak Mode" can be entered either from pressing the button labeled "Switch to In "Extra Peak mode", or by using the checkmark menu button in the "Peak Fitting" menu labeled "Add impurity/subgrp/magnetic peaks."
