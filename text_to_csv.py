import argparse
import subprocess

def textFile(value):

    return value



parser = argparse.ArgumentParser(description = 'Process a given [inFileName].txt and outputs [fileName].csv')
parser.add_argument("inFileName", help="The path to the input text file", type=textFile)
args = parser.parse_args()

inFileName = args.inFileName

subprocess.call(["scp", "sfmailand@ccc.wpi.edu:/shared/aliases/"+"pep-band", "pep-band"])
infile = open(inFileName, 'r')

inFileName = inFileName.replace(".csv", "")
out = open(inFileName+'.csv', 'w')

line = infile.readline()

while line != "":
	if "<" in line:
		tmp = line.split("<")
		name = tmp[0];
		email = tmp[1];
		email = email.replace('>', '')
		out.write(name + "," + email)

	line = infile.readline()

out.close()

subprocess.call(["rm", inFileName])
