# example script that uses sh to run a GSAS-II script
datadir="/Users/toby/software/G2/Tutorials/PythonScript/data"
gsaspath="/Users/toby/GSASII"
python $gsaspath/GSASIIscriptable.py create test.gpx 
python $gsaspath/GSASIIscriptable.py add test.gpx \
    -d $datadir/PBSO4.XRA $datadir/PBSO4.CWN -i $datadir/INST_XRY.PRM $datadir/inst_d1a.prm -hf GSAS \
    -p $datadir/PbSO4-Wyckoff.cif -pf CIF -l 0 1
cat > example.json <<EOF
{"refinements": 
  [
    {"skip":true, "call":"SetParams"},
    { "set": {"Background": {"no. coeffs": 3, "refine": true}}, 
      "call":"HistStats", "output": "step4.gpx"}, 
    { "set": {"Cell": true}, "call":"HistStats", "output": "step5.gpx"}, 
    { "set": {"HStrain": true}, 
      "histograms": [0], "phases": [0], "call":"HistStats", "output": "step6.gpx"}, 
    { "set": {"Mustrain": {"type": "isotropic", "refine": true}, 
             "Size": {"type": "isotropic", "refine": true}}, 
      "histograms": [0], "call":"HistStats", "output": "step7.gpx"}, 
    { "set": {"Sample Parameters": ["Shift"]}, 
      "histograms": [0], "skip": true}, 
    { "set": {"Atoms": {"all": "XU"}, 
             "Sample Parameters": ["DisplaceX", "DisplaceY"]}, 
      "histograms": [1], "call":"HistStats", "output": "step8.gpx"}, 
    { "set": {"Limits": [16.0, 158.4]}, 
      "histograms": [0], "skip": true}, 
    { "set": {"Limits": [19.0, 153.0]}, 
      "histograms": [1], "skip": true}, 
    { "set": {"Instrument Parameters": ["U", "V", "W"]}, 
      "call":"HistStats", "output": "step9.gpx"}
  ],
"code":
  ["global HistStats",
   "def HistStats(gpx):",
   "    '''prints profile rfactors for all histograms'''",
   "    print(u'*** profile Rwp, '+os.path.split(gpx.filename)[1])",
   "    for hist in gpx.histograms():",
   "        print('\t{:20s}: {:.2f}'.format(hist.name,hist.get_wR()))",
   "    print()",
   "proj.data['Controls']['data']['max cyc'] = 8 # not in API",
   "proj.histogram(1).data['Sample Parameters']['Gonio. radius'] = 650. # not in API"
  ]
}
EOF
python $gsaspath/GSASIIscriptable.py refine test.gpx example.json
