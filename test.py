#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 20 15:57:40 2021

@author: seara
"""

from qbwPythonModule import *
import numpy as np

gene_file='mm9_sel_chroms_knownGene.txt'
fopen=open(gene_file).readlines()


print( len(fopen) )
# print( fopen[0] )
# print( fopen[1999] )

gene_info=loadGeneFile(gene_file)
# The keys of the dictionary represent gene names. 
gene_names = gene_info.keys()
# print( gene_names )
# print( gene_info['uc012ajd.1'] )
# print( gene_info['uc009auw.1']['chr'] )
# print( gene_info['uc009auw.1']['start'] )

chroms=[]
for k in gene_info.keys():
    chr=gene_info[k]['chr']
    if chr not in chroms:
        chroms=chroms+[chr]
        
print( chroms ) # ['chr6', 'chr11', 'chr15', 'chr16']

gene_counts={}

for chr in chroms:
    chrom_count=0 
    for k in gene_info.keys():
        if gene_info[k]['chr']==chr:
            chrom_count+=1
    gene_counts[chr]=chrom_count


#Creates an empty set object. Sets are collections of unordered unique values.
in_gene=set()

#Looping through all the genes in chromosome 6, we find every sequence index assigned to the gene.
for gene in gene_info.keys():
    if gene_info[gene]['chr']=='chr6':
        gene_inds=range(gene_info[gene]['start'],gene_info[gene]['end'])
#Now we update the set with the indices of the current gene. Because it is a set, even if the indices were already entered as a different gene, we will not get duplicate entries.
        in_gene.update(gene_inds)
len(in_gene)

fa_file='selChroms_mm9.fa.zip'
seq_dict=loadFasta(fa_file)


# Create a boolean Numpy array the same length as the chromosome
# Initially, every entry will be False
chr6_length = len(seq_dict['chr6'])
in_gene_numpy = np.zeros(chr6_length, dtype=np.bool)
# Loop through the genes, switching entries to True if they are found
for gene in gene_info.keys():
    if gene_info[gene]['chr']=='chr6':
        start_ind = gene_info[gene]['start']
        end_ind = gene_info[gene]['end']
        in_gene_numpy[start_ind:end_ind] = True
# Get the answer by summing the Numpy array
# True values are treated as 1, False as 0, so the sum of the array will be the # number of index sites that are coding sites (the length of coding sequence in chr6)
num_in_gene = in_gene_numpy.sum()
print(num_in_gene)