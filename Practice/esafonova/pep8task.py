import sys
import os
import hashlib
import ast
import argparse
from time import * #неясно что импортируется *


class shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output): # Наименование dir_name через подчеркивание
          mp3s = [] # Нарушение табуляции
        for root, directories, files in os.walk(dirname): # Наименование dir_name через подчеркивание
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3' # Должно быть hash_name
            self.map[hashname] = mp3 # Должно быть hash_name
            os.rename(path + '/' + mp3), path + '/' + hashname)) # Должно быть hash_name
            # Лишняя или недостающая скобка
          f = open(output, 'r')
          f.write(str(self.map))

    def restore(self, dirname, restore_path): # Должно быть dir_name через подчеркивание
          with open(filename, '+') as f:# Должно быть file_name через подчеркивание
            self.map = ast.literal_eval(f.read())
          mp3s = [] # Нарушение табуляции
        for root, directories, files in os.walk(dirname): # Должно быть dir_name через подчеркивание
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) # Лишняя скобка
        os.remove(restore_path)
                
     def generateName(self, seed=time()): # Должно быть generate_name через подчеркивание
          return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help') # Должно быть sub_command через подчеркивание
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname') # Должно быть dir_name через подчеркивание
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname') # Должно быть dir_name через подчеркивание
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

def main():
    args = parse_arguments()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
          if args.output:
                Shuffler.rename(args.dirname, 'restore.info') # Должно быть dir_name через подчеркивание
          else:
                Shuffler.rename(args.dirname, args.output) # Должно быть dir_name через подчеркивание
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map) # Должно быть dir_name через подчеркивание
    else:
        sys.exit()


main()
