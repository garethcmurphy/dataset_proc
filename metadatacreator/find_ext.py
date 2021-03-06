#!/usr/bin/env python3
"""find extensions"""
import itertools
import json
import os

import collections
from collections import OrderedDict

def find_extensions():
    """find extensions"""
    root = './'
    files = itertools.chain.from_iterable((
        files for _, _, files in os.walk(root)
    ))
    counter = collections.Counter(
        (os.path.splitext(file_)[1] for file_ in files)
    )
    # counter_sorted= sorted(counter, key=counter.get)
    # for w in sorted(counter, key=counter.get, reverse=True):
    #  print w, counter[w]


    sorted_count = OrderedDict(sorted(counter.items(), key=lambda t: t[1], reverse=True))

    print(json.dumps(sorted_count, indent=2))
