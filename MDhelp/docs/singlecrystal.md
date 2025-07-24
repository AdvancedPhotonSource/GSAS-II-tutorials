<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="HKLF"></a>
#  Type **HKLF** data tree entries:  Single Crystal

Single-crystal datasets are read into GSAS-II using the Import/Structure Factor menu command, since the histogram is a table of structure factors. Note that GSAS-II can fit [a structure (phase entry)](./phaseoverview.md) to a one single crystal histogram, but it is also possible to fit a phase to multiple single-crystal histograms (which might be collected at different wavelengths) or even a combination of single-crystal and powder datasets (as might be the case with a laboratory single-crystal measurement combined with a neutron powder diffraction histogram.)

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

You can change the weight factor. This is a multiplier on all of the reflection weights in this histogram. Rarely needs to be changed. Use of 1 for all datasets provides optimal statistical weighting, unless there is systematic error present. 

### Menu Commands

* **Error Analysis** - this produces a 'normal probability' plot for the refinement result as bounded by the limits. The slope and intercept of the curve in the central region (-1 < / < 1) are shown on the plot status line. The slope is the GOF for the best fit set of data points (~68% of the data).
* **Merge HKLs** - this combines equivalent/duplicate reflections according to space group and some options to make a unique and averaged set of structure factors.
* **Plot 1D HKLs** - shows a stick diagram scaled to \(\rm F_c^2\) for the reflection for the selected phase
* **Plot HKLs** (the default plot) - shows a HKL layer with rings scaled to \(\rm F\) or \(\rm F^2\) for \(\rm F_o\) and \(\rm F_c\). 
: * +/- steps through the layers 
: * h,k or l selects the orientation 
: * see K box for all the possible commands.
* **Plot 3D HKLs** - shows a 3D representation of the unique part reciprocal space points for this phase. The save as/key item in the plot status bar shows the various commands for modifying this plot.

<a name="HKLF_Instrument_Parameters"></a>
## Instrument Parameters

This window shows the histogram type (SXC or SNC, for x-ray and neutron, respectively) and the wavelength. You may change the wavelength or radiation type but rarely will need to do so.

<a name="HKLF_Reflection_List"></a>
## Reflection List

This window shows the reflections for this single crystal data set.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

* Menu '**Reflection List**' – some items are useful for SHKL (single crystal) histograms.
    * **Select phase** – if there is more than one phase; you can select another phase; the window title will show which phase is shown. You can also simply select the tab for the desired phase.
    * **Plot 1D HKLs** – shows a stick diagram scaled to \(\rm F_c^2\) for the reflection for the selected phase
    * **Plot HKLs** (the default plot)– shows a HKL layer with rings scaled to \(\rm F\)  or \(\rm F^2\) for \(\rm F_o\) and \(\rm F_c\). 
      : * +/- steps through the layers
      : * h,k or l selects the orientation
      : * see K box for all the possible commands.
    * **Plot 3D HKLs** – shows a 3D representation of the unique part reciprocal space points for this phase. The save as/key item in the plot status bar shows the various commands for modifying this plot.
    * **Wilson statistics** – displays a Wilson plot for the intensities.
    * **Show/hide extinct reflections** – can exclude space group extinctions from the list

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

By default, the plot will show a l=0 layer of reflections on a square grid as rings proportional to \(\rm F_o\) (blue), \(\rm F_c\) (green) and a central dot (green or red) proportional to \(\rm (F_o -  F_c)\).

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

The "K" box in the plot controls shows the 14 keystroke controls for the plot – they are generally self-explanatory.
