#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Zhangyinuo"
__pkuid__  = "1800011770"
__email__  = "1800011770@pku.edu.cn"
"""

import sys
from collections import Counter
from urllib.request import urlopen


def wcount(lines, topn=10):
    """count words from lines of text string, then sort by their counts
    in reverse order, output the topn (word count), each in one line. 
    """
    for i in [',','.','!','?',':',';','"',"'",'(',')','-','/','\n']:
        lines_=lines.replace(i,' ')
        lines__=lines_.lower()

    lineslist=lines__.split()
    lineslist_=Counter(lineslist).most_common(topn)
    for i in lineslist_:
        print(i[0],i[1])
                

if __name__ == '__main__':

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)
    
    if  len(sys.argv) == 2:
        doc = urlopen(sys.argv[1])
        docstr = doc.read().decode()
        doc.close
        wcount(docstr)
        sys.exit(1)
        
    if  len(sys.argv) == 3:
        doc = urlopen(sys.argv[1])
        docstr = doc.read().decode()
        doc.close
        wcount(docstr,topn=int(sys.argv[2]))
        sys.exit(1)
