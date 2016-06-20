# -*- coding: utf-8 -*-

import csv
import json
import os
import time
import urllib
import urllib2

# get materials
materials_file = "manifest.csv"
materials = []
with open(materials_file, 'rb') as f:
    r = csv.DictReader(f)
    for row in r:
        materials.append(row)
print "%s items found" % len(materials)

def printInfo(item):

    # download the transcript
    response = urllib2.urlopen(item["transcript_json"])
    transcript = json.load(response)
    print "Loaded the transcript for %s from collection %s" % (item["title"], item["collection_title"])

    # print duration
    print "The duration is: %s" % time.strftime("%H:%M:%S", time.gmtime(transcript["duration"]))

    # get the word count
    lines = [l["best_text"] for l in transcript["lines"]]
    content = " ".join(lines)
    words = content.split(" ")
    print "The word count is: %s" % len(words)

    # download the audio file
    print "Downloading audio file..."
    filename = os.path.basename(item["audio"])
    urllib.urlretrieve(item["audio"], filename)
    fileBytes = os.path.getsize(filename)
    print "Downloaded %s with size %sMB" % (filename, round(0.000001 * fileBytes))

# take the first item as an example
example = materials[0]
printInfo(example)
