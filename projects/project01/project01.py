#!/usr/bin/env python
from pprint import pprint


# Modify this function signature and fill in the details
def parse_line(line: str)
    pass


# Modify this function signature and fill in the details
def read_file(file: str):
    with open(file) as f:
        for line in f:
            if (line.startswith("#")): continue  # filters out metadata lines
            #print(line)
            # pass to parse_line to extract needed data
            parse_line(line)



if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))
