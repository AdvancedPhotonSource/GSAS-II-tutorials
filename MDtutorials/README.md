This directory contains files used to generate new GSAS-II tutorials. (The older tutorials were created using Microsoft Word to produce `.html` files directly.)
The tutorials are placed on the web at
https://advancedphotonsource.github.io/GSAS-II-tutorials/<subdir> using two commands to build the HTML:

    pandoc --standalone --css tutorial.css --mathjax -o ${outfile}  ${infil}
    sed -i "s/<figure>/<BR clear=all><figure>/g" ${outfile}

Note that on MacOS the sed command must be `sed -i "" "s/...`. The [`tutorial.css` file](https://github.com/AdvancedPhotonSource/GSAS-II-tutorials/blob/main/MDtutorials/tutorial.css) is found in the `MDtutorials` directory and is copied to the same location as `$outfile`.

# Steps in creating a new tutorial

> [!NOTE] 
> Note: this is draft info and needs to be checked that I did not leave anything out

1. Create a new directory in the current location. Make sure not to use a name already in use for an existing tutorial (in the main directory, (https://github.com/AdvancedPhotonSource/GSAS-II-tutorials/tree/main). 

1. Create a &lt;filename&gt;.md file in the new directory. Name is arbitrary, but repeating the directory name is not a bad idea, as `.../new-tutorial/new-tutorial.md`. Look at file `template.md` as an outline for formatting the tutorial ([formatted version is here](https://advancedphotonsource.github.io/GSAS-II-tutorials/tutorial_template/template.html))

Start the new tutorial file with content like this:

        ---
        title: "Tutorial: ...anything you want to put here"
        ---
        <!--- Don't change the HTML version of this file; edit the .md version -->

        [//1]: <> (Comment: optional comment(s) here.)
        
        * Exercise files are found [here](data/index.html)
        
        ## Intro

omit the "Exercise files..." line if no exercise files are in use. Note that the `.../data/index.html` file is generated automatically.
    
1. Create a directory named `imgs` inside the new directory. Any images used in the tutorial go here. 

1. (Optional) Create a directory named `data` inside the new directory. Any data files used in the tutorial go here. 

1. Edit the file `tutorialIndex.py` (in the main GSAS-II repo) to include the new tutorial. Note that the first item in the list will be the directory name chosen in the first step, above. The second item will be the name of the generated `.html` file which will be based on the name of the `.md` file chosen in the second step. The remaining entries are the title of the tutorial and a synopsis. 


Editing of MarkDown can be done with any text editor, but it is sometimes nice to see the final result before committing the file. One can use the `pandoc` command above to see the result, or use VS Code, which has a MarkDown viewer. There are also lots of programs that can be used as MarkDown editors: https://github.com/mundimark/awesome-markdown-editors/blob/master/README.md
but I have not tried any of them.


TODO: someday, I'd like to have keywords associated with tutorials and a search mechanism to make it easier to find some of the "little things" (for example constraint definition) that are shown in them. 


