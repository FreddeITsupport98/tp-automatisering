import argparse
parser = argparse.ArgumentParser()
parser.add_argument("-f", "--file", help="Full file name of CSV file.")
args = parser.parse_args()

filehandle = ""

if args.file:
  filehandle = args.file
else:
  filehandle = input(".csv file to read: ")

print(filehandle)