# scan through all tutorial files and change encoding
import glob
for f in glob.glob("../*/*.htm*"):
    s = open(f,'rb').read()
    if b'charset=windows-1252' in s:
        print('Windows',f)
        open(f,'wb').write(s.replace(b'charset=windows-1252',b'charset=UTF-8'))
    elif b'charset=macintosh' in s:
        open(f,'wb').write(s.replace(b'charset=macintosh',b'charset=UTF-8'))
        print('Mac',f)
    else:
        print('OK',f)
