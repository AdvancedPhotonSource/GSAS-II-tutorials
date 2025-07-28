'''Sample script to demonstrate use of GSASIIscriptable to duplicate the
tutorial found here:
https://advancedphotonsource.github.io/GSAS-II-tutorials/CWCombined/Combined%20refinement.htm

This script is described in this tutorial: 
https://advancedphotonsource.github.io/GSAS-II-tutorials/PythonScript/Scripting.htm
'''

import os,sys
sys.path.insert(0,'/Users/toby/software/G2/GSASII')
import GSASIIscriptable as G2sc

workdir = "/Users/toby/Scratch/PythonScript"
datadir = "/Users/toby/software/G2/Tutorials/PythonScript/data"

def HistStats(gpx):
    '''prints profile rfactors for all histograms'''
    print(u"*** profile Rwp, "+os.path.split(gpx.filename)[1])
    for hist in gpx.histograms():
        print("\t{:20s}: {:.2f}".format(hist.name,hist.get_wR()))
    print("")
    gpx.save()

# create a project with a default project name
gpx = G2sc.G2Project(filename='NotUsed.gpx')

# setup step 1: add two histograms to the project
hist1 = gpx.add_powder_histogram(os.path.join(datadir,"PBSO4.XRA"),
                          os.path.join(datadir,"INST_XRY.PRM"),
                          fmthint="GSAS powder")
hist2 = gpx.add_powder_histogram(os.path.join(datadir,"PBSO4.CWN"),
                          os.path.join(datadir,"inst_d1a.prm"),
                          fmthint="GSAS powder")
# setup step 2: add a phase and link it to the previous histograms
phase0 = gpx.add_phase(os.path.join(datadir,"PbSO4-Wyckoff.cif"),
                      phasename="PbSO4",
                      histograms=[hist1,hist2],fmthint='CIF')

# not in tutorial: increase # of cycles to improve convergence
gpx.data['Controls']['data']['max cyc'] = 8 # not in API
hist2.data['Sample Parameters']['Gonio. radius'] = 650. # not in API

# tutorial step 4: turn on background refinement (Hist)
refdict0 = {"set": {"Background": { "no. coeffs": 3, "refine": True }},
            "output":'step4.gpx',
            "call":HistStats,}
# tutorial step 5: add unit cell refinement (Phase)
refdict1 = {"set": {"Cell": True},    # set the cell flag (for all phases)
            "output":'step5.gpx',
            "call":HistStats,}
# tutorial step 6: add Dij terms (HAP) for phase 1 only
refdict2 = {"set": {"HStrain": True},  # set HAP parameters
            "histograms":[hist1],      # histogram 1 only
            "phases":[phase0],         # unneeded (default is all phases)
            "output":'step6.gpx',
            "call":HistStats,}
# tutorial step 7: add size & strain broadening (HAP) for histogram 1 only 
refdict3 = {"set": {"Mustrain": {"type":"isotropic","refine":True},
                    "Size":{"type":"isotropic","refine":True},},
            "histograms":[hist1],      # histogram 1 only
            "output":'step7.gpx',
            "call":HistStats,}
# tutorial step 8: add sample parameters & set radius (Hist); refine atom parameters (phase)
refdict4a = {"set": {'Sample Parameters': ['Shift']},
            "histograms":[hist1],      # histogram 1 only
             "skip": True}
refdict4b = {"set": {"Atoms":{"all":"XU"}, 'Sample Parameters': ['DisplaceX', 'DisplaceY']},
            "histograms":[hist2],      # histogram 2 only (does not affect atom parms)
            "output":'step8.gpx',
            "call":HistStats,}
# tutorial step 9: change data limits & inst. parm refinements (Hist) 
refdict5a = {"set": {'Limits': [16.,158.4]},
            "histograms":[hist1],      # histogram 1 only
             "skip": True,}
refdict5b = {"set": {'Limits': [19.,153.]},
            "histograms":[hist2],      # histogram 2 only
             "skip": True}
refdict5c = {"set": {'Instrument Parameters': ['U', 'V', 'W']},
            "output":'step9.gpx',
            "call":HistStats,}

dictList = [refdict0,refdict1,refdict2,refdict3,
            refdict4a,refdict4b,
            refdict5a,refdict5b,refdict5c]
                
gpx.do_refinements(dictList)
