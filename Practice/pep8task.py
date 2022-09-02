import sys
import os
import hashlib  # hash_lib
import ast
import argparse # arg_parse
from time import *


class shuffler:   # CapWords

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'     # hash_name, generate_Name
            self.map[hashname] = mp3                    # hash_name
            os.rename(path + '/' + mp3), path + '/' + hashname))  # не хватает скобок (( нижнего подчеркивания has_hname
          f = open(output, 'r')
          f.write(str(self.map))

    def restore(self, dirname, restore_path):     # dir_name
          with open(filename, '+') as f:          # нижнее подчеркивание file_name
            self.map = ast.literal_eval(f.read())
          mp3s = []
        for root, directories, files in os.walk(dirname):   # dir_name
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:               # hash_name
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) # hash_name
        os.remove(restore_path)
                
     def generateName(self, seed=time()):        #  generate_name
          return hashlib.md5(str(seed)).hexdigest()  # hash_lib


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')  # sub_parsers
    rename_parser = subparsers.add_parser('rename', help='rename help')            # sub_parsers
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")      # sub_parsers
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    Shuffler = shuffler()        # shuffler   переменная пишется с маленькой буквы
    if args.subcommand == 'rename':
          if args.output:
                Shuffler.rename(args.dirname, 'restore.info')  # shuffler   dir_name
          else:
                Shuffler.rename(args.dirname, args.output)    # shuffler   dir_name
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)      # shuffler   dir_name
    else:
        sys.exit()


main()
