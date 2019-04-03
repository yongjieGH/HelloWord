#!/usr/bin/env python
########################################################################
# 
# Copyright (c) 2019 Baidu.com, Inc. All Rights Reserved
# 
########################################################################
 
"""
File: test.py
Author: tianyongjie(tianyongjie@baidu.com)
Date: 2019/04/03 10:31:41
"""
import sys
import json

for line in sys.stdin:
    line = line.strip().decode('gb18030')
    cols = line.split('\t')
    print (cols[0] + '\t1').encode('utf-8')
