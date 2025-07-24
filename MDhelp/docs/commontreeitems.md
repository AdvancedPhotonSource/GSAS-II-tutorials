<!--- Don't change the HTML version of this file; edit the .md version -->
# Universal Data Tree Items

The data tree items listed below will appear in every GSAS-II project once any histogram or phase has been placed in the project. 

<a name="Notebook"></a>
## Notebook

This window provides a log of information on what has been done in a project.
Some GSAS-II operations (*e.g.*, structure refinement, Fourier map calculation & peak fitting) will add entries to the notebook. You may also place whatever text commentary you wish into the window by clicking on the "Add comment" button. The comment will be time-stamped and placed appropriate order in the log. 

* Normally entries are shown in reverse chronological order ("newest-1st"), but that button allows sorting with the oldest entries first ("oldest-1st").

* The "Set filters" button allows you to select which type of entries are shown, as are selected on a list. Note that older Notebook entries were not recorded with tags that allow filtering to work. 

* The "Plot" button allows plotting the progression of the overall Rw or reduced \(\chi^2\) in the refinement. 

* The "Save" button writes the contents of the Notebook as a text file named &lt;project&gt;-notebook.txt. 

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

Use the notebook to keep track of information related to how you use GSAS-II, what has been done or to plot the progress of the fit. When you make different copies of a fit to try out different refinement options, it will be very helpful to put a comment here to help you remember what you did. 

<a name="Controls"></a>
## Controls

