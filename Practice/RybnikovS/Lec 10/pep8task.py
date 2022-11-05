import sys
import os
import hashlib
import ast
import argparse
from time import *  # Некорретный импорт всей библиотеки


class shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []
        for root, directories, files in os.walk(dirname): #
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3' #неверное название hashname -> hash_name
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname)) #лишние закрывающие скобки у обоих аргументов
        f = open(output, 'r') #файл открыли, но не закрыли, файл открыт на чтение, должно на запись
        f.write(str(self.map))

    def restore(self, dirname, restore_path):
        with open(filename, '+') as f: #  Открывается какой-то непонятный filename
              # Открывается файл на чтение и запись. Нужно только на чтение.
            self.map = ast.literal_eval(f.read())
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s: #неверное название hashname -> hash_name
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])
        os.remove(restore_path)

     def generateName(self, seed=time()): #обозначить как staticmethod и убрать self
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
        sys.exit() #можно не вызывать явно через sys


main()
