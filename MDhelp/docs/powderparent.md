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

The powder patterns that are part of your project are shown in the graphics window. 
They can be displayed as a stack of powder patterns, just a single pattern, or as a contour image of the peak intensities, or be plotted individually. 
What can be done here will depend on how many patterns are shown as well as what mode is selected. Note that the tick marks and difference curve positions can be customized, as discussed below.

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

There are a huge number of options that can be used with the plot to change different aspects of how pattern(s) are plotted. The controls are largely the same for graphics associated with the main PWDR Powder Histograms tree entry and
most subtree entries. See the [overview](./powder.md) section for the [plot actions](./powder.md#PWDR_plot_actions) and [key press commands](./powder.md#PWDR_keylist). 
