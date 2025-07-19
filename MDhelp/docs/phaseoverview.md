<a name="Phase"></a>
#  Overview on phase data tree entries

Phases are placed in their own section of the [GSAS-II data tree](./applicationwindow.md#Data_tree) as subentries under the "Phases" entry. Note that there are no limits to how many phases may be placed in a GSAS-II project (`.gpx` file), other than as limited by available computer memory. Also, phases are only used in refinements when they are linked to histograms (datasets) so there is very little 
"cost" connected to including a phase that is not in use.

Phases are either created with the Data/"Add new phase" menu item (manual input) or are read in using the Import/Phase menu items. After a phase is imported, if there are histograms (datasets) present in the project, you will be offered a chance to link the imported phase to the previously imported histogram(s). Likewise, if histograms(s) are imported when phase(s) are already present, you will also be asked to link the new data to existing phases. It is also possible to link histograms to a phase later by selecting that phase in the data tree and then selecting the "Data" tab and finally using the "Edit Phase"/"Add powder histograms" menu command. 

When a phase is selected from the data tree, parameters are shown for that selected phase in a tabbed window. Clicking on each tab raises the windows as documented in subsequent sections of the help documentation. The tabs are:

 - [General](./phasegeneral.md)

