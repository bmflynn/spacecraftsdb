#!/usr/bin/env python3
import sys
import argparse
import json

parser = argparse.ArgumentParser()
args = parser.parse_args()

spacecrafts = json.load(open("spacecrafts.data.json", "rb"))

# set CDS timecode at 0 byte of secondary header for all JPSS science and usuall SC data
for sc in [s for s in spacecrafts if s["scid"] in (157, 159, 177, 178, 179)]:
    for vcid in sc["vcids"]:
        for apid in vcid["apids"]:
            if apid["apid"] in [515, 528, 530, 531] + list(range(800, 829)) + list(
                range(1315, 1396)
            ) + [1289, 1290, 0, 8, 11, 30, 34, 37]:
                apid["timecodeFormat"] = {"format": "cds"}

# MODIS science data gets CDS
for sc in [s for s in spacecrafts if s["scid"] in [64, 154]]:
    for vcid in sc["vcids"]:
        for apid in vcid["apids"]:
            if apid["apid"] in [64]:
                apid["timecodeFormat"] = {"format": "cds"}

# GBAD gets CUC at byte offset 16, skipping p-field
for sc in [s for s in spacecrafts if s["scid"] in [154]]:
    for vcid in sc["vcids"]:
        for apid in vcid["apids"]:
            if apid["apid"] in [957]:
                apid["timecodeFormat"] = {"format": "cuc", "offset": 16}

json.dump(spacecrafts, sys.stdout, indent=2)
