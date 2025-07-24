''' This finds anchors in the HTML versions of the new MarkDown-formatted
GSAS-II Help files. The anchors are written into file anchorIndex.txt
in the same directory as the .html files in a format:
   <filename>.html: anchor1, anchor2,...
'''
import glob
import os
from html.parser import HTMLParser
dirname = os.path.abspath(os.path.dirname("__file__"))
files = glob.glob(os.path.join(dirname,'site','*.html'))
indx = os.path.abspath(os.path.join(dirname,'site','anchorIndex.txt'))
print('writing file',indx)
indexfile = open(indx,'w')

class MyHTMLParser(HTMLParser):
    taglist = []
    alltags = []
    def handle_starttag(self, tag, attrs):
        if tag == 'a' and 'name' in [i[0] for i in attrs]:
            #print('\t',[i[1] for i in attrs if i[0] == 'name'][0])
            for i in attrs:
                if i[0] != 'name': continue
                self.taglist.append(i[1])
                #print(i[1],'added',self.taglist)
                if ' ' in i[1]:
                    print(i[1],'has space(s)')
                if i[1] in self.alltags:
                    print(i[1],'repeated')
                else:
                    self.alltags.append(i[1])
        elif tag == 'div' and 'id' in [i[0] for i in attrs]:
            print("Encountered a start tag:", tag, attrs)
parser = MyHTMLParser()
anchorDict = {}
for fil in sorted(files):
    #print('\n'+os.path.split(fil)[1])
    parser.taglist = []
    parser.feed(open(fil,'r').read())
    anchorDict[os.path.split(fil)[1]] = parser.taglist
for key in sorted(anchorDict):
    if len(anchorDict[key]) == 0: continue
    indexfile.write(f'{key}: {", ".join(anchorDict[key])}\n')
for key in sorted(anchorDict):
    if len(anchorDict[key]) == 0: print('File with no anchors:',key)
indexfile.close()
