import argparse


def parse_args():
    parser = argparse.ArgumentParser(description='Searches for pattern in image')
    parser.add_argument('-a', '--a_arg', help='Полезный аргумент а_arg')
    parser.add_argument('-b', '--b_arg', help='Еще один аргумент b_arg')
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_args()
    print(f"{args.a_arg=}")
    print(f"{args.b_arg=}")
