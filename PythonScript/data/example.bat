@REM example script that uses cmd.exe to run a GSAS-II script
set datadir=C:\Users\toby.WIN10-VM\temp\
set gsaspath=c:\GSASII\
set python=C:\conda3\python.exe
%python% %gsaspath%GSASIIscriptable.py create test.gpx 
%python% %gsaspath%GSASIIscriptable.py add test.gpx ^
    -d %datadir%PBSO4.XRA %datadir%PBSO4.CWN ^
        -i %datadir%INST_XRY.PRM %datadir%inst_d1a.prm -hf GSAS ^
    -p %datadir%PbSO4-Wyckoff.cif -pf CIF -l 0 1
%python% %gsaspath%GSASIIscriptable.py refine test.gpx example.json
