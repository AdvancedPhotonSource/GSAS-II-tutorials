#!/bin/bash
###########################
# this script is obsolete #
# these actions are done  #
# in GitHub workflow      #
###########################
#
# to add a new tutorial
# 1) create new directory in .../GSASII-tutorials
# 2) add .html file, data/ directory
# 3) add to git
# 4) add to .../GSASII/tutorialIndex.py
# 5) run this from file location (cd .../GSASII-tutorials/scripts; bash addNewTutorials.sh)
#
cp -p ../../GSASII/GSASII/tutorialIndex.py .
python makeGitTutorial.py ..
rm tutorialIndex.py
echo use command:
echo "    git add ../*/data/index.html ../tutorials.html"
