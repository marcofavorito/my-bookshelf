#!/usr/bin/env python

import fileinput

if __name__ == "__main__":
 for line in fileinput.input("bookshelf.tsv", inplace=True, backup='.bak'):
   l = line.strip().split("\t")
   size = 17 
   l = l + [""]*(size - len(l))
   print("\t".join(l))

