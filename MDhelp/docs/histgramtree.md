# Help for GSAS-II – Powder Diffraction Tree Items

This is where to find information on the Tree item in GSAS-II associated with powder diffraction (labeled PWDR) and its associated subitems. GSAS-II use the label of "histogram" for datasets of any type (single-crystal, powder,...) Powder diffraction histograms are added to a project using the Import/"Powder Data" menu items. After data are read, if there are phases present, you will be offered a chance to link the imported histograms to the previously imported phase(s). Likewise, if phase(s) are imported after histograms you will also be asked to link the new phase(s) to existing histograms. It is also possible to add histograms to a phase later by selecting that phase in the data tree and then selecting the "Data" tab and finally using the "Edit Phase"/"Add powder histograms" menu command. Note that there is no limit to the number of histograms that can be included in a GSAS-II project (other than as limited by available computer memory) and histograms that are not linked to at least one phase are ignored in refinements. 

# Histogram data tree items

These are shown in the data tree with a prefix of 'PWDR', 'HKLF', 'PDF', 'IMG', 'PKS', 'SASD', 'REFD' or and usually a file name. These constitute the data sets ('Histograms') to be used by GSAS-II for analysis. Selection of these items does not produce much information in the data window but does display the data in the Plots Window. They are described below.

# Powder Histograms - type PWDR

This is where to find information on the Tree item in GSAS-II associated with powder diffraction (labeled PWDR) and its associated subitems. GSAS-II use the label of "histogram" for datasets of any type (single-crystal, powder,...) Powder diffraction histograms are added to a project using the Import/"Powder Data" menu items. After data are read, if there are phases present, you will be offered a chance to link the imported histograms to the previously imported phase(s). Likewise, if phase(s) are imported after histograms you will also be asked to link the new phase(s) to existing histograms. It is also possible to add histograms to a phase later by selecting that phase in the data tree and then selecting the "Data" tab and finally using the "Edit Phase"/"Add powder histograms" menu command. Note that there is no limit to the number of histograms that can be included in a GSAS-II project (other than as limited by available computer memory) and histograms that are not linked to at least one phase are ignored in refinements.

When a powder diffraction dataset (prefix 'PWDR') is selected from the data tree the dataset is plotted. The observed data points are shown as blue crosses and where fit, the calculated pattern is shown as a green line; the background is shown as red line. The difference curve is shown as a cyan line. Reflection positions are shown with small vertical lines. The data window shows statistical fit information if the pattern has been used in any fitting (peak fits, Rietveld, LeBail or Pawley fitting). The “Weight factor” is a multiplier on the data point weights; normally 1.0 but could be adjusted, e.g., to provide better balance in a combined data refinement. A data “Surprise” (S) factor is also shown. It is defined here as:

$$
  S = \frac{1}{N} \left[ \sum \ln (\frac{\hat{I}^2}{(I-\hat{I})^2}) \right] - 1
$$

where the sum is over the points (N) in the profile delimited by the Limits (see below). The surprise factors thus give an indication of the excursions of the data points from their mean ( \( \hat{I} \) ) and is best viewed for a sequence of data and not between instruments or of different materials. Data with few sharp peaks will have small surprise factors while patterns with many peaks may have larger surprise factors. An increasing timed sequence of data collections will show an initial rise & then level surprise factor perhaps indicating when sufficient data has been collected. Phase changes in a temperature sequence may show as abrupt shifts in the surprise factor.

Each powder diffraction dataset has a number of children in the tree as are shown below. Clicking on any of them produces changes in the plot and allows access to different parameters associated with the dataset.

* Comments
* Limits
* Background
* Instrument Parameters
* Sample Parameters
* Peak List
* Index Peak List
* Unit Cells List
* Reflection Lists

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

Menu **Commands**

* **Error Analysis** – this produces a 'normal probability' plot for the refinement result as bounded by the limits. The slope and intercept of the curve in the central region (-1 < / < 1) are shown on the plot status line. The slope is the GOF for the best fit set of data points (~68% of the data).

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

The powder patterns that are part of your project are shown on this page. They can be displayed as a stack of powder patterns, just a single pattern or as a contour image of the peak intensities. What can be done here will depend on how many patterns are shown as well as what mode is selected. Note that the tick marks and difference curve positions can be customized, as discussed below.

Similar plots to the one here are displayed when different subtree items are selected and on those plots it is possible to view and in some cases edit information associated with the histogram. As examples:

* By selecting the Limits entry, range of data used, as well as possible excluded regions, can be set.
* Selecting Reflection Lists allows display of reflection indices (hkl values) for a selected phase. Letting the mouse rest unmoved at the position of a reflection in 2Q, TOF, Q, etc. (the vertical position does not matter) will cause these to be displayed. After a short delay a "tool tip" will appear with indices for any reflections close to the lateral mouse position.
* Selecting Background allows a mouse to be used to define fixed points where a background curve can be fitted to those points.
* Selecting Instrument Parameters displays plot of peak widths as a function of Q.
* Selecting Peak List allows positions of peaks to be defined for use in direct peak fitting.
* Selecting Unit Cells List can show the positions of reflections for an arbitrary set of unit cell parameters, optionally with space group extinctions applied.

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

