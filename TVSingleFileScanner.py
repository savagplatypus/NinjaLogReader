import os
import re
import sys
import argparse

searchfile = open("logs test.txt", "r")
for line in searchfile:
    if "CLSID" in line: print (line)
searchfile.close()
