<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="PKS"></a>
#  Type **PKS** data tree entries: Powder Diffraction Peaks 

Powder diffraction peaks are read with the Data/"Read Powder Pttern Peaks" menu command. 
Powder peaks can only be used for indexing of the peak positions for possible unit cells.

<a name="PKS_Comments"></a>
## Comments

This window shows whatever comment lines (preceded by "#") found when the peaks data file was read by GSAS-II. If you are lucky, there will be useful information here (e.g. sample name, date collected, wavelength used, etc.). If not, this window will be blank. The text here is read-only.

<a name="PKS_Limits"></a>
## Limits

This window shows the limits in position to be used in indexing from these peak positions. The 'original' values are obtained from the minimum & maximum 1st & last position. The 'new' values determine the range of data that will be used in fitting. Units are $2\theta$.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

You can change the "new" values for Tmin and Tmax as needed. Change the upper and lower Tmin values by clicking on the appropriate vertical line and dragging it to the right or left or by typing values into the data window.

### Menu "**Edit Limits**" contents

* **Copy** - this copies the limits shown to other selected powder patterns. If used, a dialog box (Copy Parameters) will appear showing the list of available peaks list patterns, you can copy the limits parameters to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.

<a name="PKS_Instrument_Parameters"></a>
## Instrument Parameters

This window shows the relevant instrument parameters for a peaks list; namely a wavelength and zero needed to relate d-spacing to 2θ. Neither are refinable.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. Menu '**Operations**' – (many are irrelevant & will probably be removed at some point; only useful ones will be mentioned below).

    * **Reset profile** – resets the values for the instrument parameters to the default values shown in parentheses for each entry.
    * **Load profile...** - loads a GSAS-II instrument parameter file (name.instprm), replacing the existing instrument parameter values. All refinement flags are unset.
    * **Save profile...** - saves the current instrument parameter values in a simple text file (name.instprm); you will be prompted for the file name – do not change the extension. This file may be edited but heed the warning to not change the parameter names, the order of the parameter records or add new parameter records as this will invalidate the file. You may only change the numeric values if necessary. You can change or add comment records (begin with '#').
    * **Copy** – this copies the instrument parameters shown to other selected powder patterns. If used, a dialog box (Copy parameters) will appear showing the list of available powder patterns, you can copy the instrument parameters to any or all of them; select 'All' to copy them to all patterns. Then select 'OK' to do the copy; 'Cancel' to cancel the operation.

2. You can change any of the instrument coefficients

<a name="PKS_Index_Peak_List"></a>
## Index Peak List

This window shows the list of peaks that will be used for indexing (see Unit Cells List). It was filled when the import of the peaks list was done. It shows $2\theta$ position as input or calculated from provided d-spacing and wavelength given in Instrument Parameters. Note that peaks from a neutron TOF pattern could be entered here as d-spacings in descending order and a suitable wavelength used in the Instrument Parameters. When indexing is completed, this display will show the resulting hkl values for every indexed reflection along with the calculated d-spacing ('d-calc') for the selected unit cell in Unit Cells List.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

1. You may deselect individual peaks from indexing by unchecking the corresponding 'use' box.

<a name="PKS_Unit_Cells_List"></a>
## Unit Cells List

This tree item has several purposes, it can be used to perform autoindexing and it can be used to show the positions of peaks from unit cells which may be results from autoindexing or may be entered from a phase or manually. It can be used to refine unit cell parameters. It can also be used to search for cells/symmetry settings related to a specified unit cell & space group.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

**For autoindexing**, the peaks in the Index Peak List are used. Select one or more Bravais lattice types to use and use the "Cell Index/Refine"/"Index Cell" menu command to start indexing. Output will appear on the console and a progress bar dialog will appear which tracks trial volume. A Cancel button will terminate indexing; it may need to be pressed more than once to fully terminate the indexing process. Console output shows possible solutions with a computed M20 for each; good solutions are indicated by high M20 values. X20 gives number of unindexed lines out of the 1st 20 lines and Nc gives total number of reflections generated for each solution.

The "Copy Cell" menu command copies a selected solution to the Unit cell values; the Bravais lattice shown for the choice is copied. Press **Show hkl positions** to generate the allowed reflection positions, which are visually superimposed on the displayed powder pattern to visually confirm the indexing. Pay particular attention to any unmatched peaks in the pattern. A Space group can be selected from the pulldown box to remove reflections based on space group extinctions and visually eliminate possibilities.

* Max Nc/Nobs: – this controls the extent of the search for the correct indexing. This may need to be increased if an indexing trial terminates too quickly. It rarely needs to be changed.
* Start Volume: – this sets an initial unit cell volume for the indexing. It rarely needs to be changed.
* Select "keep" in the table for a cell that should be preserved when an additional indexing run is tried; all without that are erased before the indexing trial begins.

**To display a unit cell**, optionally with space group extinctions, set a Bravais class  (see [list](./powdercells.md#Laue_List)) to determine a unit cell type, optionally select a space group (by default the highest symmetry space group for the class is selected) and enter the unit cell parameters. Or use the "Cell Index/Refine"/"Load Phase" menu command to read this information from a phase that has been read into a project or from a file (such as a CIF) using the "Cell Index/Refine"/"Import Cell" menu command.

**For symmetry exploration**, once a phase/cell has been loaded, use the "Run SUBGROUPS", "Cell Symmetry Search" or "Run k-SUBGROUPSMAG" commands from the "Cell Index/Refine" menu. These commands look for: subgroups, lower symmetry cells or magnetic subgroups, respectively. Also note the "Transform Cell" command in that menu that can perform many common lattice transformations, apply a user-supplied cell transformation or create a magnetic phase.

**To optimize a cell**, to fit the peaks in the Index Peak List, use the "Cell Index/Refine"/"Refine Cell" menu command. The results will be placed in the Indexing Result table with 'use' selected.

**Other**: The "Make new phase" command creates a new phase from the selected unit cell and chosen space group. A dialog box will appear asking for a name for this phase. See the new entry under Phases and the new lattice parameters will be in the General window for that phase.
