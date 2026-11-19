"""Command line entry point for pizazzpartner0o_kit."""
import argparse
import sys

from .core import Pizazzpartner0oTool


def main(argv=None):
    parser = argparse.ArgumentParser(description="check JSON syntax")
    parser.add_argument("files", nargs="+")
    parser.add_argument("--quiet", action="store_true")
    args = parser.parse_args(argv)
    checker = Pizazzpartner0oTool()
    failed = 0
    for path in args.files:
        ok, payload = checker.check(path)
        if ok:
            if not args.quiet:
                print(payload)
        else:
            failed += 1
            print(f"{path}: {payload}", file=sys.stderr)
    return 1 if failed else 0
