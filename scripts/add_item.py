#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse

parser = argparse.ArgumentParser(prog="add-item")

parser.add_argument("title", type=str)
parser.add_argument("url", type=str)
parser.add_argument("tags", nargs="+", type=str)


if __name__ == "__main__":
  args = parser.parse_args()
  with open("bookshelf.tsv", "a") as f:
    tags = "\t".join(args.tags)
    N = 17
    current_n = len(args.tags) + 2
    f.write("\t".join([args.title, args.url, tags] + [""]*(N-current_n)))

