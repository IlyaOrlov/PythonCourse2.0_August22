import sys
import os
import hashlib
import ast
import argparse
from time import * # звездочка не указывает, вроде бы, на то, что импортируется


class shuffler: # нарушено правило CamelCase

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))
          f = open(output, 'r') # нарушение уровней вложенности (2 пробела вместо 4)
          f.write(str(self.map)) # тоже нарушены уровни вложенности

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f: #уровни вложенности
            self.map = ast.literal_eval(f.read()) # уровни вложенности
          mp3s = [] # уровни вложенности
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3': # уровни вложенности
                    mp3s.append({root, file}) # уровни вложенности
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) # лишняя скобка
        os.remove(restore_path)
                
     def generateName(self, seed=time()): # уровни вложенности + generate и name дожны быть набраны через snake case
          return hashlib.md5(str(seed)).hexdigest()


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
