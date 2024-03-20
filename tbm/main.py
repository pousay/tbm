import argparse
from .help import help
from .build import build
from .run import run


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command")

    subparsers.add_parser("build", help="build base files")
    subparsers.add_parser("help", help="help command")
    subparsers.add_parser("run", help="run your bot")

    args = parser.parse_args()

    if args.command == "build":
        build()
    elif args.command is None or args.command == "help":
        help()
    elif args.command == "run":
        run()

    else:
        print("invalid command, use 'pyro-admin help' to get help")
