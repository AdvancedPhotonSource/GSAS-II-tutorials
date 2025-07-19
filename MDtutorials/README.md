# Steps in creating a new tutorial

> [!NOTE] 
> Note: this is draft info and needs to be checked that I did not leave anything out

1. Create a new directory in the current location. Make sure not to use a name already in use for an existing tutorial (in the main directory, (https://github.com/AdvancedPhotonSource/GSAS-II-tutorials/tree/main). 

1. Create a &lt;filename&gt;.md file in the new directory. Name is arbitrary, but repeating the directory name is not a bad idea. Start the file with content like this:

        ---
        title: "Tutorial: ...anything you want to put here"
        ---
        <!--- Don't change the HTML version of this file; edit the .md version -->

        [//1]: <> (Comment: optional comment(s) here.)

        ## Intro

    look at the previously-created tutorials in this directory to see how formatting is done. 
    
1. Create a directory named `imgs` inside the new directory. Any images used in the tutorial go here. 

1. (Optional) Create a directory named `data` inside the new directory. Any data files used in the tutorial go here. 

1. Edit the file `tutorialIndex.py` (in the main GSAS-II repo) to include the new tutorial. Note that the first item in the list will be the directory name chosen in the first step, above. The second item will be the name of the generated `.html` file which will be based on the name of the `.md` file chosen in the second step. The remaining entries are the title of the tutorial and a synopsis. 

TODO: someday, I'd like to have keywords associated with tutorials and a search mechanism to make it easier to find some of the "little things" (for example constraint definition) that are shown in them. 


