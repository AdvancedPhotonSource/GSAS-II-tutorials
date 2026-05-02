<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="PWDR_Background"></a>
#  PWDR **Background** sub-data tree item (Powder Diffraction)

This window shows the choice of background functions and coefficients to be used in fitting this powder pattern. There are four types of background contributions available here. These functions are summed, so they can be used together, but use care when introducing too many degrees of freedom into background fitting. Note that as numbers are changed in this window, the background is recomputed, so it is possible to visualize the effect of different values and options. 

### Background Function

* The most commonly used option is a continuous empirical background function, with function choices:

:  * "chebyschev", 
      * "chebyschev-1", 
      * "cosine", 
      * "lin interpolate", 
      * "inv interpolate",
      * "log interpolate". 
      
      The latter three "interpolate" functions select fixed points with spacing that is equal, inversely equal or equal on a log scale of the x-coordinate. The set of magnitudes at each point then comprise the background variables. All terms are refined when the refine flag is selected. Note that 'chebyschev-1' is a better choice than 'chebyschev'. The latter option is included only for compatibility with older fits. It may be removed someday. 

### Debye Diffuse Scattering

* Uses the Debye diffuse scattering equation to compute a multi-peaked broad background function that is commonly seen from amorphous materials. 
 It is parameterized using sets of terms $A_i$, $R_i$ & $U_i$ that can be individually selected for refinement, as desired.
 The number of sets of terms to be included, e.g. the allowed values of $i$, is determined by the user. 
 
    The Debye diffuse scattering equation,  where $Q = 2\pi/d$, is:

    $$ Background = \sum_{i} A_i  \frac{\sin{QR_i}} {QR_i} \exp{(-U_iQ^2)}$$


### Background Peaks

* This provides a set of individual background peaks that can be added to the background. 
These use the pseudo-Voigt profile function as their shapes. Their parameters are "pos" (peak position), "int" (integrated intensity), "sig" (Gaussian width) & "gam" (Lorentzian width). Note that both "sig" and "gam" can be selected for refinement together, but it is most common to fit only one. The default values for sig & gam (=0.10) generate for very sharp peaks. For typical background use, values of 100 to 10,000 for sig are more common. You may want to manually adjust them accordingly to the kind of peak you are trying to fit before trying to refine them. It is common to use these with the 'chebyschev-1' function, where a small number of terms allows the chebyschev-1 to fit a smooth, slowly-varying, function and the background peaks account for broad "lumps" in the pattern, such as what arises from Kapton scattering or with 
other sample container peaks.

### Measured Background Histogram Subtraction

