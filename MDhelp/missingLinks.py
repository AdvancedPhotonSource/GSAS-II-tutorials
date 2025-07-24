# find anchors & links in original (HTML) version of Help files
import glob
import os
import subprocess
from html.parser import HTMLParser
# original HTML files
dirname = os.path.expanduser("~/G2/main/GSASII/")
files = glob.glob(os.path.join(dirname,'help','*.html'))
# new HTML files generated from MarkDown
dirname = os.path.expanduser("~/G2/GSASII-tutorials/MDhelp/site")
indx = os.path.abspath(os.path.join(dirname,'anchorIndex.txt'))

# create an index to the .HTML anchors
MDindex = {}
print('reading file',indx)
with open(indx,'r') as indexfile:
    for line in indexfile.readlines():
        fil,anchors = line.split(':')
        for a in anchors.split(','):
            if a in MDindex: print(a,'repeated!')
            MDindex[a.strip()] = fil
#print(MDindex)
#for i in sorted(MDindex):
#    print(i,'\t',MDindex[i])
#import sys; sys.exit()

class MyHTMLParser(HTMLParser):
    gotlink = []
    def handle_starttag(self, tag, attrs):
        self.gotlink = []
        if tag == 'a' and 'name' in [i[0] for i in attrs]:
            #print('\tanchor:',[i[1] for i in attrs if i[0] == 'name'][0])
            for i in attrs:
                if i[0] != 'name': continue
                if i[1] in MDindex: continue
                print('\tanchor:',i[1])
            #anchorfil.write(f'<a name="{attrs[0][1]}"></a>\n')
        elif tag == 'div' and 'id' in [i[0] for i in attrs]:
            print("Encountered a start tag:", tag, attrs)
        elif tag == 'a':
            for lst in attrs:
                if 'href' == lst[0]:
                    self.gotlink.append(lst[1])
            #print('\t\tlink',', '.join([i[1] for i in attrs if i[0] == 'href']))
    def handle_data(self,data):
        if self.gotlink:
            data.replace('\n',' ').strip() 
            #print(f"\t\tlink {', '.join(self.gotlink)} {' '.join(data.split())!r}")
            #breakpoint()

parser = MyHTMLParser()
for fil in sorted(files):
    sfil = os.path.split(fil)[1]
    #anchorfil = open(os.path.join(os.path.dirname(__file__),sfil+'_anchors'),'w')
    print('\n'+sfil)
    #parser.feed(open(fil,'r').read())
    with subprocess.Popen(['iconv', '-f', 'UTF-16LE', '-t', 'UTF-8', fil],encoding='UTF-8',
                             stdin=subprocess.PIPE,
                             stdout=subprocess.PIPE,
                             stderr=subprocess.PIPE) as p:
        txt,err = p.communicate()
    parser.feed(txt)
    #anchorfil.close()
