from sys import exit
import argparse
import os.path
import json
import yaml
import xml
import xmltodict

parser = argparse.ArgumentParser(description="Convert file formats.")
parser.add_argument("file1")
parser.add_argument("file2")

args = parser.parse_args()
format1 = args.file1.split("/")[-1].split("\\")[-1].split(".")[-1]
format2 = args.file2.split("/")[-1].split("\\")[-1].split(".")[-1]

if( not os.path.isfile(args.file1) ):
    print(f"{__file__.split('\')[-1]}:", "error: Nazwa pliku nie istnieje")
    exit()
if( not ((format1 == "xml" or format1 == "json" or format1 == "yml") and (format2 == "xml" or format2 == "json" or format2 == "yml")) ):
    print(f"{__file__.split('\')[-1]}:", "error: Nie wspierane rozszerzenie pliku")
    exit()
if( len(args.file1.split("/")[-1].split("\\")[-1].split(".")) == 1 or len(args.file1.split("/")[-1].split("\\")[-1].split(".")) == 1 ):
    print(f"{__file__.split('\')[-1]}:", "error: Nie wspierane rozszerzenie pliku")
    exit()


def postprocessor(path, key, value):
    try:
        return key, int(value)
    except (ValueError, TypeError):
        return key, value

match format1:
    case "xml":
        try:
            with open(args.file1, "r") as r_xml_file:
                data = list(xmltodict.parse(r_xml_file.read(), postprocessor=postprocessor).values())[0]
        except xml.parsers.expat.ExpatError as err:
            print(f"{args.file1.split('/')[-1].split('\')[-1]}:", err)
            exit()
    case "json":
        try:
            with open(args.file1, "r") as r_json_file:
                data = json.load(r_json_file)
        except ValueError as err:
            print(f"{args.file1.split('/')[-1].split('\')[-1]}:", err)
            exit()
    case "yml":
        try:
            with open(args.file1, "r") as r_yaml_file:
                data = yaml.safe_load(r_yaml_file)
        except yaml.YAMLError as err:
            print(f"{args.file1.split('/')[-1].split('\')[-1]}:", err)
            exit()


match format2:
    case "xml":
        with open(args.file2, "w") as w_xml_file:
            xmltodict.unparse({"root": data}, w_xml_file, pretty=True)
    case "json":
        with open(args.file2, "w") as w_json_file:
            json.dump(data, w_json_file, indent=4)
    case "yml":
        with open(args.file2, "w") as w_yaml_file:
            yaml.dump(data, w_yaml_file, sort_keys=False)