* This allows subtraction of an experimentally measured background pattern. It is also possible to generate such a pattern with the [auto-background feature](#autobackground). The experimentally measured background points are scaled by a multiplier that can be refined to account for sample absorption effects. The background pattern should be imported as a Powder Data (PWDR) entry, but should not be associated with any phases. The angular range and the step size must match the current histogram, as background is subtracted point-by-point.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

#### "**Background**" Menu Commands

  * **Copy** – this copies the background parameters shown to other selected powder histograms. If used, a dialog box (Copy Parameters) will appear showing the list of available powder patterns, you can copy the background parameters to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.
  * **Copy flags** – this copies only the refinement flags shown to other selected powder patterns. If used, a dialog box (Copy Refinement Flags) will appear showing the list of available powder patterns, you can copy the refinement flags to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.
 * **Save** –  saves the background values to a file so the can be used in a different GSAS-II project (`.gpx` file).
 * **Load** – Reads in background values from  a file created with the Save command.  

#### "**Fixed Points**" Menu Commands 

The first three menu commands select a modes for changing fixed background points; one must be selected; the selected mode will have a checkmark and the mode is also displayed on the plot.
In addition to using these menu commands to change the mode, the "k" key can also be used.
<a name="fixedbackgroundmode"></a>. See the discussion on [fixed background point fitting](#fixedbackground) for more information on this. 

* **Add** – In this mode clicking on the pattern will add a background point to the pattern. 
 * **Move** – In this mode background points can be dragged to new positions.
 * **Delete** – In this mode clicking on a background point will delete it
 
The remaining "**Fixed Points**" Menu Commands perform actions:
 
 * **Clear** –  Deletes all fix background points
  * **Fit Background** – When this is used, the refined terms in the background functions are refined to best fit the fixed background points. 
  Note that the "Fit to fixed bkg" button does the same thing as this menu command, 
  but is likely more convenient to use.

#### Actions:

The "Background" data tree item offers many options that can be used to fit different forms of background scattering, as may occur in powder diffraction histograms. Things you can do here include:

2. You can select a different Background function from the pulldown tab.
3. You can choose to refine/not refine the background coefficients.
4. You can select the number of background coefficients to be used (1-36). You should use the minimum required.
5. You can change individual background coefficient values. Enter the value then press Enter or click the mouse elsewhere in the Background window. This will set the new value.
6. You can introduce one or more Debye scattering terms into the background. For each one you should enter a sensible value for 'R' – an expected interatomic distance in an amorphous phase is appropriate. Select parameters to refine; usually start with the 'A' coefficients.
7. You can introduce single Bragg peaks into the background. For each you should specify at least the starting position. Select parameters to refine; usually start with the 'int' coefficients. Set the "sig" value manually to give a breadth that visually seems to match the pattern. You may need to increase "int" significantly to see the effect of changing "sig" in the plot. 
8. You can select an experimentally measured background pattern from those in the GSAS-II data tree and scale it with a multiplier.
1. You can place fixed background points on the pattern and then fit background coefficients to fit them. If this is done, it is possible to postpone the Rietveld fitting of the background until the late stages of the fit. This can greatly simply fitting of patterns with messy background intensities and that have poorly fit models. 
This allows you to concentrate on improving the model. Note that the tutorial [Fitting the Starting Background using Fixed Points](https://advancedphotonsource.github.io/GSAS-II-tutorials/BkgFit/FitBkgTut.htm) shows how this is done. 
1. You can automatically generate fixed background points across the pattern using the "Compute auto background" button. This creates a smooth spline function that will tend to ignore sharp peaks. Selecting this will open a new window with a number of options. See [Working with auto-background below](#autobackground) for more discussion.

Any modification of the background parameters shown here, including by manual editing of numbers, will be immediately applied to the calculated pattern so you can see its effect.


<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

The plot is the largely the same as for the parent PWDR Powder Histograms tree entry 
[with the same plot actions](./powder.md#PWDR_plot_actions) and [same key press commands](./powder.md#PWDR_keylist), except that tickmarks are not shown and the obs-calc position and excluded regions cannot be dragged. The data limits can be dragged, and since the plotting of the x-axis can be done in Q or d-space, this plot allows the limits to be set graphically in Q or d-space, 

Specific to this plot are fixed background points. These can be added, deleted and moved. Once that is done the background parameters for the selected function can be fitted to the fixed points. NB: the number of fixed points must exceed the number of background parameters to be fitted. Not recommended for fitting sharp Bragg peak backgrounds unless sufficient fixed points are selected across each Bragg peak.

<a name="autobackground"></a>
### Working with auto-background

* You can automatically generate fixed background points across the pattern using the "Compute auto background" button. This creates a smooth spline function that will tend to ignore sharp peaks. Selecting this will open a new window with the following options: 
: * There is a choice of two functions for the spline: "arpls" and "iarpls". You are suggested to try each and choose the one that works best for you. 
: * The "log(Lambda)" term is a spline coefficient that determines how much the background can "wiggle" (have sharper variations). As the slider for this is is moved, the resulting background function is shown. 
: To complete the operation, one can use either of the two buttons: 
: * "Set Fixed Points & Fit", which creates fixed background points across the entire pattern and then fits the refined background terms.
: * "Define Fixed Bkg histogram" creates a histogram of fixed background points and sets this to be subtracted from the current pattern. 
: Note that this computation is done with the [`pybaselines` package](https://pybaselines.readthedocs.io/en/latest/), [which must be installed into Python](./mainmenu.md#Help_addpkgs) in order to use this feature. 

<a name="fixedbackground"></a>
### Working with fixed background points

* The purpose for fixed background points is for interactive 
fitting of background functions using the "Fit Background" menu command or the equivalent  "Fit to fixed bkg" button. They are only used with this data tree item. 

    Fixed background points are marked on the plot with a large red diamond. 
They are only seen or are used when the Background data tree item is selected. 

    Fixed background points can be placed manually in the locations where you think 
the background should be placed or these points can be generated with the "Compute auto background" button. Depending on the mode that is selected (see the [Fixed Points menu commands](#fixedbackgroundmode)), points can be added by clicking on the location in the 
plot where points should be added, moved by dragging the points or deleted by clicking on the point to be deleted.

    When the background is fit using the menu command or button, any background parameters selected to be refined are optimized to produce a background curve that 
best-fits the fixed background points. There must be more fixed background points than refined parameters. Mist commonly, the background generated with fixed background points is used as a starting point for the background when one is fitting a material with a complex background. If so, once a good starting background is obtained, turn off the background refinement flags so that the background will not 
be optimized in a Rietveld or peak list fit. However, in Rietveld fitting, it is recommended that the background be fit against the actual data points. This will be done by adding the background refinement flag(s) back again in the final fitting stage. 
