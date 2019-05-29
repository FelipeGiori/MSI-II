#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def str2tupleList(s):
    return eval("[%s]" % s)[0]

def str2List(s):
    return s.split(" ")

def sumOfSquares(lst):
    tmp = 0
    for n in lst:
        tmp = tmp + float(n)**2

    return tmp