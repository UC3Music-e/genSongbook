#!/usr/bin/python

import sys, os

def query(question, default):
    sys.stdout.write(question + " [" + default + "] ? ")
    choice = raw_input()
    if choice == '':
        return default
    return choice

if __name__ == '__main__':

    print("----------------------")
    print("Welcome to genSongbook")
    print("----------------------")

    # Query song directory path string
    songDirectory = query("Please specify the path of the input song directory","/opt/Dropbox/lyrics/english")
    print("Will use song directory: " + songDirectory)

    # Query template file path string
    templateFile = query("Please specify the path of the template file","template/english.tex")
    print("Will use template file: " + templateFile)

    print("----------------------")

    templateFileFd = open(templateFile, 'r')
    s = templateFileFd.read()
    #sys.stdout.write(s)  #-- Screen output for debugging.

    rep = ""
    for dirname, dirnames, filenames in os.walk( songDirectory ):
        for filename in sorted(filenames):
            rep += "%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%\n"
            name, extension = os.path.splitext(filename)
            rep += "\\chapter{" + name + "}\n"  #-- Note that we use \\ instead of \.
            rep += "\\begin{verbatim}\n"
            song = open( os.path.join(dirname, filename) )
            rep += song.read()
            rep += "\\end{verbatim}\n"
            rep += "\n"

    s.replace("genSongbook",rep)

    outFd = open("out.tex", 'w')
    outFd.write(s)

