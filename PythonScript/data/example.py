'''Sample script to demonstrate use of GSASIIscriptable to duplicate the
tutorial found here:
https://subversion.xray.aps.anl.gov/pyGSAS/Tutorials/CWCombined/Combined%20refinement.htm

This script is described in this tutorial: 
https://subversion.xray.aps.anl.gov/pyGSAS/Tutorials/PythonScript/Scripting.htm
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
gpx = G2sc.G2Project(filename='PbSO4.gpx')

# setup step 1: add two histograms to the project
hist1 = gpx.add_powder_histogram(os.path.join(datadir,"PBSO4.XRA"),
                          os.path.join(datadir,"INST_XRY.PRM"))
hist2 = gpx.add_powder_histogram(os.path.join(datadir,"PBSO4.CWN"),
                          os.path.join(datadir,"inst_d1a.prm"))
# setup step 2: add a phase and link it to the previous histograms
phase0 = gpx.add_phase(os.path.join(datadir,"PbSO4-Wyckoff.cif"),
                      phasename="PbSO4",
                      histograms=[hist1,hist2])

# not in tutorial: increase # of cycles to improve convergence
gpx.data['Controls']['data']['max cyc'] = 8 # not in API

# tutorial step 4: turn on background refinement (Hist)
refdict0 = {"set": {"Background": { "no. coeffs": 3, "refine": True }}}
gpx.save('step4.gpx')
gpx.do_refinements([refdict0])
HistStats(gpx)

# tutorial step 5: add unit cell refinement (Phase)
gpx.save('step5.gpx')
refdict1 = {"set": {"Cell": True}} # set the cell flag (for all phases)
gpx.set_refinement(refdict1)
gpx.do_refinements([{}])
HistStats(gpx)

# tutorial step 6: add Dij terms (HAP) for histogram 1 only
gpx.save('step6.gpx')
refdict2 = {"set": {"HStrain": True}} # set HAP parameters
gpx.set_refinement(refdict2,phase=phase0,histogram=[hist1])
gpx.do_refinements([{}]) # refine after setting
HistStats(gpx)

# tutorial step 7: add size & strain broadening (HAP) for histogram 1 only 
gpx.save('step7.gpx')
refdict2 = {"set": {"Mustrain": {"type":"isotropic","refine":True},
                    "Size":{"type":"isotropic","refine":True},
                    }}
gpx.set_refinement(refdict2,phase=phase0,histogram=[hist1])
gpx.do_refinements([{}]) # refine after setting
HistStats(gpx)

# tutorial step 8: add sample parameters & set radius (Hist); refine atom parameters (phase)
gpx.save('step8.gpx')
hist1.set_refinements({'Sample Parameters': ['Shift']})
hist2.set_refinements({'Sample Parameters': ['DisplaceX', 'DisplaceY']})
hist2.data['Sample Parameters']['Gonio. radius'] = 650. # not in API
phase0.set_refinements({"Atoms":{"all":"XU"}})
gpx.do_refinements([{}]) # refine after setting
HistStats(gpx)

# tutorial step 9: change data limits & inst. parm refinements (Hist) 
gpx.save('step9.gpx')
hist1.set_refinements({'Limits': [16.,158.4]})
hist2.set_refinements({'Limits': [19.,153.]})
gpx.do_refinements([{"set": {'Instrument Parameters': ['U', 'V', 'W']}}])
HistStats(gpx)
