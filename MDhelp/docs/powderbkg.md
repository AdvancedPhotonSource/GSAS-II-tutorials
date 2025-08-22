<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="PWDR_Background"></a>
#  PWDR **Background** subdata tree item (Powder Diffraction)

This window shows the choice of background functions and coefficients to be used in fitting this powder pattern. There are four types of background contributions available here that are summed, so they can be used together, but use care when introducing too many degrees of freedom into background fitting. Note that as numbers are changed in this window, the background is recomputed, so it is possible to visualize the effect of different values and options. 

1. The most commonly used option is a continuous empirical function, with function choices:

:  * "chebyschev", 
      * "chebyschev-1", 
      * "cosine", 
      * "lin interpolate", 
      * "inv interpolate" & 
      * "log interpolate". 
      
      The latter three "interpolate" functions select fixed points with spacing that is equal, inversely equal or equal on a log scale of the x-coordinate. The set of magnitudes at each point then comprise the background variables. All terms are refined when the refine is selected. Note that 'chebyschev-1' is a better choice than 'chebyschev'.

* A set of Debye diffuse scattering equation terms of the form:

    $$
    Background = \sum_{i} A_i  \frac{\sin{QR_i}} {QR_i} e^{-U_iQ^2}
    $$

    where Q = 2π/d and \(A_i\), \(R_i\) & \(U_i\) can be individually selected for refinement as desired and the range for \(i\) is determined by the selected number of terms.

* A set of individual background peaks can be added, These use the pseudo-Voigt profile function as their shapes. Their parameters are "pos" (peak position), "int" (integrated intensity), "sig" (Gaussian width) & "gam" (Lorentzian width); each can be selected for refinement, but it is uncommon to fit both both sig and gam. The default values for sig & gam (=0.10) are for very sharp peaks. For typical background use, values of 100 to 10,000 for sig are more common. You may adjust them accordingly to the kind of peak you are trying to fit before trying to refine them. It is common to use these with the 'chebyschev-1' function, where a small number of terms allows the chebyschev-1 to fit a smooth, slowly-varying, function and the background peaks account for broad "lumps" in the pattern, such as what arises from Kapton. 

* Subtract an experimentally measured background. The experimentally measured background points are scaled by a multiplier that can be refined to account for sample absorption effects. 

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

### "**Background**" Menu Commands

  * **Copy** – this copies the background parameters shown to other selected powder histograms. If used, a dialog box (Copy Parameters) will appear showing the list of available powder patterns, you can copy the background parameters to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.
  * **Copy flags** – this copies only the refinement flags shown to other selected powder patterns. If used, a dialog box (Copy Refinement Flags) will appear showing the list of available powder patterns, you can copy the refinement flags to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.
 * **Save** –  saves the background values to a file so the can be used in a different GSAS-II project (`.gpx` file).
 * **Load** – Reads in background values from  a file created with the Save command.  

### "**Fixed Points**" Menu Commands 
 * **Add** – When this is selected, it is marked as checked. In this mode clicking on the pattern will add a background point (marked as a large red diamond) to the pattern. This will be used with the "Fit Background" menu command or button.  
 * **Move** –  When this is selected, it is marked as checked. In this mode background points can be dragged to new positions.
 * **Delete** – When this is selected, it is marked as checked. In this mode clicking on a background point will delete it
 * **Clear** –  Deletes all fix background points
  * **Fit Background** – When this is used, the refined terms in the background functions are refined to best fit the fixed background points. Note that the "Fit to fixed bkg" button does the same thing as this menu command, but is more convenient.

Things you can do here:

2. You can select a different Background function from the pulldown tab.
3. You can choose to refine/not refine the background coefficients.
4. You can select the number of background coefficients to be used (1-36). You should use the minimum required.
5. You can change individual background coefficient values. Enter the value then press Enter or click the mouse elsewhere in the Background window. This will set the new value.
6. You can introduce one or more Debye scattering terms into the background. For each one you should enter a sensible value for 'R' – an expected interatomic distance in an amorphous phase is appropriate. Select parameters to refine; usually start with the 'A' coefficients.
7. You can introduce single Bragg peaks into the background. For each you should specify at least the starting position. Select parameters to refine; usually start with the 'int' coefficients. Set the "sig" value manually to give a breadth that visually seems to match the pattern. You may need to increase "int" significantly to see the effect of changing "sig" in the plot. 
8. You can select an experimentally measured background pattern from those in the GSAS-II data tree and scale it with a multiplier.
1. You can place fixed background points on the pattern and then fit background coefficients to fit them. If this is done, it is possible to postpone the Rietveld fitting of the background until the late stages of the fit. This can greatly simply fitting of patterns with messy background intensities and that have poorly fit models, by allowing you to concentrate on improving the model. Note that the tutorial [Fitting the Starting Background using Fixed Points](https://advancedphotonsource.github.io/GSAS-II-tutorials/BkgFit/FitBkgTut.htm) shows how this is done. 
1. You can automatically generate fixed background points across the pattern using the "Compute auto background" button. This creates a smooth function that will tend to ignore sharp peaks. 
: * There are two functions available, "arpls" and "iarpls"; you can choose the one that works best for you. 
: * The "log(Lambda)" term is a spline coefficient that determines how much the background can "wiggle" (have sharper variations). As this is moved, the resulting background function is shown. 
: To complete the operation, one can either use 
: * "Set Fixed Points & Fit", which creates fixed background points across the entire pattern and then fits the refined background terms.
: * "Define Fixed Bkg histogram" creates a histogram of fixed background points and sets this to be subtracted from the current pattern. 
: Note that this computation is done with the [`pybaselines` package](https://pybaselines.readthedocs.io/en/latest/), [which must be installed into Python](./mainmenu.md#Help_addpkgs) to use this feature. 

Any modification of the background representation will be immediately applied to the calculated pattern so you can see its effect.


<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

The plot is the largely the same as for the parent PWDR Powder Histograms tree entry 
[with the same plot actions](./powder.md#PWDR_plot_actions) and [same key press commands](./powder.md#PWDR_keylist), except that tickmarks are not shown and the obs-calc position cannot be dragged.
Specific to this plot are fixed background points. These can be added, deleted and moved. Once that is done the background parameters for the selected function can be fitted to the fixed points. NB: the number of fixed points must exceed the number of background parameters to be fitted. Not recommended for fitting sharp Bragg peak backgrounds unless sufficient fixed points are selected across each Bragg peak.
