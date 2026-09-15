#!/usr/bin/env python
from pprint import pprint
from unittest import skip


# Modify this function signature and fill in the details
def parse_line(line:str):

    if 'AF_EXAC' in line:
        info_line = line.split('\t')[7].split(';')
        af_exac = float(extract_data_from_info(info_line, 'AF_EXAC'))
        clndn = extract_data_from_info(info_line, 'CLNDN')
        clndn = clndn.split('|')
    else:
        af_exac = 1
    if af_exac < 0.0001:
        rare_disease = clndn
    else:
        rare_disease = []

    return rare_disease





# Modify this function signature and fill in the details
def read_file(file_name:str):
    with open(file_name,"r") as f:
        disease_dict = {}
        for line in f:
            if line.startswith('#'):
                continue
            else:
                disease_list = parse_line(line)
                for disease in disease_list:
                    if disease in disease_dict.keys():
                        disease_dict[disease] += 1
                    else:
                        disease_dict[disease] = 1
        disease_dict.pop('not_provided')
        disease_dict.pop('not_specified')
        return disease_dict

def extract_data_from_info(info:list, metadata:str):
    #Extract the relevant data from the info line given a Metadata requirement such as
    #AF_EXAC or CLNDN.

    values = [data for data in info if metadata in data]
    clean_data = values[0].split('=')[1]
    return clean_data


if __name__ == "__main__":
    pprint(read_file("clinvar_20190923_short.vcf"))
