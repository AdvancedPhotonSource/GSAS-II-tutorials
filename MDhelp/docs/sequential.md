# Sequential Refinement Results

This tree entry becomes available after a sequential fit has been run. Note there are the following types of sequential fits:

1. Rietveld: Sequential results
2. PDF: Sequential PDFfit2 results
3. Peak fit: Sequential peak fit results
4. Small angle: Sequential SASD fit results
5. Reflectometry: Sequential REFD results
6. Image (strain): Sequential strain fit results
7. Image (calibration): Sequential image calibration results 

Each sequential fitting process within GSAS-II will have its own differently named set of sequential results, as listed above. When any of these tree items is selected, the window tabulates the sequential fit results. The columns are the parameter names; the naming convention is generally 'p:h:name:n' where 'p' is the phase number,' h' is the histogram number, 'name' is the parameter name, and 'n' (if needed) is the item number (e.g. atom number). The rows are the data sets used in the sequential refinement.

For a sequential Rietveld refinement, set the PWDR histograms to be used in the sequential refinement in the Controls tree item. Note that the Calculate/Refine menu command will be renamed as "Sequential Refine." Since not all histograms need be used in a sequential Rietveld fit, after a sequential fit, histograms that have been fit will be included in the table. Previously fit histograms will not be removed unless the table is cleared (in the Controls tree item). In this way, a large sequential fit may be worked on in sections. The first column of the table will list the histogram number and the number will be shown in red if it was not fit in the last sequential refinement.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

* **Select a row** - a right mouse button will display the variance-covariance matrix for the refinement with that data set; a left mouse button will display its powder data fit.
* **Select a column** - this will display a plot of that parameter across the sequence of data sets. Error bars for each value are also shown. Selecting multiple columns (hold Ctrl key down for subsequent picks) will plot all as individual curves.

* Menu '**Columns/Rows**' -

    * **Set used** - this allows you to select in a dialog which entries to use; those not used are not plotted or used in further processing.
    * **Update phase from row** - this updates the phase parameters from the entries in the selected row. Normally the phase parameters at the end of a sequential fit are those obtained from the last histogram.
    * **Set phase vals** - same as previous except you can pick which parameters to update.
    * **Plot selected cols** - plots the selected columns (redundant as selecting the columns automatically plots them)
    * **Rename selected cols** - can change column names with this
    * **Save selected as text** - gives a txt file with columns of data from those selected.
    * **Save selected as CSV** - gives a comma separated values (CSV) file of selected columns.
    * **Compute average** - gives average(esd) for selected column values.
    * **Hide columns** - you can select/deselect columns to not show in table.
    * **Save all as CSV** - gives a CSV file for all table entries.

* Menu '**Pseudo Vars**' – this is used to create derived results from sequentially refined parameters; new columns are the result.

    * **Add Formula** - create a formula used to make a derived result.
    * **Add Distance** - adds a new column for a specific interatomic distance.
    * **Add Angle** - adds a new column for a specific 3-atom angle.
    * **Delete** - to remove a pseudo variable formula.
    * **Edit** - to change a selected formula.

* Menu '**Parametric Fit**' - this is used to create fitting models for any column of sequential results.

    * **Add equation** - add a parametric fitting equation. At the end of this step, it will be used to give refined values of the coefficients with esds based of a full error propagation from the variance-covariance matrices from the individual refinements.
    * **Copy equation** - make a copy of a parametric equation.
    * **Delete equation** - to remove a parametric equation.
    * **Edit equation** - to edit an equation.
    * **Fit to equation(s)** - do the fitting of the parametric equations to the data.
* Menu '**Seq export**' –
    * **Project as** - only choice is as a full cif file.
    * **Phase as** - either a "quick' cif or a CSV file
    * **Powder as** - either a powder pattern cif, a histogram CSV file or a reflection list CSV file.
    * **Save table as CSV** - same as Save all as CSV above.

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

By default, the plot shows the variation of the selected parameters across the sequence of histograms used in the sequential fit. Each point that was fitted shows as an x with a vertical bar indicating the standard error from the fit for that value. There are some key commands:

* Press 'l' – toggles display of connecting lines between the data points
* Press 's' – this presents a choice of parameters from the table columns to be used for the x-axis. Typically, this is used to show parameter variation with e.g. temperature.
* Press 't' – this provides access to all three titles of the plot.
