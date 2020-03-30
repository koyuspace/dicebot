#!/usr/bin/python3
# -*- coding: utf-8 -*-

def fa(num, max):
    switcher = {
        1: chr(0xf525),
        2: chr(0xf528),
        3: chr(0xf527),
        4: chr(0xf524),
        5: chr(0xf523),
        6: chr(0xf526)
    }
    if max == 4:
        return chr(0xf6d0)
    elif max == 8:
        return chr(0xf6d2)
    elif max > 6:
        return chr(0xf6cf)
    else:
        return switcher.get(num, None)

def words(num, max):
    switcher = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six"
    }
    if max > 6:
        return str(num)
    else:
        return switcher.get(num, None)

def emoji(num):
    if num <= 6:
        return "🎲"
    else:
        return ""