<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="REFD"></a>
#  Type **REFD** data tree entries: Reflectometry Data

## Comments

This window shows whatever comment lines found above the QIE table when the reflectometry data file was read by GSAS-II. If you are lucky, there will be useful information here (e.g. sample name, date collected, wavelength used, etc.). If not, this window will be blank. The text is read-only.

<a name="REFD_Limits"></a>
## Limits

This window shows the limits in position to be used in any fitting for this reflectivity pattern. The 'original' values are obtained from the minimum & maximum values in the reflectivity pattern. The 'new' values determine the range of data that will be used in fitting. Units are Q(Å-1) for CW data.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

You can change the "new" values for Tmin and Tmax as needed. Change the upper and lower Tmin values by clicking on the appropriate vertical line and dragging it to the right or left or by typing values into the data window.

Menu '**Edit Limits**'

* **Copy** - this copies the limits shown to other selected powder patterns. If used, a dialog box (Copy Parameters) will appear showing the list of available powder patterns, you can copy the limits parameters to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.

<a name="REFD_Instrument_Parameters"></a>
## Instrument Parameters

This window shows the relevant instrument parameter for reflectivity data; namely a wavelength needed to properly calculate resonant scattering factors for x-rays or neutrons for the substances used in the reflectometry sample. It is not refinable.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. Menu '**Operations**' –

* **Copy** – this copies the wavelength shown to other selected reflectivity data. If used, a dialog box (Copy parameters) will appear showing the list of available reflectivity data, you can copy the wavelength to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.

2. You can change the wavelength.

<a name="REFD_Substances"></a>
## Substances

This window shows the substances that make up the reflectometry sample. By default, "vacuum" and "unit scatterer" are included; others can be added as needed. The reflectometry model is then constructed from layers of these substances.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. Menu '**Edit substance**' –

* **Load substance** – select from a suite of various substance predefined by GSAS-II as defined in GSASII/Substances.py. You may add to this list by adding a file, UserSubstances.py, by following the substance format as described in Substances.py. Place your UserSubstances.py in the GSAS-II directory.
* **Reload substances** – this recomputes the scattering contrast data for the substances.
* **Add substance** – this allows one to enter a new substance that is not among the previously defined ones. Give it a name, element composition and volume/density; GSAS-II will compute the scattering contrast data for it.
* **Copy substances** – this allows one to copy these defined substances to other small angle data histograms.
* **Delete substance** – this allows one to remove any substance but not vacuum or unit scatterer.
* **Add elements** – this allows one to add new element types to a selected substance.
* **Delete elements** – this allows one to remove elements from a substance.

2. You can edit the composition by changing the number of each kind of element and change the sum of atomic volumes or the material density.

<a name="REFD_Sample_Parameters"></a>
## Sample Parameters

This window shows the various sample-dependent parameters for the selected reflectometry pattern. All values shown in this window can be edited. Note that the last three parameters (named `FreePrm`X, X=1,2,3) have labels that can be changed. If changed in one histogram, the same label is used for all histograms. When a label is changed, the Comments tree item for each REFD histogram is searched for a matching "Label=value" pair (differences in letter case between the two label strings is ignored). When found, the value is converted to a float and saved as the appropriate Sample Parameter.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

**Command** Menu - In this window you can change parameters associated with a histogram. This histogram scale factor is ignored for REFD. Remaining parameters are of use for parametric studies and may be changed with the menu commands described here.

* **Set scale** - Rescales a pattern by multiplying by the current scale factor. Scale factor is then set = 1.0. Useful for stitching together partial REFD scans
* **Load** - This loads sample parameters from a previously saved .samprm file.
* **Save** - This saves the sample parameters to a file with the extension '.samprm'. A file dialog box will appear to ask for the name of the file to be written.
* **Copy** - This copies the sample parameters shown to other selected REFD patterns. If used, a dialog box (Copy parameters) will appear showing the list of available powder patterns, you can copy the sample parameters to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.
* **Copy selected...** - This copies only the sample parameter that are selected to other selected REFD patterns but is otherwise similar to "Copy".
* **Copy flags** - (Not valid for REFD).
* **Set one value** - This is used to set a single selected sample parameter for a selected set of REFD histograms. The same value can be used for all histograms or a dialog can be used to provide a table where you can set the values differently for each of selected histograms.
* **Load all** - Reads a file containing a table of sample parameters and copies them to matching REFD entries. The file will look something like the example here:

```
#filename       temperature pressure ignore-me  humidity
LaB6_dc250.tif      100          1      test       .2
LaB6_dc300.tif      150          1      test       .25
```

: Note that the first line(s) in the file can be a header, but each header line must start marked with a hash (#). A header is not required. "Columns" in the table are separated by one or more delimiters (which may be a comma, tab or space). Note that columns do not need to be aligned, as long as each entry is spaced by at least one delimiter. The first column in the table is used to look up REFD entries where the initial space-delimited string after the REFD tag ("myfile" in " REFD myfile AZM=180...") must match the table. Subsequent columns can then be mapped to sample parameters or can be ignored, using a dialog window.

* **Rescale all** - Allows a series of selected REFD histograms to be put on a common scale by integrating them over a specific Q region and then scaling them so that the integration range will match the first pattern. (May not be valid for REFD)

<a name="REFD_Models"></a>
## Models

A reflectometry model is composed of a sequence of layers beginning with the medium ("superphase") as the top layer in which the incident and scattered radiation paths are located (usually "vacuum" = air or other gasses) and ending with the bottom layer ("substrate") upon which the sample layers have been deposited. The substrate is considered to be "infinite" in thickness. The sample layers in between are each defined as a particular substance with a thickness and upper surface "roughness". The surface roughness describes the possibility of an interlayer mixing with the previous layer. Their scattering density can also be scaled and could include polarized magnetic neutron scatterers. The layer sequence is defined so that complex or multiple layers can be defined.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

**Command** Menu  –

* **Fit** – This attempts a refinement by one of 4 different methods of the reflectometry model to the data.
* **Undo** – This reverses the result of a bad refinement; can only be done once.
* **Sequential fit** – This attempts a fit for a sequence of REFD patterns; each has their own model description so one should ensure they are all similar.
* **Copy** – Copy the present model to other REFD patterns.
* **Plot** – Plot the scattering length density (SLD) with respect to the distance from the top surface in Å. Results from multiple REFD fits can be superimposed