* **Move mouse**: As the mouse cursor is moved across the plot, the plot status line will show the cursor position as 2Q (or TOF), d-spacing, Q and the intensity.
* **Press keyboard keys** - See below. The "s" and "w" modes are commonly used.
* **Drag tick marks** - Select any tick mark and while holding the left mouse button down, move them to where you want them to be displayed (press the s key for Sqrt(I) mode to reset to the defaults). With multiple phases, selecting the 2nd phase, etc. changes the vertical spacing between phases. Tick marks can be dragged only when the main PWDR or Reflection Lists tree items are selected.
* **Drag the difference curve** - When the "normal" obs-calc plot is shown (as opposed to the "w" mode plot where (obs-calc)/sigma is displayed, select any point in the difference curve and while holding the left mouse button down move the curve to where you want it to be displayed (press the s key for Sqrt(I) mode to reset it to the default). The difference curve can be dragged only when the main PWDR or Reflection Lists tree items are selected.
* **Display/edit histogram information** - By selecting different tree items within the current histogram, it is possible to display and, in some cases, edit information associated with the histogram. See above.
* **Create a Publication-ready plot**  - Press the green "P" button to generate a customizable version of the displayed plot that can be exported at high resolution, as discussed below.
* **Highlight reflection positions** - By selecting the "Reflection Lists" tree item and a phase, if the mouse is moved to the region of a reflection in that phase, a "tool tip" (temporarily displayed text) with the indices for nearby reflections is displayed.
* **Label reflection positions** - Right-clicking on a reflection tickmark (in the PWDR and "Reflection Lists" plots) will cause an hkl label with the indices for nearby reflection(s) to be displayed. (Dragging a tickmark with the Left mouse button allows tickmarks to be repositioned.) Once a reflection label is shown, it can be dragged to a new position with the left mouse button. Right-clicking on the label will delete it. All hkl labels can be deleted with a menu command. The hkl labels, including their positions, are saved in the GSAS-II project (.gpx) file.

The following key press characters are defined (not for all plot modes). These actions can also be initiated from the Key Press button on the plot toolbar.

## For line plots:

* **s: Sqrt(I) on/off** - changes the y-axis to be the square-root of the intensity. The tick mark and the difference curve location is reset.
* **w: toggle diff plot mode** - for the pattern selected from the data tree, this will replace the difference (obs-calc) curve with the differences divided by their standard uncertainty (esd) values [(obs-calc)/sigma], which shows the significance of the deviations in the fit of the pattern. (Recommended for proper evaluation of the differences). In this mode both plots have separate zoom control.
* **b: subtract background** - Subtracts the fitted background from the powder pattern. Pressing this again turns the mode off.
* **n: log(I) on/off** - changes the y-axis to be the log10 of the intensity; difference curve is not shown for log(I) on.
* **q: toggle Q plot** - changes the x-axis to Q. This will put multiple powder patterns taken at different wavelengths/types on the same x-axis scale.
* **t: toggle d-space plot** - changes the x-axis d-space. This will put multiple powder patterns taken at different wavelengths/types on the same x-axis scale. May not be very useful with data over a wide range.
* **e: set excluded region** - Defines a new excluded region: press the "e" key with the mouse on one side of the region. Move the mouse to the other side and press "e" again. The region markers (magenta dashed lines) can be dragged to new positions. Available only when the Limits tree entry is selected.
* **f: toggle full length reflection tick marks** - Reflection positions are indicated when the main PDWR tree entry is selected, or when the "Reflection Lists" entry is selected by display of vertical lines. These lines can be shown as tick marks, short lines or thin vertical line the full length of the plot. The 'f' key toggles between the two modes.
* **x: show excluded region** - Normally all observed data is plotted. When the "x" key is pressed, data inside excluded regions are not shown.
* **g: grid lines** - Toggle drawing vertical and horizontal grid lines at all axis label positions. Applies to all plot modes.
* **a: add magnification region** - Adds a magnification region to the plot and sets the magnification amount to x2. This can be edited (or deleted) in the table that is shown when the main PWDR tree entry is selected.
* **.: scaling diagnostic** - When the '.' key is pressed, data are plotted as intensity*weight. Normally this = 1.0 for CW data and proportional to incident spectrum for normalized neutron TOF data. Does not include effect of selected weight factor but is equal to number of detectors in multidetector data.

## For line plots with more than one powder pattern:

* **c: contour on/off** - if multiple powder profiles, then a contour plot is shown of the observed intensities. Data sets of differing length are padded/trimmed to match the 1st pattern.
* **S: set color Scheme** - Select the color map used for contour plots
* **m: toggle single/multiple plot** - In single mode, this will show only the one selected from the data tree. In multiple “waterfall” mode all are superimposed; offset options (below) can be used to shift them. The selected one is displayed as points & curve for obs/calc; others as obs lines only.
* **f: select data** - Allows a subset of the powder patterns to be plotted, rather than all.
* **+,=: no selection** - For multiple powder profiles, only the observed curve is shown when this mode is turned on ('+' and '=' do exactly the same thing).
* **/: normalize** - For multiple powder profiles, all diffraction datasets are normalized so that the maximum intensity is 1 (does not affect the data).

## Offset modes for line plots in waterfall mode (multiple patterns only):

* **l: offset left** - For a waterfall plot of multiple powder profiles, increase the offset so that later plots are shifted more to the left relative to previous plots.
* **r: offset right** - For a waterfall plot of multiple powder profiles, increase the offset to the right (or decrease the left offset.)
* **d,D: offset down** - For a waterfall plot of multiple powder profiles, increase the offset down. (D does the same as d but to a much larger amount)
* **u,U: offset up** - For a waterfall plot of multiple powder profiles, increase the offset up. (U does the same as u but to a much larger amount)
* **o: reset offset** - For a waterfall plot of multiple powder profiles, reset to no offset.

## For contour plots:

* **d: lower contour max** - This lowers the level chosen for the highest contour color.
* **D: lower contour min** - This lowers the level chosen for the lowest contour color; can be negative.
* **u: raise contour max** - This raises the level chosen for the highest contour color
* **U: lower contour min** - This lowers the level chosen for the highest contour color
* **i: interpolation method** - This changes the method used to represent the contours. If selected a dialog box appears with all the possible choices. Default is 'nearest'; the other useful choice is 'bilinear', this will smooth out the contours.
* **s: color scheme** - This changes the color scheme for the contouring. Default is 'Paired', black/ white options are 'Greys' and 'binary' (for black on white) or 'gray' (for white on black). Others can be very colorful (but not useful!)
* **c: contour off/on** -This turns off contouring and returns to a waterfall plot with any offsets applied.
* **t: temperature on/off** - Show “temperature” for y-axis; valid only if temperature is varied across data sequence and evenly spaced.
* **s: toggle sqrt(I) plot** - Show sqrt(intensity) in contour plot

## For display of reflections from magnetic unit space groups

These two key commands allow one to step through the output from k-SUBGROUPSMAG in Unit Cells List that are marked “Keep”.

* **j: show next; clear Keep flag** - Show the next magnetic space group in the list, clearing the "Keep" flag for the currently displayed space group. Use this to remove magnetic substructures from consideration that don't satisfy the reflection extinction conditions.
* **k: show next** - Show the next magnetic space group in the list. The "Keep" flag for the currently displayed space group is unchanged.

## Publication Plots

When the green "P" button is pressed, a copy of the current powder diffraction plot is presented in a separate window. This can only be done with plots of a single histogram. Not for waterfall or contour plots. The separate plot offers GUI controls to modify aspects of the plot, for example by changing colors, line widths, plot limits the contents or size of displayed text. The displayed plot, including any changes made, can be exported in a number of formats. These include a number of bitmap formats (JPEG, PNG, TIFF,...) that can then be imported into other programs; several formats offer vector graphics (Postscript, PDF, SVG), that will render at whatever resolution is desired, which can be of great value for posters or other applications where pixilation would be problematic; other formats are intended to be read into other software: Input for the Grace, Igor Pro and Origin programs is offered, as well as a generic .csv file that can be used with custom software. Note that Igor Pro and Origin are commercial products. (Origin export is only available on Windows and requires that Origin 2021 or later be installed on the computer where GSAS-II is installed. The Grace program is open-source, runs on all major computing platforms, and is available in several versions. The .csv file consists of 10 or more columns (depending on the number of phases included in the histogram). The columns are described below, noting that N is the total number of phases and if there are M data points in the histogram, will be M datapoints in each column except in the Phase, tick-pos, and Axis-limits columns.

1) Used:
:    Indicates if the data point is inside the plot limits or is excluded from the fit. A value of 1 means the values are used and 0 means the data point is not used. 

2) X:
:    The x-values from the plot in the units used in the plot (2theta, Q,...). The units are noted in the header. 

