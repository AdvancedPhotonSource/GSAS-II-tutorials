<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="PWDR_parent"></a>
<a name="PWDR"></a>
#  **PWDR** parent data tree (Powder Diffraction)

When a powder diffraction dataset (prefix 'PWDR') is selected from the data tree or for most of the subdata tree items, the dataset is plotted. The observed data points are shown as blue crosses and where fit, the calculated pattern is shown as a green line; the background is shown as red line. The difference curve is shown as a cyan line. These colors can be changed through [configuration variables](./others.md#config) `Obs_color`, `Calc_color`, `Diff_color`, and `Bkg_color`.

Reflection positions are shown with small vertical lines. The data window shows statistical fit information if the pattern has been used in any fitting (peak fits, Rietveld, LeBail or Pawley fitting). The “Weight factor” is a multiplier on the data point weights; normally 1.0 but could be adjusted, e.g., to provide better balance in a combined data refinement. A data “Surprise” (S) factor is also shown. It is defined here as:

$$
  S = \frac{1}{N} \left[ \sum \ln (\frac{\hat{I}^2}{(I-\hat{I})^2}) \right] - 1
$$

where the sum is over the points (N) in the profile delimited by the Limits (see below). The surprise factors thus give an indication of the excursions of the data points from their mean ( \( \hat{I} \) ) and is best viewed for a sequence of data and not between instruments or of different materials. Data with few sharp peaks will have small surprise factors while patterns with many peaks may have larger surprise factors. An increasing timed sequence of data collections will show an initial rise & then level surprise factor perhaps indicating when sufficient data has been collected. Phase changes in a temperature sequence may show as abrupt shifts in the surprise factor.


<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

#### "**Commands**" Menu Commands

* **Error Analysis** – this produces a 'normal probability' plot for the refinement result as bounded by the limits. The slope and intercept of the curve in the central region (-1 < / < 1) are shown on the plot status line. The slope is the GOF for the best fit set of data points (~68% of the data).

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

The powder patterns that are part of your project are shown on this page. They can be displayed as a stack of powder patterns, just a single pattern or as a contour image of the peak intensities. What can be done here will depend on how many patterns are shown as well as what mode is selected. Note that the tick marks and difference curve positions can be customized, as discussed below.


<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

<a name="PWDR_plot_actions"></a>
<a name="PWDR_dragticks"></a>
#### For all plots

* **Move mouse**: As the mouse cursor is moved across the plot, the plot status line will show the cursor position as \(2\theta\) (or TOF), d-spacing, Q and the intensity.
* **Press keyboard keys** - See below. The "s" and "w" modes are commonly used.
* **Drag tick marks** - Select any tick mark and while holding the left mouse button down, move them to where you want them to be displayed (press the s key for Sqrt(I) mode to reset to the defaults). With multiple phases, selecting the 2nd phase, etc. changes the vertical spacing between phases. Tick marks can be dragged only when the main PWDR or Reflection Lists tree items are selected.
* **Drag the difference curve** - When the "normal" obs-calc plot is shown (as opposed to the "w" mode plot where (obs-calc)/sigma is displayed, select any point in the difference curve and while holding the left mouse button down move the curve to where you want it to be displayed (press the s key for Sqrt(I) mode to reset it to the default). The difference curve can be dragged only when the main PWDR or Reflection Lists tree items are selected.
* **Display/edit histogram information** - By selecting different tree items within the current histogram, it is possible to display and, in some cases, edit information associated with the histogram. See above.
* **Create a Publication-ready plot**  - Press the green "P" button to generate a customizable version of the displayed plot that can be exported at high resolution, [as discussed below](#PWDR_publication).
* **Highlight reflection positions** - By selecting the "Reflection Lists" tree item and a phase, if the mouse is moved to the region of a reflection in that phase, a "tool tip" (temporarily displayed text) with the indices for nearby reflections is displayed.
* **Label reflection positions** - Right-clicking on a reflection tickmark (in the PWDR and "Reflection Lists" plots) will cause an hkl label with the indices for nearby reflection(s) to be displayed. Once a reflection label is shown, it can be dragged to a new position vertically with the left mouse button. Right-clicking on the label will delete it. All hkl labels can be deleted with a menu command. The hkl labels, including their positions, are saved in the GSAS-II project (.gpx) file.

The following key press characters have defined actions. These actions can also be initiated from the Key Press button on the plot toolbar. Not all actions are available for all PWDR subdata tree items.

<a name="PWDR_keylist"></a>
#### For line plots

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

#### For line plots with more than one powder pattern

* **c: contour on/off** - if multiple powder profiles, then a contour plot is shown of the observed intensities. Data sets of differing length are padded/trimmed to match the 1st pattern.
* **S: set color Scheme** - Select the color map used for contour plots
* **m: toggle single/multiple plot** - In single mode, this will show only the one selected from the data tree. In multiple “waterfall” mode all are superimposed; offset options (below) can be used to shift them. The selected one is displayed as points & curve for obs/calc; others as obs lines only.
* **f: select data** - Allows a subset of the powder patterns to be plotted, rather than all.
* **+,=: no selection** - For multiple powder profiles, only the observed curve is shown when this mode is turned on ('+' and '=' do exactly the same thing).
* **/: normalize** - For multiple powder profiles, all diffraction datasets are normalized so that the maximum intensity is 1 (does not affect the data).

#### Offset modes for line plots in waterfall mode (multiple patterns only)

* **l: offset left** - For a waterfall plot of multiple powder profiles, increase the offset so that later plots are shifted more to the left relative to previous plots.
* **r: offset right** - For a waterfall plot of multiple powder profiles, increase the offset to the right (or decrease the left offset.)
* **d,D: offset down** - For a waterfall plot of multiple powder profiles, increase the offset down. (D does the same as d but to a much larger amount)
* **u,U: offset up** - For a waterfall plot of multiple powder profiles, increase the offset up. (U does the same as u but to a much larger amount)
* **o: reset offset** - For a waterfall plot of multiple powder profiles, reset to no offset.

#### For contour plots

* **d: lower contour max** - This lowers the level chosen for the highest contour color.
* **D: lower contour min** - This lowers the level chosen for the lowest contour color; can be negative.
* **u: raise contour max** - This raises the level chosen for the highest contour color
* **U: lower contour min** - This lowers the level chosen for the highest contour color
* **i: interpolation method** - This changes the method used to represent the contours. If selected a dialog box appears with all the possible choices. Default is 'nearest'; the other useful choice is 'bilinear', this will smooth out the contours.
* **s: color scheme** - This changes the color scheme for the contouring. Default is 'Paired', black/ white options are 'Greys' and 'binary' (for black on white) or 'gray' (for white on black). Others can be very colorful (but not useful!)
* **c: contour off/on** -This turns off contouring and returns to a waterfall plot with any offsets applied.
* **t: temperature on/off** - Show “temperature” for y-axis; valid only if temperature is varied across data sequence and evenly spaced.
* **s: toggle sqrt(I) plot** - Show sqrt(intensity) in contour plot

#### For display of reflections from magnetic unit space groups

These two key commands allow one to step through the output from k-SUBGROUPSMAG in Unit Cells List that are marked “Keep”.

* **j: show next; clear Keep flag** - Show the next magnetic space group in the list, clearing the "Keep" flag for the currently displayed space group. Use this to remove magnetic substructures from consideration that don't satisfy the reflection extinction conditions.
* **k: show next** - Show the next magnetic space group in the list. The "Keep" flag for the currently displayed space group is unchanged.

<a name="PWDR_publication"></a>
<a name="PublicationPlots"></a>
### Publication Plots

When the green "P" button is pressed, a copy of the current powder diffraction plot is presented in a separate window. This can only be done with plots of a single histogram. Not for waterfall or contour plots. The separate plot offers GUI controls to modify aspects of the plot, for example by changing colors, line widths, plot limits the contents or size of displayed text. The displayed plot, including any changes made, can be exported in a number of formats. These include a number of bitmap formats (JPEG, PNG, TIFF,...) that can then be imported into other programs; several formats offer vector graphics (Postscript, PDF, SVG), that will render at whatever resolution is desired, which can be of great value for posters or other applications where pixilation would be problematic; other formats are intended to be read into other software: Input for the Grace, Igor Pro and Origin programs is offered, as well as a generic .csv file that can be used with custom software. Note that Igor Pro and Origin are commercial products. (Origin export is only available on Windows and requires that Origin 2021 or later be installed on the computer where GSAS-II is installed.) The Grace program is open-source, runs on all major computing platforms, and is available in several versions. 

**The `.csv` file** consists of 10 or more columns (depending on the number of phases included in the histogram). The columns are described below, noting that N is the total number of phases and if there are M data points in the histogram, will be M datapoints in each column except in the Phase, tick-pos, and Axis-limits columns.

   1) Used: Indicates if the data point is inside the plot limits or is excluded from the fit. A value of 1 means the values are used and 0 means the data point is not used. 

  2) X: The x-values from the plot in the units used in the plot (2theta, Q,...). The units are noted in the header. 

  3) Obs: The observed diffraction intensity. This may be modified by scaling options or background subtraction, if that has been selected for the plot. 

  4) Calc: The computed diffraction intensity. This will usually be zero if "Used" is 0. 

  5) Bkg: The computed background value at the current "X" location, This will usually be zero if "Used" is 0. 

  6) Diff: The plotted difference curve. This will have the offset used in the plot. 

  6+i) Phase i: This has the reflection positions (tickmarks) in the same units as used for "X". There will be far fewer values for this than for the previous columns. 

  7+N) tick-pos: The name of each phase followed by the vertical position used to display the tickmarks for each phase. There will be 2N of these values. 

8+N) diff/sigma: The uncertainty-weighted difference plot [(Obs-Calc)/sigma where sigma is the statistically expected uncertainty in the obs values, i.e. the standard uncertainty values]. Note that values where "Used" is 0 are meaningless, as the Calc value is 0, but the Obs and sigma values are from the data. 

9+N) Axis-limits: Has four values, x-min, x-max, y-min and y-max as used as the limits for the plot. 
