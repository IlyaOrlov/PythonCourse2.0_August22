import sys
import os
import hashlib
import ast
import argparse
from time import *  # Некорретный импорт всей библиотеки


class shuffler:  # CapWords

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        # Переопределение встр. фун., для избежания конфликта добавить в конце _
          mp3s = []  # Нарушение правила "4 пробела"
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))
          f = open(output, 'r')  # Нарушение правила "4 пробела"
          f.write(str(self.map))  # Нарушение правила "4 пробела"

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:  # Нарушение правила "4 пробела"
            self.map = ast.literal_eval(f.read())  # Нарушение правила "4 пробела"
          mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':  # Нарушение правила "4 пробела"
                    mp3s.append({root, file})  # Нарушение правила "4 пробела"
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
        os.remove(restore_path)
                #лишние пробелы
     def generateName(self, seed=time()):  # Нарушение правила "4 пробела", нет змеиного стиля
          return hashlib.md5(str(seed)).hexdigest() # Нарушение правила "4 пробела"


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
#должно быть две пустых строки
def main():
    args = parse_arguments()
    Shuffler = shuffler() # Неверное написание имени переменной Shuffler
    if args.subcommand == 'rename':
          if args.output: # Нарушение правила "4 пробела"
                Shuffler.rename(args.dirname, 'restore.info') # Нарушение правила "4 пробела"
          else: # Нарушение правила "4 пробела"
                Shuffler.rename(args.dirname, args.output) # Нарушение правила "4 пробела"
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
