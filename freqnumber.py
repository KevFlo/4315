from curses.ascii import isdigit
from fileinput import close
from typing import List
from functools import reduce
import re
from posixpath import split
import sys

def freqNum(k, inFile, outfile):
    
    
    integerlst: List[int] # integers only
    tempintLst: List[int]
    fltlst: List[float] # all real numbers
    tempfltLst: List[float]

    with open(inFile) as f:
        bloated = [s.strip().split(" ") for s in f.readlines()]
        flatList = [element for innerList in bloated for element in innerList]
    f.close()
        # now that the I/O has been handled we can calculate frequency and build lists or reals and integers
    print(flatList)
    #     Your program should use map()/reduce() functional constructs to compute the frequency of each number in the input file.
    # cleanlst = lambda c: something goes here ,filter(lambda i:re.match(r'-?[.\d]+',i),something goes here)
    # print(*cleanlst)
    # integerlst = map(lambda s: isdigit(s[0]), flatList)
    # fltlst = map(lambda s: not(isdigit(s[0])), flatList)
    # count = 0
    # for i in fltlst:
    #     print(i)   
    # print(integerlst)
    # print(fltlst)
    # tempintLst = reduce(lambda x, y: x + y, integerlst)
    # tempfltLst = reduce(lambda x, y: x + y, fltlst)

    with open(outfile, "a") as f:
        for i in range(k):
            f.write(flatList[i])
        # for i in range(k):
        #     f.write(flatList[i])
    f.close()

    return 0


if __name__ == '__main__':
    argl = sys.argv[1].split(";")
    i = 0
    for pattrn in argl:
        if i == 0:
            k = "".join([val for val in pattrn[(pattrn.find("=")+1):]])
        elif i == 1:
            infile = ("".join([val for val in pattrn[(pattrn.find("=")+1):]]))
        else:
            out = "".join([val for val in pattrn[(pattrn.find("=")+1):]])
        i+=1
    freqNum(int(k),infile,out)