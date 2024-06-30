import os
import subprocess
import glob
for i,f in enumerate(glob.glob(os.path.expanduser('~/G2/git/GSASII-tutorials/*/*.htm*'))):
    nam = os.path.split(f)[1]
    d = os.path.split(os.path.split(f)[0])[1]
    url =  f"https://advancedphotonsource.github.io/GSAS-II-tutorials/{d}/{nam}"
    print(url)
    subprocess.run(['open',url])
#    if i == 5: break
