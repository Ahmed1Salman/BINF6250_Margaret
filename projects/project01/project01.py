#!/usr/bin/env python
from pprint import pprint
from symbol import continue_stmt


# Modify this function signature and fill in the details
def parse_line(line: str):
    # splits line by tabs, takes last item (all the info starting with ALLELEID)
    new_line = line.rstrip().split('\t')[-1]
    # split new_line by ;, list
    gene_info = new_line.split(';')

    # TODO: how to find AF_EXAC (not is same place in each list)
    if "AF_EXAC" in gene_info:
        pos = gene_info.index('AF_EXAC')
        AFC_EXAC = gene_info[pos]
        print(AFC_EXAC)
    # TODO: find CLNDN
    #CLNDN = gene_info.find('CLNDN')
    #if CLNDN != -1:

    # initialize empty list to add rare genes to
    #rare_genes = []
    #if AF_EXAC < 0.0001:
     #   if CLNDN == "not_specified" or CLNDN == "not_provided":
      #      continue
      #  else:
      #      rare_genes.append(CLNDN)

    print(gene_info)


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
