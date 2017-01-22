#!usr/opt/lib
#!encoding: utf-8

import math

def dist3D(val, ref):
    x = (val[0] - ref[0])*(val[0] - ref[0])
    y = (val[1] - ref[1])*(val[1] - ref[1])
    z = (val[2] - ref[2])*(val[2] - ref[2])

    return math.sqrt(x + y + z)

def dist2D(p1, p2):
    return math.sqrt((p1[0] - p2[0])*(p1[0] - p2[0]) +(p1[1] - p2[1])*(p1[1] - p2[1]))
