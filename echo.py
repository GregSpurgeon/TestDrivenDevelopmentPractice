#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""An enhanced version of the 'echo' cmd line utility."""

__author__ = "Greg Spurgeon"


import sys
import argparse


def create_parser():
    """Returns an instance of argparse.ArgumentParser"""
    parser = argparse.ArgumentParser(
        description="Perform transformation on input text.")
    parser.add_argument('-u', '--upper', action="store_true",
                        help="convert text to uppercase")
    parser.add_argument('-l', '--lower', action="store_true",
                        help="convert text to lowercase")
    parser.add_argument('-t', '--title', action="store_true",
                        help="convert text to titlecase")
    parser.add_argument('text', help="text to be manipulated")
    return parser


def main(args):
    """Implementation of echo"""
    parse_obj = create_parser()
    ns = parse_obj.parse_args(args)
    text = ns.text
    if ns.lower:
        text = text.lower()
    if ns.upper:
        text = text.upper()
    if ns.title:
        text = text.title()
    print(text)


if __name__ == '__main__':
    main(sys.argv[1:])
