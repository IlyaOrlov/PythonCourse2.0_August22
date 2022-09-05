import sys
import os
import hashlib
import ast
import argparse
from time import * #неясно что импортируется *


class shuffler: #наименование класса должно быть CapWords

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = [] # 4 пробела
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname)) # удалить скобки в средине и в конце
          f = open(output, 'r') # Нарушение уровней вложенности лишние 2 пробела
          f.write(str(self.map)) # Нарушение уровней вложенности лишние 2 пробела

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f: # 4 пробела
            self.map = ast.literal_eval(f.read()) # 4 пробела
          mp3s = [] # 4 пробела
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3': # 4 пробела
                    mp3s.append({root, file}) # 4 пробела
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) # Лишняя скобка
        os.remove(restore_path)
                
     def generateName(self, seed=time()): # Должно быть generate_name через подчеркивание
          return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help') # Должно быть sub_command через подчеркивание
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
    Shuffler = shuffler()  # имя эм.класса со строчной, а класса с прописной
    if args.subcommand == 'rename':
          if args.output:
                Shuffler.rename(args.dirname, 'restore.info') #shuffler
          else:
                Shuffler.rename(args.dirname, args.output) #shuffler
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)  #shuffler
    else:
        sys.exit()


main()
