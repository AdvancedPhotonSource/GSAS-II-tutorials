<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="main_menu"></a>
# GSAS-II Main menu commands

The menubar has two types of entries. The "Main" menu commands, described here, are present regardless of what data tree entry is selected. In addition, most data tree items have menu items specific to that entry. Those menu commands are described with the data tree entry. 

<a name="File_menu"></a>
## **File** Menu

* **Open project...** <a name="openproject"></a> - 
Open a previously saved GSAS-II project file (files are named as &lt;project&gt;.gpx) from a file browser. Note that a native file browser is used on all platforms except Linux unless the [Configuration variable](./others.md#config) `G2FileBrowser` is set.
If you currently have a project file open, you are asked if you want to "Save &amp; Overwrite" as the contents of the current project may be lost in this operation. If you say "Yes" the current project will be saved before the next project is read; if you say "No" any changes to the current project will be discarded; "Cancel" will cancel the Open action, as if the menu command had not been entered.

    !!! Note
        Note that as files are saved during a structure refinement, copies of the previous version are saved as backup files, named as &lt;project&gt;.bak&lt;i&gt;.gpx, where &lt;i&gt; starts as 0 and is increased after each save operation. NB: you may open a backup .gpx file (e.g. &lt;project&gt;.bak3.gpx) to return to a previous version of your project, but if you do so, it is best to immediately use the Save As... menu command (you may wish to use the same named as before to overwrite the current version or select a new name.) If you forget specify a project name, then &lt;project&gt;.bak3 will be considered the project name and backups will then be named &lt;project&gt;.bak3.bak0.gpx, etc.

* **Open in new window...** - Open a previously saved GSAS-II project file without closing the current project. 

* **Reopen recent...** - Provides a list of recently used GSAS-II project file that can be opened. Otherwise behaves the same as [**Open project**](#openproject).  
 
* **Open w/project browser.** - Opens a special file browser for GSAS-II .gpx files that shows some information about the status of the last refinement in that file. Useful where many different versions of a fit have been tried on the same or similar data. Otherwise behaves the same as [**Open project**](#openproject). 

* **Save project** - Save the current project. If this is a new project that has not yet been saved, you will be prompted for a new name in a file dialog (you may optionally change the directory in that dialog). If the file exists, you will be asked if it is OK to overwrite it. Once a file name has been used to read or save a project, the name is shown after 'Loaded Data:' in the first item in the data tree.
* **Save Project as...** - Save the current project in a specified project file. You will be prompted for a new name in a file dialog (you may optionally change the directory in that dialog). If the file exists, you will be asked if it is OK to overwrite it. The current project will be now named as the saved project name.
* **New Project** - Creates a new empty project. You will be given a chance to save the current version of the open project. If not saved, any changes made to the current project since the last save will be discarded. 
* **Preferences** - Provides access to GSAS-II configuration settings, as described in the [Configuration variables](./others.md#config) description. 
* **Install GSASIIscriptable shortcut** - Modifies the current Python installation so that [GSASIIscriptable](https://gsas-ii-scripting.readthedocs.io/en/latest/GSASIIscriptable.html) can be accessed without providing a full path, as discussed in the 
[Scripting docs](https://gsas-ii-scripting.readthedocs.io/en/latest/GSASIIscriptable.html#install-gsasiiscriptable-location-into-python).

* **Quit** - Exit the GSAS-II program. You will be asked if the project should be saved or not (Cancel aborts the quit). You can also exit GSAS-II by pressing the red X in the upper right (Windows) or left (Mac). Pressing the red X on the [console window](./applicationwindow.md#Console) will kill the GSAS-II run without any save.

If the [Configuration variable](./others.md#config) `debug` is set to `True` these menu items will also be included in the file menu:

* **IPython console** - Opens a iPython debugging session; requires that the IPython package be installed into the current Python interpreter. 
* **wx.inspection tool** - Open the wxPython window inspection debugging tool.
* **Reopen current** - Rereads the current .gpx file, discarding any changes that have been made but not saved. 

<a name="Data_menu"></a>
## **Data** Menu

* **Read Powder Pattern Peaks...** - Read in a list of powder pattern peak positions as either a d-spacing or 2\(\theta\) position table; these can be used in GSAS-II powder pattern indexing. They are distinguished by their order (highest d or smallest 2\(\theta\) first in table).
* **Sum or average powder data** - Forms the sum of previously read powder patterns (PWDR tree entries); you can supply a multiplier for each. Can be used to accumulate data, subtract background/sample-container patterns, etc. Patterns used to form the sum must be of identical range and step size. Result is a new PWDR entry added to the GSAS-II data tree.
* **Sum image data** - Form the sum of previously read 2-D images; you can supply a multiplier for each. Can be used to accumulate data, subtract background/sample-container patterns, etc. Images used to form the sum must be of identical size and source. Result is a new IMG entry in the GSAS-II data tree, and a GSAS-II image file is written for future use as a Python pickle file.
* **Add new phase** - This begins the creation of a new phase in the data tree (under Phases). You are first prompted in a dialog box for a name to be assigned to the new phase. Then the Phase/[General](./phasegeneral.md) tab is opened for this new phase, where you should first select the phase type, then enter the space group symbol 
and then the lattice parameters.
Finally, move to the atoms tab where atoms can be inserted or imported. Note that inserted atoms are labeled as H atoms. You must edit the atom to set the element type and the coordinates. 

    !!! Note
        Nonstandard space group symbols (such as "F 21 21 21") are permitted in GSAS-II and are sometimes to be preferred, but to be recognized correctly, space group names must have spaces between the axial fields (e.g. use 'P n a 21' not 'Pna21'). Standard space groups names will be parsed properly even when spaces are not provided, but this is not done with non-standard space group names. Also note that GSAS-II requires that space groups use the "Origin 2" setting for centrosymmetric space groups where that choice is offered. Origin 2 puts the centre of symmetry at the origin and forces structure factors to real rather than complex numbers. 

* **Delete phase entries** - This will remove a phase from the data tree. A dialog box will present the list of phases; pick one (or more) to delete.
* **Rename tree entry** - Rename a histogram entry. This should only be done before the histogram is used in any phases: e.g. only rename data immediately after reading.
* **Delete data entries** - This will remove a data (e.g. PWDR) item from the data tree. A dialog box with a list of choices for histograms is presented; it has filter capability to ease this process. Be sure to remove histograms from all phases before deleting them from the tree.
* **Delete plots** - This will remove plots from the plot window. A dialog box with a list of choices for plots is presented.
* **Delete sequential result entries** - This will remove any sequential results from the tree. A dialog box with a list of choices for entries is presented.
* **Expand tree item** - This will show child entries for specified type of items (IMG, PWDR, etc.)
* **Move tree item** - Move classes of Tree items (IMG, PWDR, Phase, etc.) around in the tree. Individual top-level tree items can be moved using the right mouse button.

<a name="Calculate_menu"></a>
## **Calculate** Menu

* **Setup PDFs** - This is the first step in computing a pair distribution function (PDF). This creates the controls for each powder pattern selected in the dialog box, but does not compute the PDF, which must be done from [PDF tree entries](./pairdistribution.md). See [PDF Controls](./pairdistribution.md#PDF_Controls)  for information on the PDF input.

* **View LS parms** - This shows a dialog box where the status and value of every parameter used in your project can be viewed. The parameter names are of the form `p:h:name:id` where 'p' is the phase index, 'h' is the histogram index and 'id' is the item index (for atoms). 'name' indicates the type of parameter, as [defined in developer's docs](https://gsas-ii.readthedocs.io/en/latest/objvarorg.html#parameter-names-in-gsas-ii). Indexes all begin with '0' (zero). The total number of refined parameters is shown at the top of the list. Optionally only those parameters that are refined can be viewed. The "Ref" column shows a "R" for parameters that are refined; a "C" for parameters where values are generated from a constraint. If shown as blank, the parameter value is fixed. 

    Clicking on a row of the table brings up a window where **parameter limits** may be set. One may set a lower limit value, an upper limit value or both. When a parameter value refines to value outside the limit, the parameter is set to that limit value and the refinement flag for the parameter is subsequently ignored. 

Also, one can set here parameters that will be logged into the [Notebook](./commontreeitems.md#Notebook), so the values can be tracked and plotted across a refinement. 
Right-click to toggle the log setting. Note that individual log
settings will override the the `LogAllVars` preference setting (see  [Configuration variables](./others.md#config)).


    !!! Note
        Note that for atom positions, the variables associated with coordinate values (named as `p::Aw:n`, where p is the phase number, n is the atom number and w is x, y or z) is not a refinable parameter, but the shift in the value is. The refined parameters are 'p::dAw:n'. The reason this is done is that by treating an atom position as (Ax+dAx,Ay+dAy,Az+dAz) where the “d” values indicate shifts from the starting position. Shifts are refined rather than the x, y, or z values as this this simplifies symmetry constraints. As an example, suppose we have an atom on a symmetry constrained site, `x,1/2-x,z`. The process needed to enforce this symmetry constraint, so that if x moves positively y has to move negatively by the same amount would be messy. With refinement of shifts, all we need to do is constrain the dAy to be equal to the negative of dAx (`0::dAy:n = -1 * 0::dAx:n` ).

* **Refine (Sequential refine)** - This performs the refinement (Pawley/Rietveld/LeBail or single crystal) fit according to the controls set in the Controls data tree item. This menu item name will be "Refine" unless the datasets to be used in a sequential refinement have been selected in the [Controls data tree](./commontreeitems.md#Controls) item, at which point the name will appear as "Sequential refine".

    When a PWDR histogram item is selected in the data tree, or a child tree item of a PDWR histogram is selected in the tree when Refine is used, the plot of that histogram will be updated after each cycle of refinement.
    
    Once the refinement is completed, you will be offered the chance to load the results of the fit or to reject the fit,in which case no parameters will be changed, so it is possible to change settings or refinement flags and try different options. After the refinement results are reloaded, plots will be updated to reflect the new refinement values if the plot has a defined update process or will be closed as the plot contents are presumed to be obsolete and need to be manually recreated to be valid.
* **Compute partials** - 
The term "phase partial intensities" is used to designate keeping separate track of the intensity contribution from each phase separately. When this is used, a zero-cycle refinement (meaning no parameters values are changed) where the contributions from each phase (phase partial intensities) are written for each histogram and each phase in that histogram into a single file named &lt;project&gt;`.partials` where &lt;project&gt; is the GSAS-II project (.gpx) name. This file is intended for internal use in GSAS-II and will be deleted if additional refinements are performed (as the information in them is then obsolete; use this menu command to recreate them if needed.) When the .partials file is created, the user can then choose to export the intensity information in a series of ASCII files named &lt;project&gt;_part_N.csv, which can be read by spreadsheets and most scientific software.
* **Parameter impact** - This shows the parameters that will have the greatest improvement to the reduced \(\chi^2\) for the fit if refined. See [Toby, JAC 57, 175-180 (2024).](https://doi.org/10.1107/S1600576723011032)
* **Evaluate Expression and s.u.** - This allows an expression to be entered based on multiple GSAS-II parameters that computes a value and its standard uncertainty. The uncertainty computation will use the covariance matrix and thus accounts for correlation or anti-correlation in the parameters. An example for how this might be used would be for computing the total amount along with uncertainty for an element that occurs with several refined occupancies. 
* **Setup Cluster Analysis** - Uses unsupervised machine learning to group PWDR entries into groups (clusters) that share the most similarity. See the [tutorial on this](https://advancedphotonsource.github.io/GSAS-II-tutorials/ClusterAnalysis/Cluster%20and%20Outlier%20Analysis.htm) for more information. 
* **Run Fprime** - This run the utility routine Fprime, which displays real and imaginary components of the x-ray form factors for user-selected elements, as a function of wavelength/energy. Allows for an informed choice of wavelength for resonant x-ray scattering experiments
* **Run Absorb** - This runs the utility routine Absorb that displays the x-ray absorption for a user selected sample composition as a function of wavelength/energy. Allows determination of the maximum sample size before absorption corrections are needed or where diffraction intensities will be severely reduced by x-ray absorption. 
* **Run PlotXNFF** - This runs the utility routine PlotXNFF which displays the x-ray, neutron, electron and magnetic form factors for a selected element. This imcludes
resonant (if any) neutron scattering lengths for all isotopes of a selected element. It also displays the x-ray and magnetic neutron form factors for all valences (if any) for this element.

<a name="Import_menu"></a>
## **Import** Menu

A special set of modules, known as importers, is used to read information into GSAS-II 
from external files. The importers that are found by GSAS-II at runtime are used to configure the import menus. Import modules are usually fairly easy to create and thus new formats are relatively easy to support. See the [GSAS-II Import Modules](https://gsas-ii.readthedocs.io/en/latest/imports.html) section of the Programmers documentation for more information on this. Note that most menus include a "**guess format from file**" option. This attempts to determine the file format by matching the file extension and a cursory examination of the file contents to the importer(s) to be tried. On occasion, this command may not succeed in correctly determining a file format. If it fails, retry by selecting the correct format from the list.

While we are not able to reproduce this, with some locale settings (particularly CJK ones?), GSAS-II will not be able to read UTF-8 files that have a BOM (Byte Order Mark). If you find that you are unable to read a data file in GSAS-II, you may wish to try stripping the BOM from the file. 

* **Image** - Read in one or more 2D powder diffraction images (multiple patterns can be selected). A submenu appears with choices for import of data. Each entry when selected with the mouse shows further submenus with specific imports that are available. Any of these files can be accessed from a zip file. GSAS-II can read many different image file formats including MAR345 files, Quantum ADSC files, and tiff files from Perkin-Elmer, Pilatus, and GE. See the [image importers code docs](https://gsas-ii.readthedocs.io/en/latest/imports.html#image-importer-routines) for a full list of the supported formats. Although many of these formats have data fields that should contain important information for the measurement (e.g. wavelength), these are rarely filled in correctly by the data acquisition software. Thus, you should have separately noted this information as it will be needed. In some cases, this information may be in a separate “metadata” file; GSAS-II will look for this and attempt to open it as well as the image file.

    !!! Note
        gain maps can be imported but they must be integer values as 1000*the gain value (where the gain is typically ~1); if a gain map is used, GSAS-II will rescale the gain map by 1/1000 and apply it to the image.

* **Phase** - Creates a new phase by reading unit cell/symmetry/atom coordinate information. GSAS-II can read information from several different format files; see the [phase importers code docs](https://gsas-ii.readthedocs.io/en/latest/imports.html#phase-importer-routines)
for a full list of the supported formats. In all cases, after selecting an importer, a file open dialog is opened to locate the file. If the selected file has more than one phase, a dialog is shown with the choices; only one can be chosen. To import more than one phase from a .EXP file, repeat the import command. After selecting a phase, a dialog box is shown with the proposed phase name. You can change it if desired. 

    Some notes on more commonly used formats are below. Other formats currently available for import include JANA .m50, ICDD .str & RMCProfile .rmc6f files.

    * **GSAS.EXP** - This reads one phase from a GSAS/EXPGUI (old) experiment file (&lt;name&gt;.EXP). 
    * **PDB file** - This reads macromolecular phase information from a Protein Data Base file (&lt;name&gt;.PDB or &lt;name&gt;.ENT). Be careful that the space group symbol on the 'CRYST1' record in the PDB file follows the GSAS-II conventions (e.g. with spaces between axial fields). 
    * **CIF file** - This reads one phase from a Crystallographic Information File (&lt;name&gt;}.CIF (or &lt;name&gt;.cif). 
    * **GSAS-II .gpx file** - This reads one phase from a GSAS-II project file (&lt;name&gt;.gpx). 
    * **SHELX ins & res** - note that SHELX files do not contain the space group symbol; you must set it on the new phase's General tab after import.

* **Powder Data** - Reads a powder diffraction data set in a variety of formats. Results are placed in the GSAS-II data tree as 'PWDR &lt;filename&gt;'. After selecting an importer, a file open dialog is opened to locate the file. If the selected file has more than one histogram (dataset), a dialog is shown with the choices; multiple datasets can be selected. 

    Information needed for processing a powder diffraction data set, such as data type, calibration constants (such as wavelength) and default profile parameters and after most importers are run a second  file open dialog is opened to locate a separate instrument parameter file with this information. This may be a GSAS/EXPGUI (old) instrument parameter file (file extension is usually `.prm`, `.ins` or `.inst`) or a GSAS-II created file, with extension `.instparm`. If no instrument parameter file is available, press the "Cancel" button on the file open dialog and you will be offered some default options that may be a good starting point, but ideally will be used to perform a calibration and a .instparm file with appropriate instrumental terms will be created. (See the ["Create Instrument Parameter File..." tutorial](https://advancedphotonsource.github.io/GSAS-II-tutorials/CWInstDemo/FindProfParamCW.htm).)

    !!! Note
        Note that It is possible to apply systematic changes to the 2\(\theta\), intensity or weight values. This is done by adding a Python command(s) to the instrument (.instprm) parameter file. See [here for an example](./others.md#CorrectionCode). 

    * **CIF file** - This reads one powder pattern (histogram) from a Crystallographic Information File (&lt;name&gt;.CIF). 
    * **GSAS-II .gpx file** - This reads powder patterns from a previously created GSAS-II gpx project file.
    * **GSAS .fxye files** - This reads powder patterns (histograms) from the powder data file formats used in the GSAS/EXPGUI (old) program. GSAS file types of STD, ESD, FXY and FXYE are recognized. Neutron TOF data with a 'TIME-MAP' are also recognized. Note that for CW data, 2\(\theta\) values are in "centidegrees" (degrees*100).
    * **TOPAS .xye files** - This format is a simple 3-column (2-theta, intensity & \(\sigma\)) text file. 
    * **other supported formats** - Bruker .brml & .RAW; FullProf .dat; Panalytical .xrdml; Comma-separated .csv; Rigaku .ras & .txt. See the [powder data importers code docs](https://gsas-ii.readthedocs.io/en/latest/imports.html#powder-data-importer-routines)
for a full list of the supported formats. 

    Note that this menu contains three separate "special" import items:

    * **Simulate a dataset** - This creates a histogram with initially all zero intensity values that will be filled with calculated intensity values later, when the Calculate/Refine menu command is used. The user will specify the range of data to be used (2\(\theta\) or TOF) and the instrument parameters to be used in the computation. One or more crystalline phases must assigned to the histogram to perform a crystallographic simulation. When the "Refine" menu command is initially used, the intensities are computed from these phases and both the "observed" and "calculated" intensity values are set from these computed values, with superimposed "random" noise added to the "observed" where the variance in intensity is computed with \(\sigma = \sqrt(I)\). (N.B. to decrease the impact of the noise, increase the histogram scale factor.) Once Refine is used, the "observed" values are not changed, but the "calculated" values will change based on the current instrument, sample and phase parameters. To reset the "observed" intensity values back to zero and recompute them, use the "Edit range" button on the "PWDR" tree item.

    * **Auto Import** - This brings up a window that reads in powder diffraction files as they are added to a directory. The file extension must determine the importer that will be used and a filter pattern is specified to determine which files will be read (e.g. use "*June23*.fxye" so that only files that contain the string "June23" will be read.

    * **Fit Instr. profile from fundamental parms...** -
<a name="FPA_menuitem"></a>
This option is used to compute instrument parameters from a set of fundamental parameters that describe a constant wavelength (most likely Bragg-Brentano) powder diffraction instrument. The user must first specify the data range to be used and then a set of FP (fundamental parameter) values. The FP values and a source spectrum can be supplied using a nomenclature similar to Topas and [described separately](./others.md#FPA). They will then be converted to the SI units and parameter names used in the NIST FPA code. Alternately a file can be supplied with the parameter values used directly in that program. With this input, a series of peaks are computed across the specified data range and the Instrumental Parameters that determine the instrumental profile (U, V, W, X, Y and SH/L) are determined from those peaks. These values are then saved in an instrument parameter file that can be used when reading in new datasets or for pattern simulation. 

* **Structure Factor** - Creates a new single crystal data entry (histogram) from a variety of file types. Results are placed in the GSAS-II data tree as "HKLF &lt;filename&gt;". Note that since it cannot be determined if SHELX format `.hkl` contains \(F\) or \(F^2\) values, do not use "guess format from file" with SHELX format files. Information on some supported formats is provided below. There are also specific importers for incommensurate or twinned single crystal data as well as data from specific neutron diffractometers.
See the [Single crystal importers code docs](https://gsas-ii.readthedocs.io/en/latest/imports.html#single-crystal-data-importer-routines)
for a full list of the supported formats.
    * **HKL F file** - This reads structure factors [as \(F\) and  \(\sigma(F)\) values] from a SHELX format .hkl file. You must know the file contains structure factors (as F values), as the file itself has no internal indication of this.
    * **HKL F\*\*2 file** - This reads squared structure factors [as \(F^2\) and  \(\sigma(F^2)\) values]. You must know the file contains squared structure factors (\(F^2\) values), as the file itself has no internal indication of this.
    * **CIF file** - This reads structure factors from a CIF `.CIF`/`.cif` or `.FCF`/`.fcf` format file.  The CIF data names indicates which form of structure factors (\(F\) or \(F^2\) values) are supplied.
    
* **Small Angle Data** - Reads small angle scattering data from files. Results are placed in the GSAS-II data tree as 'SASD &lt;filename&gt;'. The data are in 'QIE' form as q-stepped data of intensities in 2 columns or optionally with \(\sigma(I)\) in 3 columns. Data may be preceded by comment records. Importers are for x-ray or neutron data with q in \(Å^{-1}\) or \(\rm nm^{-1}\); data will be stored in \(Å^{-1}\). The data type is either 'LXC' or 'LNC' (for X-ray and neutron, respectively). 

* **Reflectometry Data** - Reads x-ray or neutron reflectometry data from files. Results are placed in the GSAS-II data tree as 'REFD  &lt;filename&gt;'. The data are in 'QIE' form as q-stepped data of intensities in 2 columns or optionally with \(\sigma(I)\) in 3 columns. The data are in 'QIE' form as q-stepped data of intensities and optional sig(I) as 3 (or) 2 columns. 
Data may be preceded by comment records. The data type is either 'RXC' or 'RNC' (for X-ray and neutron, respectively)

* **Powder Peak Position Data** - Reads ordered peak positions as \(2\theta\) or d-spacing from .txt files. Results are placed in the GSAS-II data tree as 'PKS  &lt;filename&gt;'. The data format consists of optional comments (each line starts with '#') followed by positions in a single column. Peak positions must be sorted and their order indicates if the values are \(2\theta\) or d-spacing. If the position of the first peak is larger than the last peak, they positions are interpreted as d-spacings, otherwise as \(2\theta\). A second column of intensities is optional.
* **PDF G(R) Data** - Reads pair distribution data for possible analysis by PDFfit from within GSAS-II.

<a name="Export_menu"></a>
## **Export** Menu

A special set of modules, known as exporters, is used to write information from GSAS-II 
to external files. The exporters that are found by GSAS-II at runtime are used to configure the export menus. Export modules are usually fairly easy to create and thus new formats are relatively easy to support. See the [GSAS-II Export Modules](https://gsas-ii.readthedocs.io/en/latest/exports section of the Programmers documentation for more information on this.

* **Entire project as** - At present there are several supported formats for all information in a GSAS-II project. One is a full CIF file, which brings up a separate window where information such as ranges for bond distances and angles can be selected. Note that when a project contains more than one histogram or phase, a multiblock CIF must be created. Two `.csv` (column-separated-value) forms suitable for cutting/pasting into manuscripts or creating spreadsheets. The "bracket notation" uses crystallographic notation [e.g. 1.234(5) indicates a value of 1.234 with a standard uncertainty of 0.005] and the other `.csv` format places standard uncertainty values in a separate column. The JSON "dump" provides a sort-of human readable (ASCII) version to the contents of a project (`.gpx`) file. GSAS-II cannot at present read anything from this file. 

* **Phase as** - The contents of a phase (unit cell, space group, coordinates, etc.) can be exported in a variety of formats, including a simplified CIF file that contains only the unit cell, symmetry and coordinates.

* **Powder data as** - Powder data can be exported in number of formats. Note that this menu can also be used to export reflection lists from Rietveld and Pawley fits.

* **Small angle data** - This is exported only as a csv text file.

* **Reflectometry Data** - This is exported only as a csv text file.

* **Single crystal data as** - Single crystal reflection lists can be exported as text files or as a simplified CIF file that contains only structure factors.

* **Image data** - This exports selected images as a portable networks graphics format (PNG) file. Alternately, the image controls and masks can be written for selected images. If strain analysis has been performed on images, the results can also be exported here as a spreadsheet (.csv file).

* **Maps as** - Fourier maps can be exported here.

* **Export all Peak Lists...** - This allows peak lists from selected powder histograms to be written to a simple text file. There will be a heading for each PWDR GSAS-II tree item and columns of values for position, intensity, sigma and gamma follow.

* **Export HKLs** - This allows single crystal reflection lists from selected histograms to be written to a file.

* **Export MTZ file** - This exports macromolecular structure information in a commonly recognized format for input to other macromolecular packages.

* **Export PDF...** - This allows computed PDFs peak lists from selected histograms to be written as two simple text files, {name}.gr and {name}.sq, containing g(r) and S(Q), respectively as 2 columns of data; a header on each indicated the source file name and the column headings. The file is named based on the name of the PDF entry in the GSAS-II data tree.

<a name="Help_menu"></a>
## **Help** Menu

The help menu offers access to this documentation, the GSAS-II tutorials, as well as options to select the version of GSAS-II that is used. Note that the update, regress and switch options will appear as inactive (greyed out) if you do not have write access to the directory where GSAS-II is installed and will not appear in the menu if the git program needed to make updates is not available to GSAS-II.

* **Check for updates** - When GSAS-II starts, if Internet access is available, a check is made to see if newer versions of GSAS-II are available. If so, it is downloaded as a background task. This menu command will check to see if a newer version has been downloaded and will offer the choice to install that. While it is not necessary to update GSAS-II every day (in fact on some days there may be multiple updates provided) it is recommended that updates be made at least monthly. Please do not [report a bug](https://advancedphotonsource.github.io/GSAS-II-tutorials/bug.html) in GSAS-II without first updating to the most recent version. 

* **Regress to old GSAS-II version** - This allows the GSAS-II version to be set back to an older version. This might be useful to confirm that a result obtained previously is reproduced in the latest code or to avoid a bug that has inadvertently been introduced.
Note that if there is some aspect of a newer version of GSAS-II that needs to be avoided, please report this, preferably by  [creating a new GitHub issue](https://github.com/AdvancedPhotonSource/GSAS-II/issues) or at least post this on [the GSAS-II mailing list](https://advancedphotonsource.github.io/GSAS-II-tutorials/mailinglist.html). The likelihood is that the feature you like will be lost or the bug you found will not be addressed, if not reported

 * **Switch to/from branch** - On occasion the GSAS-II developers will create trial versions of GSAS-II to try out new ideas or test changes before they are incorporated into the "main" release. These trial versions are called branches. Use this if working with the developers to test out a feature available in a test branch. This only appears in the menu the [Configuration variable](./others.md#config) `debug` is set to `True`.
 
<a name="Help_addpkgs"></a>
* **Add packages for more functionality** - 
GSAS-II runs in Python and requires [several Python packages](https://gsas-ii.readthedocs.io/en/latest/packages.html#python-requirements) as well. Additional [Python packages are optional](https://gsas-ii.readthedocs.io/en/latest/packages.html#python-requirements), but sections of GSAS-II will not operate without them (as an example, to read Bruker `.brml` files, a package for interpreting XML, *xmltodict* is used. If this has not been installed, the  Bruker `.brml` importer cannot be run. As GSAS-II runs, it makes note of optional Python packages that are not present but could be useful. This menu command can be used to install those packages. If there are no uninstalled optional packages, this option will be greyed out. 

* **Tutorials** - GSAS-II offers more than 50 tutorials on different aspects of the program. If this menu command is used, one see a list of tutorials, select to view a tutorial, optionally downloading the input files needed to run the tutorial.

* **Help on GSAS-II** - Opens an index file to these web pages with GSAS-II documentation.

* **Help on current data tree item** - Opens this GSAS-II documentation for the currently selected data tree item. A yellow help button on each section of the GUI will perform the same action. 

* **Citation information** - If you use GSAS-II please cite Toby, B. H., & Von Dreele, R. B. (2013). “GSAS-II: the genesis of a modern open-source all purpose crystallography software package”. * Journal of Applied Crystallography*, **46**(2), 544-549. doi:10.1107/S0021889813003531, but there are many specialized features of GSAS-II that utilize other's software that should also be cited. This menu item provides a list of all the works that one may want to consider citing through use of GSAS-II. 
