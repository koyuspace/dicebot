#!/usr/bin/python3
# -*- coding: utf-8 -*-

def fa(num):
    switcher = {
        1: chr(0xf525),
        2: chr(0xf528),
        3: chr(0xf527),
        4: chr(0xf524),
        5: chr(0xf523),
        6: chr(0xf526)
    }
    return switcher.get(num, None)

def words(num):
    switcher = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six"
    }
    return switcher.get(num, None)