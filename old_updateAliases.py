import urllib2
import json


members = json.loads(urllib2.urlopen("http://sheetsu.com/apis/2abe8f64").read())


import argparse
import subprocess
import time

mailingLists = [
    "pepoff",
    "drumline",
    "sectionleaders",
    "pepfun",
    "pep-band",
    "highwoodwinds",
    "middlewinds",
    "lowbrass",
    "trumpets",
    "colorguard",
    "marching",
    "clarinets",
    "flutes",
    "stands",
    "pit",
    "pep16",
    "pep17",
    "pep18",
    "pep19",
    "drummajors",
    "highwoodwinds-marching",
    "middlewinds-marching",
    "lowbrass-marching",
    "trumpets-marching",
    "clarinets-marching",
    "flutes-marching",
    "drumline-marching",
    "pit-marching",
    "stands"]

subprocess.call(["rm", "-f", "-r", "oldMailingLists"])

subprocess.call(["python", "grabAllMailingLists.py"])

subprocess.call(["rm", "-f", "-r", "newMailingLists"])
subprocess.call(["mkdir", "newMailingLists"])

pepFunOut = open('newMailingLists/pepfun', 'w')
marchingOut = open('newMailingLists/marching', 'w')
standsOut = open('newMailingLists/stands', 'w')
sectionLeaderOut = open('newMailingLists/sectionleaders', 'w')
officerOut = open('newMailingLists/pepoff', 'w')
colorguardOut = open('newMailingLists/colorguard', 'w')
pepBandOut = open('newMailingLists/pep-band', 'w')
clarinetsOut = open('newMailingLists/clarinets', 'w')
highwoodwindsOut = open('newMailingLists/highwoodwinds', 'w')
flutesOut = open('newMailingLists/flutes', 'w')
trumpetsOut = open('newMailingLists/trumpets', 'w')
middlewindsOut = open('newMailingLists/middlewinds', 'w')
lowbrassOut = open('newMailingLists/lowbrass', 'w')
drumlineOut = open('newMailingLists/drumline', 'w')
pitOut = open('newMailingLists/pit', 'w')
pep16 = open('newMailingLists/pep16', 'w')
pep17 = open('newMailingLists/pep17', 'w')
pep18 = open('newMailingLists/pep18', 'w')
pep19 = open('newMailingLists/pep19', 'w')
drummajorsOut = open('newMailingLists/drummajors', 'w')
highwoodwinds_marching = open('newMailingLists/highwoodwinds-marching', 'w')
middlewinds_marching = open('newMailingLists/middlewinds-marching', 'w')
lowbrass_marching = open('newMailingLists/lowbrass-marching', 'w')
trumpets_marching = open('newMailingLists/trumpets-marching', 'w')
clarinets_marching = open('newMailingLists/clarinets-marching', 'w')
flutes_marching = open('newMailingLists/flutes-marching', 'w')
drumline_marching = open('newMailingLists/drumline-marching', 'w')
pit_marching = open('newMailingLists/pit-marching', 'w')
stands_only = open('newMailingLists/stands', 'w')


def toEmail(name, email):
    return (name + ' <'+email+'>\n');


def assignStands(name, email, stands):
    if(stands == "clarinets"):
        clarinetsOut.write(toEmail(name, email));
        highwoodwindsOut.write(toEmail(name, email));
    if(stands == "flutes"):
        flutesOut.write(toEmail(name, email));
        highwoodwindsOut.write(toEmail(name, email));
    if(stands == "trumpets"):
        trumpetsOut.write(toEmail(name, email));
    if(stands == "middlewinds"):
        middlewindsOut.write(toEmail(name, email));
    if(stands == "lowbrass"):
        lowbrassOut.write(toEmail(name, email));
    if(stands == "drumline"):
        drumlineOut.write(toEmail(name, email));
    if(stands == "drumline"):
        pitOut.write(toEmail(name, email));
    if(stands == "colorguard"):
        colorguardOut.write(toEmail(name, email));
    if(stands == "drummajors"):
        drummajorsOut.write(toEmail(name, email));

