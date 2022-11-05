import sys
import os
import hashlib
import ast
import argparse
import time # Лучше не использовать * при импорте


class shuffler:

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = [] # Исправил уровень вложенности
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename((path + '/' + mp3), path + '/' + hashname) # Путаница со скобочками
        with open(output, 'w') as f: # Файл открывался на чтение, при этом в него пытались записать.
            f.write(str(self.map)) # Файл не закрывался, решил обернуть в with

    def restore(self, dirname, restore_path):
        with open("./filename", '+') as f: #не совсем понятно что за переменная filename, рискну предположить что это путь
            self.map = ast.literal_eval(f.read())
        mp3s = []
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s:
            os.rename((path + '/' + hashname), (path + '/' + self.map[hashname]))
            os.remove(restore_path)
                
    def generateName(self, seed=time.time()): # Так как импорт time теперь без *, метод time() нужно вызывать с указанием библиотеки
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
    match args.subcommand:
        case 'rename':
            if args.output:
                Shuffler.rename(args.dirname, 'restore.info')
            else:
                Shuffler.rename(args.dirname, args.output)
        case 'restore':
            Shuffler.restore(args.dirname, args.restore_map)
        case _:
            sys.exit()
    # Сделал match/case из вот этого
    # if args.subcommand == 'rename':
    #       if args.output:
    #             Shuffler.rename(args.dirname, 'restore.info')
    #       else:
    #             Shuffler.rename(args.dirname, args.output)
    # elif args.subcommand == 'restore':
    #     Shuffler.restore(args.dirname, args.restore_map)
    # else:
    #     sys.exit()


main()