3) Obs:
:    The observed diffraction intensity. This may be modified by scaling options or background subtraction, if that has been selected for the plot. 

4) Calc:
:    The computed diffraction intensity. This will usually be zero if "Used" is 0. 

5) Bkg:
:    The computed background value at the current "X" location, This will usually be zero if "Used" is 0. 

6) Diff:
:    The plotted difference curve. This will have the offset used in the plot. 

6+i) Phase i:
:    This has the reflection positions (tickmarks) in the same units as used for "X". There will be far fewer values for this than for the previous columns. 

7+N) tick-pos:
:    The name of each phase followed by the vertical position used to display the tickmarks for each phase. There will be 2N of these values. 

8+N) diff/sigma:
:    The uncertainty-weighted difference plot [(Obs-Calc)/sigma where sigma is the statistically expected uncertainty in the obs values, i.e. the standard uncertainty values]. Note that values where "Used" is 0 are meaningless, as the Calc value is 0, but the Obs and sigma values are from the data. 

9+N) Axis-limits:
:    Has four values, x-min, x-max, y-min and y-max as used as the limits for the plot. 

## Comments

This window shows whatever comment lines (preceded by “#”) found when the powder data file was read by GSAS-II. If you are lucky, there will be useful information here (e.g. sample name, date collected, wavelength used, etc.). If not, this window will be blank. The text is read-only.

## Limits

This window shows the limits in position to be used in any fitting for this powder pattern. The 'original' values are obtained from the minimum & maximum values in the powder pattern. The 'new' values determine the range of data that will be used in fitting, Tmax and Tmin. Tmin and Tmax will be either 2θ (deg.) for CW data or time (μsec) for TOF data. You can also designate areas of the pattern that should be "excluded", meaning that they will not be included in the refinement. This should be be done when there is a well-understood reason why that region is expected to have spurious intensities (such as scattering from a furnace). For the computed pattern, shown as a green line from a fit, no computed pattern is shown for data in an excluded region.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

You can change the 'new' values for Tmin and Tmax as needed. Change the upper (Tmax) and lower (Tmin) values by clicking on the appropriate vertical line and dragging it to the right or left, or by typing values into the data window, or using the "Set lower limit" or "Set upper limit" commands in the "Edit Limits" menu and then click on a point in the pattern.

You can add an excluded region using the "Add excluded region" command in the "Edit Limits" menu and then click on a point in the pattern. This creates region at that point. Edit the region by dragging the magenta lines or by editing the values in the data window.

Menu '**Edit Limits**':

**Copy**
: This copies the limits shown for the selected pattern to other powder patterns. If used, a dialog box (Copy Parameters) will appear showing the list of available powder patterns, you can copy the limits parameters to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.

**Add excluded region**
: Select this menu item and click on a data point. A pair of magenta lines is drawn to indicate a range that should be excluded. The magenta lines can be dragged, as described below for setting data limits.

**Set lower limit**
**Set upper limit**
: These menu items are used to select a location in the pattern to set as Tmin or Tmax. After using the menu command, click on a point in the pattern at the appropriate location.

**Cancel Set**
: Resets the "Add excluded region", "Set lower limit" or "Set upper limit" command.

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

The plot is the same as for Powder Histograms - type PWDR and the key press commands are all the same. However, vertical lines: green for the lower Tmin value and red for the upper Tmin value, are displayed. Excluded regions are displayed with pairs of magenta vertical lines. All these vertical lines can be dragged to set limits/excluded regions.

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

The upper and lower Tmin values can be changed by clicking on the appropriate vertical line and dragging it to the right or left. A drag beyond the end of the pattern will reset that limit to the original value. Likewise, excluded regions can be created here and modified by dragging the lines as needed.

## Background

This window shows the choice of background functions and coefficients to be used in fitting this powder pattern. There are four types of contributions available for the background:

* A continuous empirical function ('chebyschev', 'chebyschev-1', 'cosine', 'lin interpolate', 'inv interpolate' & 'log interpolate'). The latter three select fixed points with spacing that is equal, inversely equal or equal on a log scale of the x-coordinate. The set of magnitudes at each point then comprise the background variables. All are refined when refine is selected. Note that 'chebyschev-1' is a better choice than 'chebyschev'.

* A set of Debye diffuse scattering equation terms of the form:

    $$
    B = A (sin{QR}/QR)e^{-UQ^2}
    $$

    where A,R & U are the possible variables and can be individually selected as desired; Q = 2π/d.

* A set of individual Bragg peaks using the pseudo-Voigt profile function as their shapes. Their parameters are 'pos', 'int', 'sig' & 'gam'; each can be selected for refinement. The default values for sig & gam (=0.10) are for very sharp peaks, you may adjust them accordingly to the kind of peak you are trying to fit before trying to refine them.

* Subtract an experimentally measured background scaled by a multiplier.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. Menu '**Background**' –

* **Copy** – this copies the background parameters shown to other selected powder patterns. If used, a dialog box (Copy Parameters) will appear showing the list of available powder patterns, you can copy the background parameters to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.
* **Copy flags** – this copies only the refinement flags shown to other selected powder patterns. If used, a dialog box (Copy Refinement Flags) will appear showing the list of available powder patterns, you can copy the refinement flags to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.

2. You can select a different Background function from the pulldown tab.
3. You can choose to refine/not refine the background coefficients.
4. You can select the number of background coefficients to be used (1-36). You should use the minimum required.
5. You can change individual background coefficient values. Enter the value then press Enter or click the mouse elsewhere in the Background window. This will set the new value.
6. You can introduce one or more Debye scattering terms into the background. For each one you should enter a sensible value for 'R' – an expected interatomic distance in an amorphous phase is appropriate. Select parameters to refine; usually start with the 'A' coefficients.
7. You can introduce single Bragg peaks into the background. For each you should specify at least the position. Select parameters to refine; usually start with the 'int' coefficients.
8. You can select an experimentally measured background pattern from those in the GSAS-II data tree and scale it with a multiplier.

Any modification of the background representation will be immediately applied to the calculated pattern so you can see its effect.

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

The plot is the same as for Powder Histograms - type PWDR and the key press commands are largely the same. Specific to this plot are fixed background points. These can be added, deleted and moved. Once that is done the background parameters for the selected function can be fitted to the fixed points. NB: the number of fixed points must exceed the number of background parameters to be fitted. Not recommended for fitting sharp Bragg peak backgrounds unless sufficient fixed points are selected across each Bragg peak.

## Instrument Parameters

This window shows the instrument parameters for the selected powder data set. Note that the preferred method for use of GSAS-II is that these parameters are fitted to calibration materials to develop a set of values for an instrumental configuration and these values are not refined when fitting samples. The plot window shows the corresponding resolution curves. Solid lines are for the default values (in parentheses), dashed lines from the refined values and '+' fitted widths for individual entries in the Peak List. Curves that fall below zero will generate a warning in the plot title, coefficients should be adjusted to ensure every dashed line curve is zero or above.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. Menu '**Operations**' – A single menu is provided with the selection of instrument parameters.

**Calibrate**
: performs calibration of position dependent instrument coefficients from indexed peak positions.

**Reset profile**
: resets the values for the instrument parameters to the default values shown in parentheses for each entry.

**Load profile...**
: loads a GSAS-II instrument parameter file (name.instprm), replacing the existing instrument parameter values. All refinement flags are unset.

**Save profile...**
: saves the current instrument parameter values in a simple text file (name.instprm); you will be prompted for the file name – do not change the extension. This file may be edited but heed the warning to not change the parameter names, the order of the parameter records or add new parameter records as this will invalidate the file. You may only change the numeric values if necessary. You can change or add comment records (begin with '#').

**Save all profile...**
: saves multibank histogram instrument parameters into a single instprm file. Suitable for neutron TOF instruments.

**Copy**
: this copies the instrument parameters shown to other selected powder patterns. If used, a dialog box (Copy parameters) will appear showing the list of available powder patterns, you can copy the instrument parameters to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation. The copy will only work for instrument parameters that are commensurate with the one that is shown, e.g. single radiation patterns will not be updated from Kα1α2 ones.

**Copy flags**
: this copies the instrument parameter refinement flags shown to other selected powder patterns. If used, a dialog box (Copy refinement flags) will appear showing the list of available powder patterns, you can copy the instrument parameter refinement flags to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation. The copy will only work for instrument parameters that are commensurate with the one that is shown, e.g. single radiation patterns will not be updated from Kα1α2 ones.

**Set one value**
: this is used to set a single selected instrument parameter for a selected set of PWDR histograms. The same value can be used for all histograms, or a dialog can be used to provide a table where you can set the values differently for each of selected histograms.

**Show multiple**
: Sets a mode where selected histograms matching the current selected histogram are shown in the data window.

2. You can change any of the instrument coefficients
3. You can choose to refine any instrument coefficients. NB: In certain circumstances some choices are ignored e.g. Zero is not refined during peak fitting. Also, some choices may lead to unstable refinement, e.g. Lam refinement and lattice parameter refinement. Examine the 'Covariance' display for highly correlated parameters.

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

This plot shows the contributions to the powder pattern peak widths as ΔQ/Q (=Δd/d) vs. Q for the Gaussian and Lorentzian parts of the profile function, in addition to the overall widths. The solid curves are based on the default values of U, V, W, X and Y shown in the Instrument Parameters window (shown in parentheses; these are the values for the instrument contribution that were set when the powder pattern was first read in to GSAS-II.) The dashed values are based on the refined values, if different. If individual peak fitting has been performed, the values of 'sig' & 'gam' for those peaks are plotted as '+'; these are computed from the fitted values of U, V, W, X and Y as well as any sig or gam values that are individually refined. For neutron TOF, the curves include those for the α and β coefficients. All curves must be zero or above. Negative values are not mathematically or physically possible; if encountered in fitting, the corresponding peaks may be ignored.

## Sample Parameters

This window shows the various sample-dependent parameters for the selected powder pattern. The presence of a refine button indicates that a parameter can be refined (all others are fixed.) All values shown in this window can be edited. Note that the last three parameters (named FreePrmX, X=1,2,3) have labels that can be changed. If changed in one histogram, the same label is used for all histograms. When a label is changed, the Comments tree item for each PWDR histogram is searched for a matching "Label=value" pair (differences in letter case between the two label strings is ignored). When found, the value is converted to a float and saved as the appropriate Sample Parameter. NB: for powder data, be sure the correct instrument type is selected (Debye-Scherrer or Bragg-Brentano). Also, ensure the goniometer radius is correct (in mm) so that sample displacements are properly scaled (in μm).

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

**Command** Menu items

In this window you can change parameters associated with a histogram or set them to be refined. The histogram scale factor is usually refined. For **Debye-Scherrer** mode the "Sample X displacement" is also usually refined but the "Sample Y displacement" can only be refined when data are collected over a two-theta range that extends to greater than ~90 degrees (typically for CW Neutron). Sample absorption should not be refined when all atomic displacement parameters (Uiso or Uij values) are varied, as the correlation is very high. For Bragg-Brentano, "Sample displacement" is usually refined and for low-Z samples "Sample transparency" is usually refined instead. "Surface roughness" parameters are not usually refined unless the sample has high absorption and negative Uiso obtained for heavy atoms. Remaining parameters are of use for texture or parametric studies and may be changed with the menu commands described here.

* **Set scale** - Rescales a pattern by multiplying by the current scale factor. Scale factor is then set = 1.0.
* **Load** - This loads sample parameters from a previously saved .samprm file.
* **Save** - This saves the sample parameters to a file with the extension '.samprm'. A file dialog box will appear to ask for the name of the file to be written.
* **Copy** - This copies the sample parameters shown to other selected powder patterns. If used, a dialog box (Copy parameters) will appear showing the list of available powder patterns, you can copy the sample parameters to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.
* **Copy selected...** - This copies only the sample parameter that are selected to other selected powder patterns but is otherwise similar to "Copy".
* **Copy flags** - This copies the sample parameter refinement flags shown to other selected powder patterns. If used, a dialog box (Copy refinement flags) will appear showing the list of available powder patterns, you can copy the sample parameter refinement flags to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.
* **Set one value** - This is used to set a single selected sample parameter for a selected set of PWDR histograms. The same value can be used for all histograms or a dialog can be used to provide a table where you can set the values differently for each of selected histograms.
* **Load all** - Reads a file containing a table of sample parameters and copies them to matching PWDR entries. The file will look something like the example here:

```
    #filename       temperature pressure ignore-me  humidity
    LaB6_dc250.tif      100          1      test       .2
    LaB6_dc300.tif      150          1      test       .25 
```

Note that the first line(s) in the file can be a header, but each header line must start marked with a hash (#). A header is not required. "Columns" in the table are separated by one or more delimiters (which may be a comma, tab or space). Note that columns do not need to be aligned, as long as each entry is spaced by at least one delimiter. The first column in the table is used to look up PWDR entries where the initial space-delimited string after the PWDR tag ("myfile" in "PWRD myfile AZM=180...") must match the table. Subsequent columns can then be mapped to sample parameters or can be ignored, using a dialog window.

* **Rescale all** - Allows a series of selected PWDR histograms to be put on a common scale by integrating them over a specific two-theta region and then scaling them so that the integration range will match the first pattern.

## Peak List

The Peak List data tree entry is used to fit diffraction peaks at user-supplied positions (not generated from a unit cell). Peak positions and intensities may be selected for individual refinement. Gaussian (sigma2) and Lorentzian (gamma) peak widths may be varied individually or the values may be generated from the the appropriate profile terms in the Instrument Parameters tree item (U, V & W for sigma2; X & Y for gamma): Note that the Gaussian full-width at half-maximum is given by FWHM = (8 * ln2 * sigma2)0.5 while gamma is the Lorentzian FWHM. The ''sigma2'' values (peak variances) are in units of centidegrees2 (centidegrees are degrees*100) for CW data or microseconds for TOF data.

If individual sigma<sup>2</sup> or gamma values are refined, then those value(s) in the table are used as the refinement starting point. If values are not refined, then normally the unvaried widths are determined from the appropriate Instrument Parameters profile terms and are placed in the table prior to fitting. This behavior can be overridden by changing the "Gen unvaried widths" mode entry in the menu (see below) so that fixed values can be specified.

For peak fitting, the background is generated using the parameters in the Background data tree entry. Also, the range of data used in the fit is set from the Limits tree item. In both cases these are the same values that are used in Rietveld fits. Note that optionally the parameters on the Background and in the Instrument Parameters tree items may be refined during peak fitting.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

There are three ways to interact with Peak List data tree item: through its menu, labeled Peak Fitting, through interaction with the peak list table, and through interactions with the plot.

The following interactions are available with the peak table:

* You can change individual peak coefficient values. Enter the value then press Enter or Tab or click the mouse elsewhere in the Peak List window. This will set the new value.
* You can change the individual refine flags by clicking on the individual check boxes.
* You can change all refine flags in a column by clicking on a single flag and then click on the column label above. (The entire column should then be highlighted in blue.) Type 'y' to set the refine flags or 'n' to clear the flags. You can also change flags for an entire column by double-clicking on the column label, which brings up a menu where "Y" or "N" can be selected.
* You can delete peaks in the Peak List by selecting a row by clicking on the row label to the left (multiple selection of rows is allowed). Selected rows will be highlighted in the plot (see below). Then press the Delete or backspace key. (Note that peaks can also be deleted from the plot, see below.)
* You can highlight a peak in the plot by double-clicking on the row label (to the left) for a peak.
* Pressing "d" in the plot window causes the next peak in the table (or the first if none are selected) to be selected and causes that peak to be highlighted in the plot; pressing "u" causes the previous peak in the list to be highlighted. 

The **Peak Fitting** menu contains the following commands:

* **Set sel. ref flags** - If one or more rows of peaks are selected by clicking on the peak label to the left, this menu item can be used to set the refinement flags for the selected reflections.
* **Set all ref flags** - This sets refinement flags for all peaks in the table.
* **Auto search** - This fills the table with peak positions. These are selected based on peak tops that are substantially above background. Noisy data will give spurious peaks, and small peaks or shoulders will necessarily not be found. Examine results & modify as needed.
* **UnDo** - Resets peak parameters, background and instrument parameter values varied in the last peak fitting refinement back to their original values. Use this to recover from a failed refinement. Note: only one previous refinement is saved, so this cannot be pressed twice to return to the refinement before the previous.
* **PeakFit** - Performs a least squares fit of the peaks in Peak List to the data. Any peak parameters, background parameters and instrument parameters with refine checked will be varied in this refinement. The refinement will proceed until convergence. We suggest you vary the intensity along with the background first (the default), then vary the position and instrument parameters after. The order will depend on how poor is the initial estimate of the instrument parameters (U, V, W, X, Y & SH/L). To determine how to proceed, examine in detail the powder pattern difference curve displayed in the GSASII Plots window. If individual peaks show peak widths that are widely different, their individual sigma and gamma parameters may be refined. If the refinement results in negative peak coefficients, these will be highlighted in red. If this happens, you should use the UnDo menu item (above) to return to the refinement and reconsider your choice of parameters to be varied.
* **Peakfit one cycle** - Perform a single cycle of least squares refinement. This can be used in difficult cases to get a refinement started toward convergence.
* **Reset sig and gam** - This resets the values of sigma and gamma in the table to those computed from the instrument parameters U, V, W, X & Y.
* **Peak copy** - Copy the current set of peaks to other histogram(s)
* **Seq PeakFit** - Fit peaks for multiple histograms; results will be in Sequential peak fit results.
* **Clear peaks** - This removes all the peaks from the Peak List.
* **Move selected peak** - A peak may be moved using the following process: select it in the table by clicking on its label (to left), use this menu item. The peak line will then follow movement of the mouse in the plot window. Click with the left mouse button to set a new position. Click with the right mouse button to delete that peak. Click outside the axes to abort the move and return to the previous position. (Note that peak movement is also possible with the plot window, see below.)
* **Gen unvaried widths** - This determines how sigma and gamma values are treated when unvaried. When this item is checked (the default mode), unvaried Gaussian (sigma) and Lorentzian (gamma) peak widths will be generated from the the appropriate profile terms in the Instrument Parameters tree item (U, V & W for sigma; X & Y for gamma). This allows those Instrument Parameters to be refined. If this mode is changed and the "Gen unvaried widths" mode is unchecked the the sigma and gamma peak widths are used as supplied, but then it is not possible to refine Instrument Parameters. This mode will not affect sigma and gamma values that have their refine flag checked.

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

The plot is the same as for Powder Histograms - type PWDR and the key press commands are largely the same. The plot window shows the observed and computed patterns, as well as the background and peak positions. Observed points are shown as blue crosses (+) and the fitted pattern is shown as a solid green line. The background is shown as a red line and the difference curve is shown as a cyan (turquoise) line, below the observed and computed pattern. Specific to this plot are the peak positions that are shown as vertical dashed blue lines. To show that a peak is selected, it is highlighted in yellow and the blue line is made wider. The upper and lower data limits are shown as red and green dashed vertical lines, respectively.

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

For all actions involving mouse clicks such as those below, be sure that the Zoom/Pan buttons are not selected on the Plot window, as the mouse will be used for zooming or panning, not the desired action.

* You can add peaks to the Peak list using the mouse on the plot by: position the cursor pointer onto a cross for an observed point and pressing the left mouse button. The selected peak will be added to the Peak List in the appropriate position to keep peaks sorted and a blue vertical line will be plotted on that position. We recommend that you begin picking peaks from the right side of the pattern; that way the tool tip won't be in your way as you select peaks.
* You can delete peaks using the mouse on the plot by positioning the pointer on the blue line for the peak to be deleted and then pressing the right mouse button. The blue line should vanish, and the corresponding peak will be removed from the Peak List.
* You can move a Peak List item using the mouse on the plot by: position the pointer on the blue line for the peak you wish to move and then hold the left mouse button down, dragging the line to the desired position. When the mouse button is released, the peak line will be drawn in the new position.
* The fit limits can be changed from the plot either here or in the Limits data tree. Change the upper and lower Tmin/Tmax values by clicking on the appropriate vertical line and dragging it to the right or left.
* Highlight each peak in the list successively using the "d" keyboard key to move down the list or "u" to move up the list. 

## Index Peak List

This window shows the list of peaks that will be used for indexing (see Unit Cells List). It must be filled with peaks from the Peak List (using the Operations‑>Load/Reload menu command) before indexing can proceed. When indexing is completed, this display will show the resulting hkl values for every indexed reflection along with the calculated d-spacing ('d-calc') for the selected unit cell in Unit Cells List. .

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

* Menu command **Operations‑>Load/Reload** – loads the peak positions & intensities from the Peak List to make them available for the indexing routine. The d-obs value is obtained from Bragg's Law after applying the Zero correction shown on the Instrument Parameters table to the position shown here.
* Menu command **Operations‑>Save** – saves a csv version of this table.
* Menu command **Operations‑>Export to PreDict** – saves the table in a format that can be used by PreDict, an updated version of the DICVOL program.
* Menu command **Operations‑>Refine Cell** – optimizes the unit cell parameters shown at the bottom of the window to best-fit the peak list.
* Double-clicking on a row of the table causes that row to be selected and causes that peak to be highlighted in the plot.
* Pressing "d" in the plot window causes the next peak in the table (or the first if none are selected) to be selected and causes that peak to be highlighted in the plot; pressing "u" causes the previous peak in the list to be highlighted.
* You may designate that individual peaks not be used in the indexing by process by unchecking the corresponding "use" box. 

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

The plot is the same as for Powder Histograms - type PWDR and the key press commands are largely the same. The plot window shows the observed and computed patterns, as well as the background and peak positions. Observed points are shown as blue crosses (+) and the fitted pattern is shown as a solid green line. The background is shown as a red line and the difference curve is shown as a cyan (turquoise) line, below the observed and computed pattern. Specific to this plot are the peak positions that are shown as vertical solid blue lines. To show that a peak is selected, it is highlighted in yellow and, if "use" is selected, the blue line is made wider. The upper and lower data limits are shown as red and green dashed vertical lines, respectively.

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

* Highlight each peak in the list successively using the "d" or "u" keyboard keys. 

## Unit Cells List

This tree item has several purposes, it can be used to perform autoindexing and it can be used to show the positions of peaks from unit cells which may be results from autoindexing or may be entered from a phase or manually. It can be used to refine unit cell parameters. It can also be used to search for cells/symmetry settings related to a specified unit cell & space group.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

The actions that can be performed with this tree item are:

1. Autoindexing
2. Visualizing reflection positions
3. Symmetry exploration
4. Cell fitting

**For autoindexing**, the peaks in the Index Peak List are used. Select one or more Bravais lattice types to use and use the "Cell Index/Refine"/"Index Cell" menu command to start indexing. Output will appear on the console and a progress bar dialog will appear which tracks trial volume. A Cancel button will terminate indexing for the Bravais lattice being searched; one may need to press it more than once to fully terminate the indexing process. Console output shows possible solutions with a computed **M20** for each; good solutions are indicated by high **M20** values. **X20** gives number of unindexed lines out of the 1st 20 lines and Nc gives total number of reflections generated for each solution.

The "Copy Cell" menu command copies a selected solution to the Unit cell values; the Bravais lattice shown for the choice is copied. Press **Show hkl positions** to generate the allowed reflection positions, which are visually superimposed on the displayed powder pattern to visually confirm the indexing. Pay particular attention to any unmatched peaks in the pattern. A **Space group** can be selected from the pulldown box to remove reflections based on space group extinctions and visually eliminate possibilities. The **Try All?** button tests all compatible space groups from the pull down against the peak set. The results are displayed and one can select the “best” one based on the listed criterion.

* **Max Nc/Nobs**: – this controls the extent of the search for the correct indexing. This may need to be increased if an indexing trial terminates too quickly. It rarely needs to be changed.
* **Start Volume**: – this sets an initial unit cell volume for the indexing. It rarely needs to be changed.
* Select "**try**" in the table to display the reflection positions the selected unit cell/space group (as described below).
* Select "**keep**" in the table for a cell that should be preserved when an additional indexing run is tried; all without that are erased before the indexing trial begins.

**To display a unit cell**, possibly with space group extinctions, enter the unit cell here. Optionally enter space group information here as well. The values can be typed into the appropriate boxes (note that the Bravais class determines which cell parameters are available) or use the "Cell Index/Refine"/"Load Phase" menu command to read this information from a phase that has been read into a project or from a file (such as a CIF) using the "Cell Index/Refine"/"Import Cell" menu command. Note that the values in the unit cell parameter boxes can be specified as Python equations, thus entering "*2" after a value will double it and "/2" will divide it by two.

To change the displayed extinctions, first set a Bravais class, which determines the unit cell type (see list below), and then optionally select a space group (by default the highest symmetry space group for the class is selected). As any change is made to the unit cell values or the symmetry, the display of reflection positions shown in the plot window is immediately updated. The "Show hkl positions" button also forces an update of the plot, but this is normally not needed.

Reflection positions are displayed as dashed vertical lines. Reflections will normally be shown as orange, but green lines are used instead in 3+1 superspace groups for reflections with non-zero components in the fourth dimension ("superlattice lines"). If the "Show extinct" option is selected, then reflections that are generated by the unit cell, but must be zero in intensity due to the selected space group are shown with blue dashed lines. This slows computations somewhat. Note that the speed of reflection display is determined by the number of reflections that are computed, so reducing the range of data used by changing the diffraction Limits will speed the refresh of the display when values/symmetry is changed.

The reflection indices (hkl values) can be displayed by moving the mouse cursor over a reflection line and waiting ("hovering"). After a short delay, the indices for all nearby reflections are shown temporarily as a "tool tip". If multiple reflections are closely spaced, the reflection indices will be listed in the order that reflections occur, but extinct reflections are shown after non-extinct. Also, if multiple extinct reflections occur at the same location, only the first of them is used.

**For symmetry exploration**, once a phase/cell has been loaded, the following commands in available in the "Cell Index/Refine" menu to explore related unit cells and space groups. Use the:

* "Run SUBGROUPS" menu item to generate lower symmetry space groups for the loaded phase;
* "Cell Symmetry Search" menu item to find higher symmetry unit cells equivalent to the current cell.
* "Run k-SUBGROUPSMAG" menu item to find magnetic subgroups (with neutron data) commands from the
* "Transform Cell" command in that menu can perform many common lattice transformations, apply a user-supplied cell transformation or create a magnetic phase.

Note that "Run SUBGROUPS", "Cell Symmetry Search" and "Run k-SUBGROUPSMAG" access the Bilbao Crystallographic Server [for use please cite: Bilbao Crystallographic Server I: Databases and crystallographic computing programs, M. I. Aroyo, J. M. Perez-Mato, C. Capillas, E. Kroumova, S. Ivantchev, G. Madariaga, A. Kirov & H. Wondratschek Z. Krist. 221, 1, 15-27 (2006)  and Determining magnetic structures in GSAS-II using the Bilbao Crystallographic Server tool k-SUBGROUPSMAG, R.B. Von Dreele & L. Elcoro, Acta Cryst. B80, x-x (2024).]

**To optimize a cell** to fit the indexed peaks in the Index Peak List, use the "Cell Index/Refine"/"Refine Cell" menu command. The results will be placed in the Indexing Result table with 'use' selected.

**Other**: The "Make new phase" command creates a new phase from the selected unit cell and chosen space group. A dialog box will appear asking for a name for this phase. See the new entry under Phases and the new lattice parameters will be in the General window for that phase.

GSAS-II offers space groups in the following Laue classes (note that some redundant choices are included for convenience):

**GSAS-II Laue classes**

* Cubic: Fm3m, Im3m & Pm3m
* Rhombohedral: R3-H (hexagonal axes)
* Hexagonal: P6/mmm
* Tetragonal: I4/mmm, P4/mmm
* Orthorhombic: Fmmm, Immm, Ammm, Bmmm, Cmmm, Pmmm
* Monoclinic: I2/m, A2/m, C2/m, P2/m (b-unique)
* Triclinic: P1, C1

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

The fit limits can be changed from the plot either here or in the Limits data tree. Change the upper and lower Tmin values by clicking on the appropriate vertical line and dragging it to the right or left. Reducing the maximum Q value (TOF min or 2θ max) can greatly speed the time needed to compute reflections from a unit cell.

## Reflection Lists

This window shows the reflections for the selected phase (selected by the tab at top) found in this powder data set. It is generated by a Rietveld (including Pawley and LeBail) refinement. Reflection d-spaces are generated directly from lattice parameters but 2Q (or TOF) values will incorporate corrections, such as for sample displacement, zero, etc. The values of various correction factors, I100, size and mustrain terms for each are also shown.

The powder diffraction reflection list shows the reflection widths, accounting for instrumental as well as sample effects (the latter can be anisotropic), where the columns labeled as "sig2" and "gam" show the Gaussian and Lorentzian components for the width. The "sig2" value is the variance of the Gaussian contribution to the peak (sigma\*\*2), while "gam" is the full-width at half maximum (FWHM) for the Lorentzian component. Note that the Gaussian FWHM is given by FWHM = Sqrt(8 \* ln2 \* sigma\*\*2). For CW data, both "sig" and "gam" have units of degrees*100 (centidegrees) For TOF data, both are in microseconds.

#<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. The indices (hkl values) for reflections can be displayed by letting the mouse rest at the position of a reflection in 2Q, Q, etc. in the PWDR plot (the vertical position does not matter) for reflections in the phase selected as a tab in the data window. A "tool tip" with the reflection indices will be displayed for any reflections close to the lateral mouse position.

2. Menu '**Reflection List**' – some items are more useful for SHKL (single crystal) histograms.

    * **Select phase** – if there is more than one phase; you can select another phase; the window title will show which phase is shown. You can also simply select the tab for the desired phase.
    * **Plot 1D HKLs** – shows a stick diagram scaled to Fc2 for the reflection for the selected phase
    * **Plot HKLs** – shows a HKL layer with rings scaled to F or F2 for Fo and Fc. +/- steps through the layers and h,k or l selects the orientation – see K box for all the possible commands.
    * **Plot 3D HKLs** – shows a 3D representation of the unique part reciprocal space points for this phase. The save as/key item in the plot status bar shows the various commands for modifying this plot.
    * **Wilson statistics** – displays a Wilson plot for the intensities.
    * **Show/hide extinct reflections** – can exclude space group extinctions from the list (not valid for PWDR data).
