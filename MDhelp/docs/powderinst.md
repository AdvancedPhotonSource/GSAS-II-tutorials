<!--- Don't change the HTML version of this file; edit the .md version -->

<a name="PWDR_Instrument_Parameters"></a>
#  PWDR **Instrument Parameters** subdata tree item (Powder Diffraction)

This window shows the instrument parameters for the selected powder data set. Note that the preferred method for use of GSAS-II is that these parameters are fitted only to calibration materials. The parameters fit from the calibrant then defines a set of values unique to that instrumental configuration; these values are not refined when fitting samples. The plot window shows the corresponding resolution curves. 

* Solid lines are for the default values (in parentheses), 
* dashed lines from the refined values and 
* '+' fitted widths for individual entries in the [Peak List](./powderpeaks.md). 

Curves that fall below zero will generate a warning in the plot title, coefficients should be adjusted to ensure every dashed line curve is zero or above.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

### "**Operations**" Menu Commands

A single menu is provided with the selection of instrument parameters.

* **Calibrate**: performs calibration of position dependent instrument coefficients from indexed peak positions.

* **Reset profile**: resets the values for the instrument parameters to the default values shown in parentheses for each entry.

* **Load profile...**: loads a GSAS-II instrument parameter file (name.instprm), replacing the existing instrument parameter values. All refinement flags are unset.

* **Save profile...**: saves the current instrument parameter values in a simple text file (name.instprm); you will be prompted for the file name – do not change the extension. This file may be edited but heed the warning to not change the parameter names, the order of the parameter records or add new parameter records as this will invalidate the file. You may only change the numeric values if necessary. You can change or add comment records (begin with '#').

* **Save all profile...**: saves multibank histogram instrument parameters into a single instprm file. Suitable for neutron TOF instruments.

* **Copy**: this copies the instrument parameters shown to other selected powder patterns. If used, a dialog box (Copy parameters) will appear showing the list of available powder patterns, you can copy the instrument parameters to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation. The copy will only work for instrument parameters that are commensurate with the one that is shown, e.g. single radiation patterns will not be updated from Kα1α2 ones.

* **Copy flags**: this copies the instrument parameter refinement flags shown to other selected powder patterns. If used, a dialog box (Copy refinement flags) will appear showing the list of available powder patterns, you can copy the instrument parameter refinement flags to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation. The copy will only work for instrument parameters that are commensurate with the one that is shown, e.g. single radiation patterns will not be updated from Kα1α2 ones.

* **Set one value**: this is used to set a single selected instrument parameter for a selected set of PWDR histograms. The same value can be used for all histograms, or a dialog can be used to provide a table where you can set the values differently for each of selected histograms.

* **Show multiple**: Displays instrument parameters for all histograms similar to the current selected histogram in a dingle table.

Note that you can change any of the instrument coefficients and the instrument peak widths plot will be updated to show the effect of the change on overall peak widths. 
Note that while the software does allow you to refine any of the instrument coefficients, refinement of these terms is discouraged, except for generating instrumental profiles for calibration. NB: In certain circumstances some refinement choices are ignored: e.g. Zero is not refined (or used) during peak fitting. Also, some parameter choices may lead to unstable refinement, e.g. combining refinement of Lam (wavelength) and lattice parameter. In Rietveld fitting, examine the 'Covariance' display for highly correlated parameters.

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

This plot shows the contributions to the powder pattern peak widths as ΔQ/Q (=Δd/d) vs. Q for the Gaussian and Lorentzian parts of the profile function, in addition to the overall widths. The solid curves are based on the default values of U, V, W, X and Y shown in the Instrument Parameters window (shown in parentheses; these are the values for the instrument contribution that were set when the powder pattern was first read in to GSAS-II.) The dashed values are based on the refined values, if different. If individual peak fitting has been performed, the values of 'sig' & 'gam' for those individually-fit peaks are plotted as '+'; these are computed from the fitted values of U, V, W, X and Y as well as any sig or gam values that are individually refined. For neutron TOF, the curves include those for the α and β coefficients. 

Care should be taken that coefficients do not generate negative peak widths at any point in the pattern where peaks are present. Negative values are not mathematically or physically possible; if encountered in fitting, the corresponding peaks may be ignored. 

