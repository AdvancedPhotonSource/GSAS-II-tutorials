<!--- Don't change the HTML version of this file; edit the .md version -->

<a name="PWDR_Sample_Parameters"></a>
#  PWDR **Sample Parameters** subdata tree item (Powder Diffraction)

This window shows the various sample-dependent parameters for the selected powder pattern. Some are related to the measurement conditions, such as diffractometer setting angles, or the data collection temperature. Others, such as the histogram scale factor, adjust the fit to match the collected data. 
The presence of a refine button indicates that a parameter can be refined (all others are fixed.) All values shown in this window can be edited. 

Note that the last three parameters (named internally as `FreePrm`*X*, *X*=1,2,3), which are labeled by default as "Sample humidity", "Sample Voltage" and "Applied Load" are fields where the labels that can be changed. If changed in one histogram, the same label is used for all histograms. Thus, a minimum of three parametric variables are available in addition to temperature, pressure and time. Also, note when a label `FreePrm` is changed, the Comments tree item for each PWDR histogram is searched for a matching "Label=value" pair (differences in letter case between the two label strings is ignored). When found, the value is converted to a float and saved as the appropriate Sample Parameter. 

Be sure the correct instrument type is selected (Debye-Scherrer or Bragg-Brentano). Also, ensure the goniometer radius is correct (in mm) so that sample displacements are properly scaled (in μm).

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

In this window you can change parameters associated with a histogram or set them to be refined. 

* The histogram scale factor is usually refined. 
* For **Debye-Scherrer** mode the "**Sample X displacement**" is also usually refined but the "**Sample Y displacement**" *can only be refined when data are collected over a two-theta range that extends to much greater than 90 degrees* (typically for CW Neutron).
Note that while in the past it was common to vary the \(2\theta_0\) (**Zero**) [Instrument Parameter](./powderinst.md), the "Sample X displacement" is almost always a much better parameter to fit.  "Sample X displacement" should never be refined with Zero, with the possible exception of a calibrant where the lattice parameters are fixed.

* For **Bragg-Brentano** mode the "**Sample displacement**" is the displacement of the sample from the diffractometer circle in \(\mu\)m. This almost always refined. The \(2\theta_0\) (**Zero**) [Instrument Parameter](./powderinst.md) is almost never refined with Bragg-Brentano data. For low-Z samples "**Sample transparency**" is usually refined instead of "**Sample displacement**". Only if data are collected over a very wide \(2\theta\) range should both be refined together. 

* Sample absorption should not be refined when all atomic displacement parameters (Uiso or Uij values) are varied, as the correlation is very high. 
* "Surface roughness" parameters are not usually refined, unless the sample has high absorption and negative Uiso values are obtained for heavy atoms. 

The remaining parameters are non-refinable and may be needed for texture or parametric studies. They may be edited in the window or may be changed for all histograms with the menu commands described below.

### "**Command**" Menu Commands

* **Set scale** - Rescales a pattern by multiplying by the current scale factor. Scale factor is then set = 1.0.
* **Load** - This loads sample parameters from a previously saved `.samprm` file.
* **Save** - This saves the sample parameters to a file with the extension `.samprm`. A file dialog box will appear to ask for the name of the file to be written.
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

