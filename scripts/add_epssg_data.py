#!/usr/bin/env python3
import sys
import argparse
import json

parser = argparse.ArgumentParser()
args = parser.parse_args()

spacecrafts = json.load(open("spacecrafts.data.json", "rb"))

vcids = [
   (8, "HK-TM", "ab"),
   (9, "Platform Ancillary", "ab"),
   (10, "ADMIN DDB message", "ab"),
   (11, "RO", "ab"),
   (12, "IASI-NG", "a"),
   (13, "MWS", "a"),
   (14, "3MI", "a"),
   (15, "Sentinal 5", "a"),
   (16, "METImage", "a"),
   (17, "SPARE", "a"),
   (18, "MWI", "b"),
   (19, "ADCS", "b"),
   (20, "SCA", "b"),
   (21, "ICI", "b"),
   (22, "SPARE", "b"),
]

apids = [
    (0x00, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x0A, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x0B, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x0C, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x0D, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x0E, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x0f, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x29, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x2f, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x32, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x35, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x36, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x3c, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x3d, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x43, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x44, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x4a, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x4b, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x51, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x52, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x58, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x59, None, 8, "HK-TM", "spacecraft", "ab"),
    (0x24, 0x00, 9, "Platform Anillary Data (NAVATT)", "spacecraft", "ab"),
    (0x24, 0x01, 10, "ADMIN DDB message (MMAM)", "spacecraft", "ab"),
    (0x37, None, 11, "Science Data", "ro", "ab"),
    (0x38, None, 11, "Calibration Data", "ro", "ab"),
    (0x3e, None, 12, "NSD data", "iasi-ng", "a"),
    (0x3f, None, 12, "Check mode", "iasi-ng", "a"),
    (0x45, None, 13, "Science data", "mws", "a"),
    (0x46, None, 13, "Calibration", "mws", "a"),
    (0x4c, None, 14, "Science data", "3mi", "a"),
    (0x4d, None, 14, "Calibration data", "3mi", "a"),
    (0x53, None, 15, "Science data", "sentinal5", "a"),
    (0x54, None, 15, "Calibration data", "sentinal5", "a"),
    (0x5a, None, 16, "Science data", "metimage", "a"),
    (0x5b, None, 16, "Calibration data", "metimage", "a"),
    (0x45, None, 18, "Science data", "mwi", "b"),
    (0x45, None, 18, "Calibration data", "mwi", "b"),
    (0x4c, None, 19, "Science data", "adcs", "b"),
    (0x4d, None, 19, "Calibration data", "adcs", "b"),
    (0x53, None, 20, "Science data", "sca", "b"),
    (0x54, None, 20, "Calibration data", "sca", "b"),
    (0x5a, None, 21, "Science data", "ici", "b"),
    (0x5b, None, 21, "Calibration data", "ici", "b"),
]


# set CDS timecode at 0 byte of secondary header for all JPSS science and usuall SC data
for sc in [s for s in spacecrafts if s["scid"] in (3, 27, 48, 66, 70, 71)]:
    sat_vcids = []
    sat_apids = []
    if "a" in sc["name"]:
        sat_vcids = [v for v in vcids if "a" in v[-1]]
        sat_apids = [a for a in apids if "a" in a[-1]]
    if "b" in sc["name"]:
        sat_vcids = [v for v in vcids if "b" in v[-1]]
        sat_apids = [a for a in apids if "b" in a[-1]]

    for vcid in sat_vcids:
        dat = {"vcid": vcid[0], "description": vcid[1], "apids": []}
        sc["vcids"].append(dat)

    for apid in sat_apids:
        num = apid[0]
        cat = apid[1]
        vcid = apid[2]
        desc = apid[3]
        sensor = apid[4]
        if cat is not None:
            dat = {"apid": (num << 4), "description": desc, "sensor": sensor}
        else:
            vcid = [v for v in sc["vcids"] if v["vcid"] == vcid][0]
            for i in range(15):
                dat = {"apid": (num << 4) | i, "description": desc, "sensor": sensor}
                vcid["apids"].append(dat)


json.dump(spacecrafts, sys.stdout, indent=2)
