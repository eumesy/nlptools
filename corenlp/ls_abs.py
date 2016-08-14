#! /usr/bin/env python3
# -*- coding: utf, mode: Python -*-

import os
import argparse

def main():
    textfiles_dir_abspath = os.path.abspath(args.path_textfiles_dir)

    for filename in os.listdir(textfiles_dir_abspath):
        print(textfiles_dir_abspath + '/' + filename)

if __name__ == '__main__':
    # parser
    parser = argparse.ArgumentParser(description='list up absolute paths of files in dir')
    parser.add_argument('path_textfiles_dir', type=str)
    args = parser.parse_args()

    main()
