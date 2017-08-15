import csv
import json
import argparse
import subprocess
import time

f = open("Email aliases (For script) - Sheet1.csv")
members = csv.DictReader(f)

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
    "pep-seniors",
    "pep-juniors",
    "pep-sophomores",
    "pep-freshmen",
    "drummajors",
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

print("UPDATING MAILING LISTS")
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
pepSeniors = open('newMailingLists/pep-seniors', 'w')
pepJuniors = open('newMailingLists/pep-juniors', 'w')
pepSophomores = open('newMailingLists/pep-sophomores', 'w')
pepFreshmen = open('newMailingLists/pep-freshmen', 'w')
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
winterGuard = open('newMailingLists/winterguard', 'w')
def toEmail(name, email):
    return name + ' <' + email + '>\n';


def assignStands(name, email, stands):
    if stands == "clarinets":
        clarinetsOut.write(toEmail(name, email));
        highwoodwindsOut.write(toEmail(name, email));
    if stands == "flutes":
        flutesOut.write(toEmail(name, email));
        highwoodwindsOut.write(toEmail(name, email));
    if stands == "trumpets":
        trumpetsOut.write(toEmail(name, email));
    if stands == "middlewinds":
        middlewindsOut.write(toEmail(name, email));
    if stands == "lowbrass":
        lowbrassOut.write(toEmail(name, email));
    if stands == "drumline":
        drumlineOut.write(toEmail(name, email));
    if stands == "drumline":
        pitOut.write(toEmail(name, email));
    if stands == "colorguard":
        colorguardOut.write(toEmail(name, email));
    if stands == "drummajors":
        drummajorsOut.write(toEmail(name, email));


def assignMarching(name, email, marching):
    marchingOut.write(toEmail(name, email));
    if marching == "clarinets":
        clarinets_marching.write(toEmail(name, email));
        highwoodwinds_marching.write(toEmail(name, email));
    if marching == "flutes":
        flutes_marching.write(toEmail(name, email));
        highwoodwinds_marching.write(toEmail(name, email));
    if marching == "trumpets":
        trumpets_marching.write(toEmail(name, email));
    if marching == "middlewinds":
        middlewinds_marching.write(toEmail(name, email));
    if marching == "lowbrass":
        lowbrass_marching.write(toEmail(name, email));
    if marching == "drumline":
        drumline_marching.write(toEmail(name, email));
    if marching == "drumline":
        pit_marching.write(toEmail(name, email));
    if marching == "colorguard":
        colorguardOut.write(toEmail(name, email));

for i in members:
    name = i['Name']
    if name == "name":
        continue
    email = i['Email']
    isPepFun = i['pepfun']
    marching = i['marching']
    isOnlyStands = i['stands only']
    standsSection = i['stands section']
    isSectionLeader = i['sectionleaders']
    isOfficer = i['pepoff']
    isPepBand = i['pep-band']
    isSenior = i['seniors']
    isJunior = i['juniors']
    isSophomore = i['sophomores']
    isFreshmen = i['freshmen']
    isWinterGuard = i['winterguard']
    if isPepFun == "x":
        pepFunOut.write(toEmail(name, email))
    if isOnlyStands == "x":
        stands_only.write(toEmail(name, email))
    if isSectionLeader == "x":
        sectionLeaderOut.write(toEmail(name, email))
    if isOfficer == "x":
        officerOut.write(toEmail(name, email))
    if isPepBand == "x":
        pepBandOut.write(toEmail(name, email))
    if marching != "":
        assignMarching(name, email, marching)
    assignStands(name, email, standsSection)
    if isSenior == "x":
        pepSeniors.write(toEmail(name, email));
    if isJunior == "x":
        pepJuniors.write(toEmail(name, email));
    if isSophomore == "x":
        pepSophomores.write(toEmail(name, email))
    if isFreshmen == "x":
        pepFreshmen.write(toEmail(name, email))
    if isWinterGuard == "x":
        winterGuard.write(toEmail(name, email))


  
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
pepSeniors.close();
pepJuniors.close();
pepSophomores.close();
pepFreshmen.close();
highwoodwinds_marching.close();
middlewinds_marching.close();
lowbrass_marching.close();
trumpets_marching.close();
clarinets_marching.close()
flutes_marching.close()
pit_marching.close()
drumline_marching.close()
stands_only.close();
winterGuard.close();
'''
for list in mailingLists:
    subprocess.call(["scp", "newMailingLists/"+list, "dkaravoussianis@ccc.wpi.edu:/shared/aliases/"+list])
'''

os.chdir("newMailingLists")

command = ["scp"]
for alias in mailingLists:
    command.append(alias)
command.append("dkaravoussianis@ccc.wpi.edu:/shared/aliases/")

subprocess.call(command)
