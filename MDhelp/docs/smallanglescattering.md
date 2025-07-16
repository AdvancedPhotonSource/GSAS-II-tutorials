# Small Angle Scattering – type SASD

## Comments

This window shows whatever comment lines found above the QIE table when the small angle data file was read by GSAS-II. If you are lucky, there will be useful information here (e.g. sample name, date collected, wavelength used, etc.). If not, this window will be blank. The text is read-only.

## Limits

This window shows the limits in position to be used in any fitting for this small angle scattering data. The 'original' values are obtained from the minimum & maximum values in the data. The 'new' values determine the range of data that will be used in fitting. Units are in Q (Å-1).

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

You can change the "new" values for Tmin and Tmax as needed. Change the upper and lower Tmin values by clicking on the appropriate vertical line and dragging it to the right or left or by typing values into the data window.

Menu '**Edit Limits**'

* **Copy** - this copies the limits shown to other selected small angle patterns. If used, a dialog box (Copy Parameters) will appear showing the list of available small angle patterns, you can copy the limits parameters to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.

## Instrument Parameters

This window shows the relevant instrument parameter for small angle data; namely a wavelength to relate Q to scattering angle (2Q). It is not refinable.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. Menu '**Operations**' –

    * **Copy** – this copies the instrument parameter shown to other selected small angle data. If used, a dialog box (Copy parameters) will appear showing the list of available small angle data, you can copy the wavelength to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.

2. You can change the wavelength.

## Substances

This window shows the substances that make up the small angle scattering sample. By default, “vacuum” and “unit scatterer” are included; others can be added as needed. The desired substances must be added to Sample Parameters (below) before their use in constructing scattering models for small angle data analysis.

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

## Sample Parameters

This window shows the various sample-dependent parameters for the selected small angle pattern. All values shown in this window can be edited. Note that the last three parameters (named FreePrmX, X=1,2,3) have labels that can be changed. If changed in one histogram, the same label is used for all histograms. When a label is changed, the Comments tree item for each SASD histogram is searched for a matching "Label=value" pair (differences in letter case between the two label strings is ignored). When found, the value is converted to a float and saved as the appropriate Sample Parameter. The last two items define the two components of a small angle scattering sample. One comprises the objects of interest while the other is the marix they are embedded in. The small angle pattern then results from the shape and scattering contrast between the two materials.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

**Command** Menu  - In this window you can change parameters associated with a histogram. This histogram scale factor is ignored for SASD. Remaining parameters are of use for parametric studies and may be changed with the menu commands described here.

* **Set scale** - Rescales a pattern by multiplying by the current scale factor. Scale factor is then set = 1.0. Useful for stitching together partial SASD scans
* **Load** - This loads sample parameters from a previously saved .samprm file.
* **Save** - This saves the sample parameters to a file with the extension '.samprm'. A file dialog box will appear to ask for the name of the file to be written.
* **Copy** - This copies the sample parameters shown to other selected SASD patterns. If used, a dialog box (Copy parameters) will appear showing the list of available SASD patterns, you can copy the sample parameters to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.
* **Copy selected...** - This copies only the sample parameter that are selected to other selected SASD patterns but is otherwise similar to "Copy".
* **Copy flags** - (Not valid for SASD).
* **Set one value** - This is used to set a single selected sample parameter for a selected set of SASD histograms. The same value can be used for all histograms or a dialog can be used to provide a table where you can set the values differently for each of selected histograms.
* **Load all** - Reads a file containing a table of sample parameters and copies them to matching SASD entries. The file will look something like the example here:

```
#filename       temperature pressure ignore-me  humidity
LaB6_dc250.tif      100          1      test       .2
LaB6_dc300.tif      150          1      test       .25
```

Note that the first line(s) in the file can be a header, but each header line must start marked with a hash (#). A header is not required. "Columns" in the table are separated by one or more delimiters (which may be a comma, tab or space). Note that columns do not need to be aligned, as long as each entry is spaced by at least one delimiter. The first column in the table is used to look up SASD entries where the initial space-delimited string after the SASD tag ("myfile" in "SASD myfile AZM=180...") must match the table. Subsequent columns can then be mapped to sample parameters or can be ignored, using a dialog window.

* **Rescale all** - Allows a series of selected SASD histograms to be put on a common scale by integrating them over a specific Q region and then scaling them so that the integration range will match the first pattern. (May not be valid for SASD)

## Models

Small angle scattering models in GSAS-II have four different forms:

* **Size Dist.** – this represents the size distribution for particles of a selected shape (usually “spheroid”, but others possible) via maximum entropy or the Interior-Point Gradient (IPG) method. The result is a volume distribution of particle diameters in Å.
* **Particle Fit** – this gives the best fit of a suite of models for each component of the sample. Each model is chosen from a suite of possible descriptions, each with parameters that describe the shape, size (as a radius, Å) and magnitude.
* **Pair Distance** – this is used as the preliminary step in creating a “beads” model for the shape of a protein and gives the distribution of all interatomic vectors within the protein.
* **Shapes** – after a Pairs Distance distribution has been obtained, this develops a bead model for the protein shape that best satisfies the pair distance distribution using the SHAPES python algorithm developed by J. Badger.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

Menu **Models** –

* **Add** – this adds a distribution to a Particle Fit model
* **Fit** – this does the fitting of the model to the small angle data or bead model to the Pair Distance distribution (Shapes only).
* **Undo** – reverses the last fit operation. Can only be done once for a given fit result.
* **Sequential Fit** – does the fit to a sequence of SAD data. All must have the same model description.
* **Copy** – this copies the current model description to other SASD histograms
* **Copy flags** – this copies refinement flags from the current model to other SASD histograms with the same model.
