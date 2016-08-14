#! /usr/bin/env python3
# -*- coding: utf-8 -*-

import os

currentdir = os.path.dirname(os.path.abspath(__file__))
txtdir_relpath = '../data/txt'
txtdir = os.path.normpath(os.path.join(currentdir, txtdir_relpath))

for dataset in ['train','dev','test']:
    with open('../data/snli/snli_1.0/snli_1.0_' + dataset + '.txt', 'r') as fi:
        next(fi) # skip the first line
        for l in fi:
            gold_label, _, _, _, _, sentence1, sentence2, _, pairID = l.split('\t')[:9]
            if gold_label not in ['entailment','neutral','contradiction']:
                print(dataset + ', ' + gold_label + ', ' + pairID)
                continue
            with open(txtdir + '/' + dataset + '/' + gold_label + '/' + pairID + '.txt', 'w') as fo:
                fo.write(sentence1 + '\n' + sentence2 + '\n')