This window provides access to the controls that determine how GSAS-II performs minimizations as well as few global parameters for GSAS-II. Note that many other customization settings are set as  [configuration variables](./others.md#config) in the File/Preferences menu. (See the 
[Configuration variables section of the Programmer's documentation.](https://gsas-ii.readthedocs.io/en/latest/GSASIIutil.html#config-example-py-configuration-options) for listing of these options.)

1. **Refinement Controls**: 
<a name="RefinementControls"></a>
 These controls determine how refinements are performed. The first determines the computational engine used to minimize the structure.

    * **Refinement type** - 
    <a name="RefineType"></a>
    This determines how structure refinements are performed. The choices are:
        * **analytic Hessian**: This is the default option and is usually the most useful. It uses a custom-developed least-squares minimizer that uses singular-value decomposition (SVD) to reduce the errors caused by correlated variables and the Levenberg-Marquardt algorithm to up-weight diagonal Hessian terms when a refinement step fails to lower χ2.
        * **analytic Jacobian**: This uses the numpy-provided `leastsq` minimizer, which not applicable for problem with a large number of histograms as it requires much more memory than the Hessian routines. This because it creates a Jacobian matrix (J) that is shaped N x M (N parameters x M observations) that is used to create the N x N Hessian. The Hessian method creates a Jacobian matrix only for each histogram; the N x N Hessian is the made from summing the J x J\(^T\) products across the histograms
        * **numeric**: This also uses the numpy leastsq minimizer and is also not applicable for larger problems. Unlike, the "analytic Jacobian", numerical derivatives are computed rather than use the analytical derivatives that are coded directly into GSAS-II. This will be slower than the analytical derivatives and will is often less accurate which results in slower convergence. It is typically used for code development to check the accuracy of the analytical derivative formulations.
        * **Hessian SVD**: This is very similar to analytic Hessian but does not include the Levenberg-Marquardt algorithm. It can be faster but is more prone to diverge when severe correlation is present. It is possible that it might be better for single-crystal refinements.

    Note that the Jacobian refinement tools are the Fortran MINPACK` lmdif` and `lmder` algorithms wrapped in Python, as provided in the numpy/Scipy package. The Hessian routines were developed for GSAS-II based on routines in numpy and scipy and used aw well material from *Numerical Recipes* (Press, Flannery, Teulosky & Vetterling) for the Levenberg-Marquardt algorithm. The `lmdif` and `lmder` routines were written by Burton S. Garbow, Kenneth E. Hillstrom, Jorge J. Moré (Argonne National Laboratory, 1980).

    * **Min delta-M/M** - A refinement will stop when the change in the minimization function, *M*,  \( (M=\sum[w(I_o-I_c)^2]) \) is less than this value. The allowed range is \(10^{-9}\) to 1.0, with a default of 0.001. A value of 1.0 stops the refinement after a single cycle. Values less than \(10^{-4}\) cause refinements to continue even if there is no meaningful improvement.
    * **Max cycles** - This determines the maximum number of refinement cycles that will be performed. This is used only with the "analytical Hessian" and "Hessian SVD" minimizers.
    * **Initial lambda** - Note that here λ is the Marquardt coefficient, where a weight of 1+λ is applied to the diagonal elements of the Hessian. When λ is large, this down-weights the significance of the off-diagonal terms in the Hessian. Thus, when λ is large, the refinement is effectively one of steepest-descents, where correlation between variables is ignored. Note that steepest-descents minimization is typically slow and may not always find the local minimum. This is only used when with the "analytical Hessian" minimizer is selected.
    * **SVD zero tolerance** - This determines the level where SVD considers deivative values to be the same. Default is \(10^{-6}\). Make this larger when problems occur due to correlation. This is used only with the "analytical Hessian" and "Hessian SVD" minimizers.
    * **Initial shift factor** - This provides an initial scaling ("damping") for the first cycle of refinement. Only available for "analytic Jacobian" and "numeric" minimizers. 

2. **Single Crystal Refinement Settings**: 
<a name="SingleXtlSettings"></a> 
A set of controls is provided for control of single-crystal refinements. These only appear when single crystal (HKLF) histograms are present in the project.
   
    * **Refine HKLF as F^2?** - When checked, refinements are against \(F^2\) rather than \(|F|\).
    * **Min obs/sig** - Conventional cutoff for single crystal refinements as to what reflections should be considered observed, typical values are 2.0 (\(2\sigma\)) or 3.0 (\(3\sigma\)).
    * **Min extinct.** - Reflections with extinction corrections larger than this value are ignored.
    * **Max delt-F/sig** - Removes reflections that are very poorly fit. Should be used only with extreme care, since poorly-fit reflections could be an indication that the structure is wrong.
    * **Max d-spacing** - Reflections with d-space values larger than this value are ignored.
    * **Min d-spacing** - Reflections with d-space values smaller than this value are ignored. 

3. **Sequential Settings**: 
<a name="SequentialSettings"></a> 
 A set of controls is for sequential refinement. Settings here determine if a "normal" or "sequential" refinement is performed. If no datasets are selected here, then all histograms linked to phases in the project and that are flagged as "used" are included in one potentially large (combined) refinement. However, if any number of histograms are selected here as used in a sequential fit, then each of the selected histograms is fitted in turn, which in GSAS-II is called a sequential refinement. Only the first item below is shown in "normal" mode.

    * **Select datasets/Reselect Datasets** - This brings up a menu where histograms can be selected, which potentially switches between a normal and a sequential refinement. If one or more histograms are selected, a sequential refinement is used. If none are selected, then the refinement be set as "normal". The button is labeled "Select" when in normal refinement mode and "Reselect" in sequential refinement mode.
    * **Reverse order?** - Normally, in a sequential refinement histograms are fit in the order they are shown in the data tree (which can be reordered by dragging tree items), but when this option is selected, the sequential fit is performed in the opposite order, with the last tree entry first.
    * **Copy results to next histogram?** - When this option is selected, the fitted parameters from each refinement are copied to the next histogram, so that the starting point for each refinement will be the results from fitting the previous. This works well for parametric experiments where parameters such as the lattice parameters change gradually over the course of successive measurements. This option is usually used only for the initial refinement after a sequential fit is started and the setting is cleared once that refinement is completed. For subsequent refinements, it is usually better to start with the results from the previous fit.
    * **Clear previous seq. results** - When this button is pressed, the "Sequential Results" entry with the results from the last sequential fit is deleted from the tree.

4. **Global Settings**: This is a location for parameters that apply to an entire project. At present there is only one:

    * **CIF Author** - The value provided here is used when creating a CIF of an entire project. 

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

This offers a place to change how GSAS-II performs refinements, but has no specific menu commands or graphics.

<a name="Covariance"></a>
## Covariance

This window contains residual information after the last refinement. When this tree item is selected, the GSAS-II Plots window shows '**Covariance**', with a graphical representation of the variance-covariance matrix. The text in the data window shows statistical values related to the current fit. At the bottom of this list are buttons that display a horizontal bar chart with the shift to standard uncertainty ratio for each parameter.

* The button labeled "last refinement" shows these ratios based on the differences between each parameter value from the beginning of the refinement run and the value at the end of the refinement run.
* The button labeled "last cycle" shows these ratios based on the differences between each parameter value at the beginning of the last refinement least squares cycle and the value at the end of the cycle (and the refinement run). (These "last cycle" values are only available when the [Controls](#Controls) are set for an "analytic Hessian" refinement.) 

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

The variance-covariance matrix as a color-coded array is shown on this page. The color bar to the right shows the range of covariances (-1 to 1) and corresponding colors. The parameter names are to the right and the parameter numbers are below the plot. 

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

* Move the mouse cursor across the plot. If on a diagonal cell, the parameter name, value and standard uncertainty (esd) is shown both as a tooltip and in the right-hand portion of the status bar. If the cursor is off the diagonal, the two parameter names and their covariance are shown in the tool tip and the status bar.
* Use the Zoom and Pan buttons to focus on some section of the variance-covariance matrix.
* Press 's' – A color scheme selection dialog is shown. Select a color scheme and press OK, the new color scheme will be plotted. The default is 'RdYlGn'.
* Press 'p' – Saves the covariance values in a text file.

<a name="Constraints"></a>
## Constraints

This window shows the constraints to be used in a refinement. Constraints are divided with a tab for each type: Phase, Histogram/Phase, Histogram, Global and Sym-Generated. Note that the standard parameters in GSAS-II are divided into three classes and appear respectively on the Phase, Histogram and Histogram/Phase tabs:

* those pertaining to quantities in each phase (naming pattern `p::name`); examples include atom coordinates, thermal motion and site fraction parameters;
* those pertaining to quantities in each histogram (naming pattern `:h:name`); such parameters are those that depend only on the data set: the scale factor and profile coefficients (e.g. U, V, W, X and Y);
* and those pertaining to quantities defined for each histogram in each phase (naming pattern `p:h:name`); these parameters are quantities that can be dependent on both the phase properties and the sample or dataset used for the measurement. Examples include phase fractions and sample-broadening coefficients such as microstrain and crystallite size; they are found in the Data tab for each phase.

The following types of constraints may be specified by users:

* **Holds** - Use this to prevent a parameter from being refined. Most valuable when refinement of a parameter is selected in a group for refinement (such as x, y & z for an atom or unit cell parameters) and one must be fixed. For example, if the space group for a phase has a polar axis (e.g., the y-axis in monoclinic space group \(P \ \rm 2_1\), the origin with respect to *b* is arbitrary). With a polar axis present, if an arbitrary constant is added to all atom coordinates along that axis, a completely equivalent structure is obtained. Thus in \(P \ \rm 2_1\) it is not possible to refine the y coordinates for all atoms. Place a Hold on any one atom y coordinate to keep the structure from drifting up or down the y-axis during refinement.

* **Equivalence assignments** - Determines a set of parameters that should have values with a specified ratio. Atom coordinates are handled slightly different, where the ratios are specified for the applied shifts, not the actual coordinate values. Examples for typical use are sets of atoms that should be constrained to have the same displacement parameters (aka thermal motion, Uiso, etc.) or sets of profile coefficients U, V & W across multiple data sets. Note that the first selected parameter is treated as independent, and the remainder are "slaved" to that parameter as "dependent parameters." All parameters in an equivalence must be varied. If any parameter is not varied or is given a "hold," a warning is displayed and none of the parameters in the equivalence are refined.

* **Constraint Equations** - Defines a set of parameters whose sum (with possible non-unitary multipliers) will be equal to a constant. For example, a common use for this is to specify the sum of occupancies for atoms sharing a site have a sum fixed to unity or so that the sum of occupancies for an atom type that is occurs on several sites is fixed to match a composition-determined value. Note that all parameters in the equation are considered as "dependent parameters." If a parameter in a constraint equation is held or is not varied, that parameter is removed from the equation (the sum value is modified accordingly). If no parameters remain the equation is ignored.

* **New Var assignment** - These are similar to constraint equations in that they define a set of parameters and multipliers, but rather than specifying a value for the expression, a new parameter is assigned to that sum. Thus these constraints create new variable that effectively replace the original GSAS-II parameters with ones supplied by the user. This is done by replacing a degree of freedom from the original variables with a new one that modifies the parameters, where the shift is applied according to the ratio specified in the expression. This can be used to create new parameters that redefine the relationships between items such as coordinates or magnetic moments. The new parameter may optionally be named by the user. The new var expression creates a new global parameter, where that new parameter is independent, while all the parameters in the expression are considered as dependent. The setting of the refine flags for the dependent parameters is not used. Only if the new var parameter is marked as `refine` then it will be refined. However, if any dependent variable is set as "hold," the **new var** parameter will not be refined.

    **New Var** constraints are generated when [ISODISTORT](https://iso.byu.edu/isodistort.php) is used to develop mode distortions from a comparison of a high symmetry parent structure (e.g. cubic perovskite) with a distorted child substructure. They are implemented for the phase when a special CIF file produced by ISODISTORT from a mode distortion analysis is imported. You can select which distortion modes to refine. Refining all modes is equivalent to refining the atoms freely and then importing the resulting structure to ISODISTORT to determine the mode amplitudes. 

Note that when new var and constraint equation constraints are defined, they create new global parameters. Constraints on these will be rare, but can be managed on the Globals tab. Finally, some constraints are defined automatically based on restrictions determined by space group symmetry. These constraints can be seen, but not changed, using the Sym-Generated tab. Other constraints (holds) will be created when rigid bodies are specified.


<H3 style="color:blue;font-size:1.1em">What can I do here?</H3> 

Select the tab for the parameter type(s) you wish to constrain then create new parameters using the "Edit Constr." menu commands:

* **Add Hold** - Select a parameter that you wish to remain fixed. If selected, a dialog box will appear showing the list of available parameters; select one and then OK to implement it, Cancel will cancel the operation. The held parameter will be shown in the constraint window with the keyword 'FIXED'.
* **Add equivalence** - Select the independent parameters and press OK; a second dialog box will appear with only those parameters that can be made equivalent to the first one. Choose those and press OK. Cancel in either dialog will cancel the operation. The equivalenced parameters will show as an equation of the form \(M1*P1+M2*P2=0\); usually M1=1.0 and M2=-1.0 but can be changed via the 'Edit' button. The equation(s) are shown in the window tagged by 'EQUIV' to mark it as an equivalence assignment.
* **Add constraint** - If selected, a dialog box will appear with a list of the available parameters. Select one and press OK; a second dialog box will appear with only those parameters that can be used in a constraint with the first one. Choose those and press OK. Cancel in either dialog will cancel the operation. The equivalenced parameters will show as an equation of the form \(M1*P1+M2*P2+…=C\); the multipliers M1, M2, … and C can be changed via the 'Edit' button. The equation is shown in the window tagged by 'CONSTR' to mark it as a constraint equation assignment.
* **Add New Var** - This behaves very much like the "Add constraint" menu command except that it defines a new parameter rather than define a value for the expression. That new var parameter can optionally have a named assigned. The expression is displayed with the keyword 'New Var' to mark its type. Note that a 'Refine?' box is included for this type of constraint.
* **Make atoms equivalent** - This provides a shortcut for establishing constraints when two share a single site. Coordinates and Uiso values are constrained to be the same and site fractions are constrained to add to 1.
* **Show ISODISTORT modes** - Used after a CIF from the ISODISTORT web site is read, which will display the values for the normal modes from representational analysis from the coordinates.

In addition to menu commands, this window also offer the following actions by pressing buttons:

* **Show Errors** - this button will be active if serious errors -- that would prevent a refinement from being performed -- are encountered processing the constraints.
* **Show Warnings** - this button will be active if correctable problems are encountered in processing the constraints, such as a constraint being rejected because a parameter is not varied. These warning may indicate that the choice of which parameters will be refined is not what was planned.
* **Show Generated Constraints** - After constraints have been processed, a series of relationships are developed to determine new variables from the current parameters and "inverse" equations that determine dependent parameters from the new variables and independent parameters. This shows the resulting relationships, as well as any "Hold" variables.
* **Delete Selected** - This button will cause all the selected constraints on the current tab to be deleted.

<a name=Constraints-SeqRef></a>
### Sequential Refinement Constraints

While all the general information on constraints (above) applies to sequential refinements, the sequential refinement is performed by fitting each histogram individually and this affects how constraints are defined and processed for parameters keyed to a particular histogram number. When sequential refinement is selected (via the [Controls](#Controls) tree item), it becomes possible to define constraints of form `p:*:name` and `:*:name` (where "p" is a phase number and name is a parameter name). The "*" here is called a wildcard, and in a constraint or equivalence will cause that to be used for every histogram in turn.

In sequential refinement mode, two additional controls are shown in the Constraints window. The first, which is labeled wildcard use, specifies what is done when a specific histogram is referenced by number in a constraint or equivalence by number rather than by wildcard. This offers three modes:

* **Set hist # to \*** - Any constraints previously specified with a specific histogram number will be changed to apply to all histograms. This is the default for new projects.
* **Ignore unless hist=\*** - Any constraints previously specified with a specific histogram number will be ignored and constraints with a "*" for a histogram number will be used. Note that constraints on phase parameters (of form 'p::name' -- without a histogram number specified) will be used normally. Note that this was the operating mode for GSAS-II in earlier versions before these buttons were introduced.
* **Use as supplied** - If different constraints are to be applied to different histograms, it becomes necessary to create constraints with specific histogram numbers. In this mode, constraints specified with a specific histogram are applied only to that histogram, while wildcarded ones are applied to all histograms. Note that one should not specify two constraints on a single parameter, one with a wildcard and one with a specific histogram number, as both will be applied to the specified histogram which results in an unsatisfiable conflict.

Also included when sequential refinement is selected is a menu button labeled "Selected histogram." With this it is possible to look at constraint problems when processing a specific histogram.

<a name="Restraints"></a>
## Restraints

This window shows the restraints to be used in a refinement for each phase (if more than one). It is organized into several tabbed pages, one page for each type of restraint. Restraints are developed for an individual phase and act as additional observations to be "fitted" during the refinement.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

* Select the tab for the restraint type you wish to use. Each will have the same possibilities in the 'Edit' menu.
* You can change the Restraint weight factor – this is used to scale the weights for the entire set of restraints of this type. Default value for the weight factor is 1.0.
* You can choose to use or not use the restraints in subsequent refinements. Default is to use the restraints.
* You can change the search range used to find the bonds/angles that meet your criteria for restraint.
* You can examine the table of restraints and change individual values; grayed out regions cannot be changed. The 'calc' values are determined from the atom positions in your structure, 'obs' values are the target values for the restraint and 'esd' is the uncertainty used to weight the restraint in the refinement (multiplied by the weight factor).
* Menu 'Edit' – some entries may be grayed out if not appropriate for your phase or for the selected restraint.

    * **Add restraints** - this takes you through a sequence of dialog boxes which ask for the identities of the atoms involved in the restraint and the value to be assigned to the restraint. The esd is given a default value which can be changed after the restraints are created.
    * **Add residue restraints** - if the phase is a 'macromolecule' then develop the restraints from a selected 'macro' file based on those used in GSAS for this purpose. A file dialog box is shown directed to /GSASIImacros; be sure to select the correct file.
    * **Add MOGUL restraints** - add restraints in the style of the MOGUL program
    * **Plot residue restraints** - if the phase is a 'macromolecule' and the restraint type is either 'Torsion restraints' or 'Ramachandran restraints', then a plot will be made of the restraint distribution; torsions as 1-D plots of angle vs. pseudopotential energy and Ramachandran ones as 2-D plot of psi vs phi. In each case a dialog box will appear asking for the residue types or specific torsion angles to plot. Each plot will show the observed distribution (blue) obtained from a wide variety of high-resolution protein structures and those found (red dots) for your structure. The restraints are based on a pseudopotential (red curve or contours – favorable values at the peaks) which has been developed from the observed distributions for each residue type.
    * **Change value** - this changes the 'obsd' value for selected restraints; a dialog box will appear asking for the new value.
    * **Change esd** - this changes the 'esd' value for selected restraints; a dialog box will appear asking for the new value.
    * **Delete restraints** - this deletes selected restraints from the list. A single click in the blank box in the upper left corner of the table will select/deselect all restraints.

<a name="Rigidbodies"></a>
<a name="Rigid_bodies"></a>
## Rigid bodies

There are three different types of rigid bodies that can be used in GSAS-II, as selected by the tabs at the top of this window. 

* **vector rigid bodies**, where atoms are defined in terms of multiple displacements from an origin. 
* **residue rigid bodies**, where atoms are defined according to Cartesian coordinates and torsion angles. These are much more commonly used than vector rigid bodies. 
* **spinning rigid bodies**, where the dynamics or disorder causes the atoms to not have specific locations in the unit cell. 

Note that there are two steps in defining a rigid body. In this data item the rigid body is defined. The rigid body is then later inserted into one or more phases using the ["RB Models"](./phaseRB.md) tab on a Phase data item. A rigid body can be inserted into more than one phase. 

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

* Select the tab for the rigid body type you wish to use. 
* Once the rigid body type has been selected, use the menu commands listed below. The menu contents will depend on which type of rigid body is selected.
* Editing of some of much of the rigid body information can be done in the data window once a body is created. 

    * **Add rigid body** - (Vector & Spinning rigid bodies). For vector bodies this creates a vector description of a rigid body. A dialog box asks the number of atoms (>2) and the number of vectors required to create the rigid body. An entry will be created showing a magnitude with the vector set to be applied for each vector needed to develop the rigid body.
    
    * **Extract from file** - (Vector & residue rigid bodies). This prepares a rigid body by reading in coordinates (typically as fractional coordinates) and then atoms are selected from the file that is read and finally the origin and axes of the Cartesian system used by the rigid body are defined.

    * **Save rigid body** - (Vector & Spinning rigid bodies). Writes the contents of a defined rigid body into a file where it can be reused in another GSAS-II project. A different format is used for vector vs. residue bodies.
    
    * **Read rigid body** - (Vector & Spinning rigid bodies). Creates a rigid body from a file written perviously by a "Save rigid body" command.
    
    * **Add translation** - (Vector rigid bodies). The Cartesian coordinates for the body are created from the sum of coordinate matrices multiplied by a value that converts the arbitrary axis lengths to Angstroms. One can sum 9 multiplier/coordinate matrix sets. This command will add an additional "translation" consisting of a multiplier and coordinates for every atom in the rigid body. 
    
    * **Import XYZ** - (Residue rigid bodies) this reads a text file containing a set of Cartesian coordinates describing a rigid body model. Each line has atom type (e.g. C, Na, etc.) and Cartesian X, Y and Z.
    * **Save as PDB** - (Vector rigid bodies). Writes the contents of a defined rigid body as Cartesian coordinates in a PDB file. 

    * **Define Torsion** - (Residue rigid bodies) this adds a variable torsion angle in an existing rigid body via a sequence of dialog boxes. The first one asks for the origin and the second asks for the pivot atom for the torsion from the nearest neighbors to the origin atom; the atoms that ride on the selected torsion are automatically found from their bond lengths.
    * **Import residues** - (Residue rigid bodies) this reads a predetermined macro file that contains standard (Engh & Huber) coordinates for the amino acids found in natural proteins along with predetermined variable torsion angle definitions.

* Once a rigid body is defined you can plot it, change its name or manipulate any torsion angle to see the effect on the plot.
* The translation magnitudes in a vector rigid body can be refined allowing some lengths within a vector rigid body to be varied.
