<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="PDF"></a>
#  Type **PDF** data tree entries: Pair Distribution Functions

A PDF entry is created from a powder histogram (PWDR entry) using the [Setup PDFs entry in the Calculate menu](./mainmenu.md#Calculate_menu). Alternately, a PDF entry can also be imported as G(r) from a file. When this item is selected, the S(Q) function or G(r) function (if imported) is plotted, see below.
The main PDF data tree item displays the same window as the PDF Controls, below. 

<a name="PDF_Controls"></a>
## PDF Controls

This window provides parameters for computing the pair distribution function [PDF, G(r)] from the I(Q) function. This can only be done when a chemical formula and appropriate control values are provided. If so, clicking on this menu item causes the I(Q), S(Q), F(Q) and G(r) functions to be plotted, as described below.

The **Optimize PDF** button can be used to refine the values of the "Flat Bkg", "Background ratio" and "Ruland width" parameters to best agree with the \(-4*\pi*r\) line that is plotted for r < Rmin. Rmin should be set to a distance below the shortest expected interatomic distance for the material. 

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

The PDF parameters can be changed, triggering recomputation of the I(Q), S(Q), F(Q) and G(r) functions.

Available menu commands are:

* **Add element** - Adds a new element to the chemical formula by clicking on a periodic table. Note that the number of atoms of this type in the empirical formula must still be entered.
* **Delete element** - Removes a previously-entered element from the chemical formula.
* **Copy Controls** - Copies the current PDF control values to other PDF data entries
* **Load Controls** - Replaces the current PDF control values with values read from a file (see Save controls).
* **Save Controls** - Saves the current PDF control values into a file.
* **Compute PDF** - Recomputes the PDF for the current entry. This is usually done automatically when values are changed, but if not, this can be forced with this menu item.
* **Compute all PDFs** - Recomputes the PDFs for all selected PDF entries. This is usually done after Copy Controls is used. By default, PDFs are optimized to reduce the low G(r) region, but this can be turned off.

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

When a chemical formula and appropriate control values are provided, clicking on this menu item causes the I(Q), S(Q), F(Q) and G(r) functions to be plotted, as described separately, below. 

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

For each of the plots, the following keyboard shortcuts are available:

* **c: contour on/off** - if multiple PDFs are available, then a contour plot is shown for the displayed function. All data sets must be the same length as the first one to be included in the contour plot.
* **m: toggle multiple plot** - for multiple PDFs, this will show only the one selected from the data tree. The offset options are not active. Or all selected items will be plotted on a single axis.
* **s: toggle single plot** - for multiple PDFs, this will show only the one selected from the data tree. The offset options are not active. Or all selected items will be plotted on a single axis.
* **f: select data** - Allows only some PDFs to be plotted, rather than all.
* **t: toggle legend** - provides a legend with the line type and name for each PDF.
* **l: offset left** - for a waterfall plot of multiple powder profiles, increase the offset so that later plots are shifted more to the left relative to previous plots.
* **r: offset right** - for a waterfall plot of multiple powder profiles, increase the offset to the right (or decrease the left offset.)
* **d: offset down** - for a waterfall plot of multiple powder profiles, increase the offset down.
* **u: offset up** - for a waterfall plot of multiple powder profiles, increase the offset up.
* **o: reset offset** - for a waterfall plot of multiple powder profiles, reset to no offset. 

<a name="PDF_I_Q"></a>
## I(Q) Function

This shows the I(Q) function. 
See the [PDF Controls](#PDF_Controls) for information on menu commands and plot options.

<a name="PDF_S_Q"></a>
## S(Q) Function

This shows the S(Q) function. 
See the [PDF Controls](#PDF_Controls) for information on menu commands and plot options.

<a name="PDF_F_Q"></a>
## F(Q) Function

This shows the F(Q) function. 
See the [PDF Controls](#PDF_Controls) for information on menu commands and plot options.


<a name="PDF_G_R"></a>
## G(r) Function

This shows the PDF, G(r) function. 
See the [PDF Controls](#PDF_Controls) for information on menu commands and plot options.
 
