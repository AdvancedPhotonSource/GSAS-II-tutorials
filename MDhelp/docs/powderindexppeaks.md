<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="PWDR_Index_Peak_List"></a>
#  PWDR **Index Peak List** subdata tree item (Powder Diffraction)

This window shows the list of peaks that will be used for indexing (see [Unit Cells List](./powdercells.md)). It must be filled with peaks from the [Peak List](./powderpeaks.md) (using the Operations‑>Load/Reload menu command) before indexing can proceed. When indexing is completed, this display will show the resulting hkl values for every indexed reflection along with the calculated d-spacing ('d-calc') for the selected unit cell in Unit Cells List. .

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

* Double-clicking on a row of the table causes that row to be selected and causes that peak to be highlighted in the plot.
* Pressing "d" in the plot window causes the next peak in the table (or the first if none are selected) to be selected and causes that peak to be highlighted in the plot; pressing "u" causes the previous peak in the list to be highlighted.
* You may designate that individual peaks not be used in the indexing by process by unchecking the corresponding "use" box. 

### "**Operations**" Menu Commands

* **Load/Reload** – loads the peak positions & intensities from the [Peak List](./powderpeaks.md)  to make them available for the indexing routine. The d-obs value is obtained from Bragg's Law after applying the Zero correction shown on the Instrument Parameters table to the position shown here.
* **Save** – saves a csv version of this table.
* **Export to PreDict** – saves the table in a format that can be used by PreDict, an updated version of the DICVOL program.
* **Refine Cell** – optimizes the unit cell parameters shown at the bottom of the window to best-fit the peak list.

<H3 style="color:blue;font-size:1.1em">What is plotted here?</H3>

The plot is the largely the same as for the parent PWDR Powder Histograms tree entry 
[with the same plot actions](./powder.md#PWDR_plot_actions) and [same key press commands](./powder.md#PWDR_keylist). 
Specific to this plot are the peak positions that are shown as vertical solid blue lines. To show that a peak is selected, it is highlighted in yellow and, if "use" is selected, the blue line is made wider. The upper and lower data limits are shown as red and green dashed vertical lines, respectively. Tick marks aer not shown. Limits cannot be dragged from this data tree item. 

<H3 style="color:blue;font-size:1.1em">What can I do with the plot?</H3>

* Highlight each peak in the list successively using the "d" or "u" keyboard keys. 
