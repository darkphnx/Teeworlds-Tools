#!/usr/bin/python

import os

print "Content-type: text/plain\r\n"

maps = os.listdir("/usr/share/games/teeworlds/data/maps/")

for mapfile in sorted(maps):
    print mapfile.rstrip('.map')
