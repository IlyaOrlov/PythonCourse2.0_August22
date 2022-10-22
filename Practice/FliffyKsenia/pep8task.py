import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler:   # надо назвать класс с большой буквы
    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = []                                             # сдвинуть на 2 пробела влево до правильного уровня кода и добавить пустую строку после для отделения области определения переменных от кода
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))  # убрать по одной лишней скобки после mp3 и hashname
          f = open(output, 'r')           # сдвинуть на два пробела вправо для правильного уровня кода.
          f.write(str(self.map))        # сдвинуть на два пробела вправо для правильного уровня кода.

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f:   # сдвинуть на 2 пробела влево до правильного уровня кода, откуда брать переменную filename  не нашла, но метод открытия надо поменять на r
            self.map = ast.literal_eval(f.read())
          mp3s = [] # сдвинуть на 2 пробела влево до правильного уровня кода
        for root, directories, files in os.walk(dirname):
            for file in files:
               if file[-3:] == '.mp3':  # сдвинуть на 1 пробела вправо до правильного уровня кода
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))  # убрать по одной лишней скобки после  hashname и ]
        os.remove(restore_path)
                
     def generateName(self, seed=time()):   # сдвинуть на 1 пробел влево до правильного уровня кода
          return hashlib.md5(str(seed)).hexdigest()  # сдвинуть на 2 пробела влево до правильного уровня кода


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
  # добавить еще одну пустую строку для лучшей читабельности.
def main():
    args = parse_arguments()
    Shuffler = shuffler()    # надо класс с большой буквы, а переменную с маленькой
    if args.subcommand == 'rename':
          if args.output:  # сдвинуть на 2 пробела влево до правильного уровня кода
                Shuffler.rename(args.dirname, 'restore.info')  # сдвинуть на 4 пробела влево до правильного уровня кода, надо shuffler с маленькой буквы
          else:  # сдвинуть на 2 пробела влево до правильного уровня кода
                Shuffler.rename(args.dirname, args.output)  # сдвинуть на 4 пробела влево до правильного уровня кода, надо shuffler с маленькой буквы
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)   # надо shuffler с маленькой буквы/
    else:
        sys.exit()


main()
