# scan through all tutorial files and change encoding
import glob
#for f in glob.glob("../*/*.htm*"):
#    s = open(f,'rb').read()
#    if b'charset=windows-1252' in s:
#        print('Windows',f)
#        open(f,'wb').write(s.replace(b'charset=windows-1252',b'charset=UTF-8'))
#    elif b'charset=macintosh' in s:
#        open(f,'wb').write(s.replace(b'charset=macintosh',b'charset=UTF-8'))
#        print('Mac',f)
#    else:
#        print('OK',f)

import os
import subprocess
import glob
failed = []
f = os.path.expanduser('~/G2/git/GSASII-tutorials/RMCProfile-I/RMCProfile-I.htm')
for f in glob.glob(os.path.expanduser('~/G2/git/GSASII-tutorials/*/*.htm*')):
    ftmp = os.path.join('/tmp',os.path.split(f)[1])
    cmd = f'iconv {f!r} -f windows-1252 -t utf-8 > {ftmp!r}'
    print(cmd)
    rc = subprocess.call(cmd,shell=True)
    if rc == 0:
        print(f'creation of {ftmp} OK, moving')
        subprocess.run(['mv','-v',ftmp,f])
    else:
        print(f'creation of {ftmp} Failed')
        failed.append(f)
print('failed on')
for f in failed: print('\t',f)
