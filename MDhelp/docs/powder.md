<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="PWDR"></a>
#  Overview on **PWDR** data tree entries: Powder Diffraction

This is where to find information on the Tree item in GSAS-II associated with powder diffraction (labeled PWDR) and its associated subitems. Note that GSAS-II uses the label of "histogram" for datasets of any type (single-crystal, powder,...) Powder diffraction histograms are added to a project using the Import/"Powder Data" menu items. After data are read, if there are phases present, you will be offered a chance to link the imported histograms to the previously imported phase(s). Likewise, if phase(s) are imported after histograms you will also be asked to link the new phase(s) to existing histograms. It is also possible to add histograms to a phase later by selecting that phase in the data tree and then selecting the "Data" tab and finally using the "Edit Phase"/"Add powder histograms" menu command. Note that there is no limit to the number of histograms that can be included in a GSAS-II project (other than as limited by available computer memory) and histograms that are not linked to at least one phase are ignored in refinements. 

Each powder diffraction dataset has a number of children (subdata tree items) in the tree, as are shown below. 

* [Comments](./powdercomments.md)
* [Limits](./powderlimits.md)
* [Background](./powderbkg.md)
* [Instrument Parameters](./powderinst.md)
* [Sample Parameters](./powdersample.md)
* [Peak List](./powderpeaks.md)
* [Index Peak List](./powderindexppeaks.md)
* [Unit Cells List](./powdercells.md)
* [Reflection Lists](./powderrefs.md)

Clicking on the parent or on the subdata tree items, as well as [main (parent) entry for the histogram](./powderparent.md) 
them produces similar plots of the powder diffraction histogram, with different variations, as examples:

* By selecting the Limits entry, range of data used, as well as possible excluded regions, can be set.
* Selecting Reflection Lists allows display of reflection indices (hkl values) for a selected phase. Letting the mouse rest unmoved at the position of a reflection in \(2\theta\), TOF, Q, etc. (the vertical position does not matter) will cause these to be displayed. After a short delay a "tool tip" will appear with indices for any reflections close to the lateral mouse position.
* Selecting Background allows a mouse to be used to define fixed points where a background curve can be fitted to those points.
* Selecting Peak List allows positions of peaks to be defined for use in direct peak fitting.
* Selecting Unit Cells List can show the positions of reflections for an arbitrary set of unit cell parameters, optionally with space group extinctions applied.

One selection produces a different type of plot:

* Selecting Instrument Parameters displays plot of peak widths as a function of Q rather than the powder diffraction histogram.  

Each of the PWDR data tree entries allows access to different parameters associated with the dataset and offers different menu commands.
