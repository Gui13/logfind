#!/usr/bin/env python


import os
import sys
import argparse
import glob


pref_file = '~/.logfind'

parser = argparse.ArgumentParser(prog='logfind', description='Finds things in logs. You should specify the list of files to consider in the ~/.logfind file (regexps allowed).')
parser.add_argument('patterns', metavar='PATTERN', type=str, nargs='+',
                    help='''The list of words to search for. All words should be found for the logfile to match.''')
parser.add_argument('-o', dest='or', type=bool,
                    help='''Will change the matcher to match at least one of the words instead of all.''')


if __name__ == '__main__':
    parser.parse_args()

    files = []

    try:
        prefs = open(os.path.expanduser(pref_file), 'r')
        for line in prefs:
            line = os.path.expanduser(line)
            line = os.path.expandvars(line)
            files += [f for f in glob.glob(line) if os.path.isfile(f)]
        print('We need to check these files: {dirs}'.format(dirs=files))



    except FileNotFoundError as e:
        print('The file {pref} was not found. logfind will not search anywhere. Please create this file and specify the list of files to search in it.'.format(pref=pref_file))
        