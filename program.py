import argparse
import os.path

parser = argparse.ArgumentParser(description="Convert file formats.")
parser.add_argument("file1")
parser.add_argument("file2")

args = parser.parse_args()
format1 = args.file1.split("/")[-1].split("\\")[-1].split(".")[-1]
format2 = args.file2.split("/")[-1].split("\\")[-1].split(".")[-1]

if( not os.path.isfile(args.file1) ):
    print(f"{__file__.split("\\")[-1]}:", "error: Nazwa pliku nie istnieje")
    exit()
if( not ((format1 == "xml" or format1 == "json" or format1 == "yml") and (format2 == "xml" or format2 == "json" or format2 == "yml")) ):
    print(f"{__file__.split("\\")[-1]}:", "error: Nie wspierane rozszerzenie pliku")
    exit()
if( len(args.file1.split("/")[-1].split("\\")[-1].split(".")) == 1 or len(args.file1.split("/")[-1].split("\\")[-1].split(".")) == 1 ):
    print(f"{__file__.split("\\")[-1]}:", "error: Nie wspierane rozszerzenie pliku")
    exit()
