<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="Phase-ISODISTORT"></a>
# **ISODISTORT** phase tab

This displays the setup for using the web-based application, [ISODISTORT](https://iso.byu.edu/iso/isodistort.php), to identify the possible mode distortions of a parent structure. To use it you must be connected to the internet. Two ISODISTORT Methods are supported in GSAS-II: 

 * Method 1: identifies all possible subgroups that result from simple mode distortions that are associated with a single irreducible representation. 
 * Method 4: is more useful in that it finds the mode decomposition of a parent structure to give a specified distorted structure and is set up to find only atom displacement modes. 

See help pages for [ISODISTORT](https://iso.byu.edu/iso/isodistort.php) for more information. The ultimate product of using ISODISTORT is a special CIF file with constraints describing the mode distortions; this is imported into GSAS-II to form a new phase with these constraints.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

If this is a freshly created phase (not an imported ISODISTORT CIF) then you can choose the Method (4 is default) and select parent structure and distorted child structure (for Method 4).

If you chose Method 1 & run ISODISTORT, a table of possible substructures is displayed; a CIF file with mode distortion constraints can be produced from your selection. The table can be filtered by crystal class.

If this is a phase imported from an ISODISTORT CIF file, the mode displacements are shown with sliders to allow visualization of the displacements in a drawing of the crystal structure (prepare this first before trying a slider). A structure refinement using this phase will employ the mode distortions as constraints on the atom coordinates; there should be as many as there are free variable coordinates in the structure. The values (in Å) represent the largest atom shift associated with the mode; shown is a list of atom coordinates affected by each mode.

* **Operations** menu –

    * **Run ISODISTORT** – run this from the web site with the controls as shown.
    * **Make cif file** – active after table from Method 1 is displayed; generate CIF file by ISODISTORT web site with mode distortion constraints.
    * **Make PDFfit phase** – active when mode distortions are shown. Makes new phase specific for fitting PDF data via PDFfit2.
    * **Show modes** – active when mode distortions are shown. Displays mode names & values.
    * **Show relationships** - active when mode distortions are shown. Displays constraint equations associated with mode distortions.


