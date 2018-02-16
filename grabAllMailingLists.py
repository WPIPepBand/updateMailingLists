
import subprocess
import time

mailingLists = [
    "pepoff",
    "pepalum",
    "drumline",
    "gamemaster",
    "sectionleaders",
    "pepfun",
    "pep-band",
    "highwoodwinds",
    "middlewinds",
    "lowbrass",
    "trumpets",
    "colorguard",
    "marching",
    "fieldstaff",
    "drummajors",
    "clarinets",
    "flutes",
    "marchingevents",
    "standsevents",
    "pepassmaster",
    "stands",
    "pit",
    "pep-freshmen",
    "pep-sophomores",
    "pep-juniors",
    "pep-seniors",
    "highwoodwinds-marching",
    "middlewinds-marching",
    "lowbrass-marching",
    "trumpets-marching",
    "clarinets-marching",
    "flutes-marching",
    "drumline-marching",
    "pit-marching",
    "stands",
    "winterguard"]


subprocess.call(["mkdir", "oldMailingLists"])

for list in mailingLists:
    subprocess.call(["scp", "sfmailand@ccc.wpi.edu:/shared/aliases/"+list, "oldMailingLists/."])
