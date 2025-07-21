<!--- Don't change the HTML version of this file; edit the .md version -->
<a name="Phase-Pawley_reflections"></a>
# **Pawley reflections** phase tab

This gives the list of reflections used in a Pawley refinement; for them to be used the 'Do Pawley refinement' flag must be set (see the [General tab](./phasegeneral.md)), otherwise they are ignored.

<H3 style="color:blue;font-size:1.1em">What can I do here?</H3>

* Menu '**Operations**' –

    * **Pawley settings** – allows setting of Pawley parameters as shown on the General tab.
    * **Pawley create** – this creates a new set of Pawley reflections, over writing any preexisting Pawley set. They are generated with d-spacings larger than the limit set as 'Pawley dmin' in the General tab for this phase. By default, the refine flags are not set and the Fsq(hkl) = 100.0.
    * **Pawley estimate** – this attempts an estimate of Fsq(hkl) from the peak heights of the reflection as seen in the 1st powder pattern of those shown as 'Use' in the [Data tab](./phasedata.md) for this phase.
    * **Pawley update** – process Pawley reflection set for negative intensities. These are set to ½ its absolute value for noncentrosymmetric space groups (0.3 otherwise); the refine flag is turned off. One should repeat Pawley refinement and then do Refine all and an additional refinement. Repeat as needed to remove negative intensities. Set Pawley neg. wt. (see Pawley settings) to further suppress negatives.
    * **Refine all** – sets all refine flags
    * **Refine none** – clears all refine flags
    * **Toggle selection** – toggles all refine flags

* You can change the refine flags either by clicking on the box or by selecting one and then selecting the column (a single click on the column heading). Then type 'y' to set the refine flags or 'n' to clear the flags. You should not refine those reflections that are below the lower limit or above the upper limit of the powder pattern otherwise you will have singular matrix errors in your Pawley refinement (adds to the refinement time as bad parameters are removed). Reflections that fall inside excluded regions may also result in refinement singularities.
* You can delete an individual reflection from the Pawley set by selecting its row (will be highlighted) and then pressing the Delete key (this is not reversable & only deletes the 1st one selected).
* You can change the individual Fsq(hkl) values by selecting it, typing in the new value and then pressing enter or selecting somewhere else in the table.
