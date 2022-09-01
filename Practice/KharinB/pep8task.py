import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler: #Класс пишется CamelCase

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
         mp3s = []
        for root, directories, files in os.walk(dirname):  #Из-за инициализации переменной mp3s не распознаёт dirname, не знаю почему.
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file]) #Рискну предположить что переменная не иницилиализирована из-за косяка с отступами выше
        for path, mp3 in mp3s: #переменная не иницилиализирована
            hashname = self.generateName() + '.mp3'#Из-за инициализации переменной mp3s не распознаёт self
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname)) #Скобка не в ту сторону, hashname()
          f = open(output, 'r') #Лишние отступы (если файл нужно открыть несколько раз, то наоборот отступов не хватает)
          f.write(str(self.map))#Из-за инициализации переменной mp3s не распознаёт self, и отступы.

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f: #Переменная filename не инициализирована. Неверное количество отступов
            self.map = ast.literal_eval(f.read())
          mp3s = []#Неверное количество отступов
        for root, directories, files in os.walk(dirname):#Тут не знаю почему не работает, даже с верным количеством отступов у mp3s не распознаётся.
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file}) #переменная не иницилиализирована
        for path, hashname in mp3s: #переменная не иницилиализирована
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))#из-за инициализации mp3s не читает self, не хватает скобки self.map[hashname]())
        os.remove(restore_path) #неверное количество отступов, должно быть больше?
                
     def generateName(self, seed=time()):
          return hashlib.md5(str(seed)).hexdigest() #Вообще не знаю что тут происходит...)))


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