def assignMarching(name, email, marching):
    marchingOut.write(toEmail(name, email));
    if(marching == "clarinets"):
        clarinets_marching.write(toEmail(name, email));
        highwoodwinds_marching.write(toEmail(name, email));
    if(marching == "flutes"):
        flutes_marching.write(toEmail(name, email));
        highwoodwinds_marching.write(toEmail(name, email));
    if(marching == "trumpets"):
        trumpets_marching.write(toEmail(name, email));
    if(marching == "middlewinds"):
        middlewinds_marching.write(toEmail(name, email));
    if(marching == "lowbrass"):
        lowbrass_marching.write(toEmail(name, email));
    if(marching == "drumline"):
        drumline_marching.write(toEmail(name, email));
    if(marching == "drumline"):
        pit_marching.write(toEmail(name, email));
    if(marching == "colorguard"):
        colorguardOut.write(toEmail(name, email));




for i in members['result']:

    name = i['Name']
    if(name == "name"):
        continue;
    email = i['Email']
    isPepFun = i['pepfun']
    marching = i['marching']
    isOnlyStands = i['stands only']
    standsSection = i['stands section']
    isSectionLeader = i['sectionleaders']
    isOfficer = i['pepoff']
    isPepBand = i['pep-band']
    isPep16 = i['pep16']
    isPep17 = i['pep17']
    isPep18 = i['pep18']
    isPep19 = i['pep19']
    if(isPepFun == "x"):
        pepFunOut.write(toEmail(name, email));
    if(isOnlyStands == "x"):
        stands_only.write(toEmail(name, email));
    if(isSectionLeader == "x"):
        sectionLeaderOut.write(toEmail(name, email));
    if(isOfficer == "x"):
        officerOut.write(toEmail(name, email));
    if(isPepBand == "x"):
        pepBandOut.write(toEmail(name, email));
    if(marching != ""):
        assignMarching(name, email, marching);
    assignStands(name, email, standsSection);
    if(isPep16 == "x"):
        pep16.write(toEmail(name, email));
    if(isPep17 == "x"):
        pep17.write(toEmail(name, email));
    if(isPep18 == "x"):
        pep18.write(toEmail(name, email));
    if(isPep19 == "x"):
        pep19.write(toEmail(name, email));


pepFunOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
marchingOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
standsOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
sectionLeaderOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
officerOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
pepBandOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
clarinetsOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
highwoodwindsOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
flutesOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
trumpetsOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
middlewindsOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
lowbrassOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
drumlineOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
pitOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
colorguardOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
drummajorsOut.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
pep16.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
pep17.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
pep18.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
pep19.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
highwoodwinds_marching.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
middlewinds_marching.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
lowbrass_marching.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
trumpets_marching.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
clarinets_marching.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
flutes_marching.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
drumline_marching.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
pit_marching.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));
stands_only.write(toEmail("Sam Mailand", "sfmailand@wpi.edu"));

pepFunOut.close()
marchingOut.close()
standsOut.close()
sectionLeaderOut.close()
officerOut.close()
pepBandOut.close()
clarinetsOut.close()
highwoodwindsOut.close()
flutesOut.close()
trumpetsOut.close()
middlewindsOut.close()
lowbrassOut.close()
drumlineOut.close()
pitOut.close()
colorguardOut.close()
drummajorsOut.close();
pep16.close();
pep17.close();
pep18.close();
pep19.close();
highwoodwinds_marching.close();
middlewinds_marching.close();
lowbrass_marching.close();
trumpets_marching.close();
clarinets_marching.close()
flutes_marching.close()
pit_marching.close()
drumline_marching.close()
stands_only.close();


for list in mailingLists:
    subprocess.call(["scp", "newMailingLists/"+list, "sfmailand@ccc.wpi.edu:/shared/aliases/"+list])
