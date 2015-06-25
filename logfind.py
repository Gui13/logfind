#!/usr/bin/env python3


import os
import argparse
import glob


pref_file = '~/.logfind'

parser = argparse.ArgumentParser(prog='logfind', description='Finds things in logs. You should specify the list of files to consider in the ~/.logfind file (regexps allowed).')
parser.add_argument('patterns', metavar='PATTERN', type=str, nargs='+',
                    help='''The list of words to search for. All words should be found for the logfile to match.''')
parser.add_argument('-o', dest='or_operator', type=bool, const=True, default=False, nargs='?',
                    help='''Will change the matcher to match at least one of the words instead of all.''')


# todo: sinplify the loop maybe?
def find_words_in_file(filename, words, match_one):
    with open(filename) as logfile:
        found_words = 0
        for line in logfile:
            for word in words:
                if word in line:
                    found_words += 1
                    if match_one:
                        return True

        if found_words == len(words):
            return True
    return False

if __name__ == '__main__':
    args = parser.parse_args()

    files = []

    try:
        # read prefs file and build list of files
        prefs = open(os.path.expanduser(pref_file), 'r')
        for line in prefs:
            line = os.path.expanduser(line)
            line = os.path.expandvars(line)
            files += [f for f in glob.glob(line) if os.path.isfile(f)]

        for f in files:
            if find_words_in_file(f, args.patterns, args.or_operator):
                print('{filename}'.format(filename=f))


    except FileNotFoundError as e:
        print('The file {pref} was not found. logfind will not search anywhere. Please create this file and specify the list of files to search in it.'.format(pref=pref_file))
        