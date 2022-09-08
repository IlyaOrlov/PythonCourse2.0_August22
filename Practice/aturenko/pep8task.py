
import sys
import os
import hashlib
import ast
import argparse
from time import * # It is not worth importing from *, because in this way we pollute our own namespace,
                   # it would be more correct to: import time


class shuffler: # The name of the class must begin with a capital letter : class Shuffler:
                # Missing """documentation line""" for the class,the main functions of the classes must be separated
                # by two empty lines

    def __init__(self): # This line uses a tab for a paragraph, you need to use 4 spaces
        self.map = {} # You need to use 4 spaces,missing documentation line after def, the main functions
                      # of the classes must be separated by two empty lines

    def rename(self, dirname, output): # You need to use 4 spaces,missing documentation line after def, the main functions
                                       # of the classes must be separated by two empty lines
        mp3s = []                      # You need to use 4 spaces,the way of writing the variable name
                                       # does not correspond to pep8
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3': # Should better use ".endswith()": if file.endswith('.mp3'):
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))
          f = open(output, 'r') # Incorrect number of spaces, should be 8
          f.write(str(self.map)) # Incorrect number of spaces, should be 8

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:
            self.map = ast.literal_eval(f.read()) # Incorrect number of spaces, should be 12
          mp3s = []
        for root, directories, files in os.walk(dirname): # Incorrect number of spaces, should be 8
            for file in files:
               if file[-3:] == '.mp3': # Should better use ".endswith()": if file.endswith('.mp3'):
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) 
        os.remove(restore_path)

    def generateName(self, seed=time()): # It is better to use underscores in the function name to separate words,
                                         # Incorrect number of spaces, should be 4
        return hashlib.md5(str(seed)).hexdigest() # Incorrect number of spaces, should be 8


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
          if args.output:
                Shuffler.rename(args.dirname, 'restore.info')
          else:
                Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
