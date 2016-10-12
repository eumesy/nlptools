#! /usr/bin/env python3
# -*- coding: utf-8; mode: Python -*-

import argparse
import os

def main():
    with open(args.path_to_src, 'r') as fi:
        for i,l in enumerate(fi):
            if l == '\n':
                continue
            with open(os.path.join(args.path_to_output_dir, '{}.txt'.format(i)), 'w') as fo:
                s1, s2 = l.rstrip().split('\t')
                fo.write(s1 + '\n')
                fo.write(s2 + '\n')

if __name__ == '__main__':
    # parser
    parser = argparse.ArgumentParser(description='Split the text including tab-separated sentence pairs s.t. `s11\t s12\n s21\t s22\n ... to indivisual texts s.t. `s1\n s2\n[EOF]`')
    parser.add_argument('path_to_src')
    parser.add_argument('path_to_output_dir')
    args = parser.parse_args()

    main()
