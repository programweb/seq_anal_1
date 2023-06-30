# seq_anal_1
Sequence Analysis

I downloaded a list of genes from part of the mouse genome. This is data 
from the UCSC genome browser that maintains genomic information across many 
organisms as they have been sequenced.  

DNA sequences encode proteins using a three-letter alphabet such that each of 
the 20 amino acids that comprise protein sequences is represented by a distinct 
set of 3-letter nucleic acid combinations. 

Translation of the protein occurs at the start codon, represented by the three 
base pairs ATG.  We can identify where translation begins in the Cntn4 gene 
sequence using the index command, built into the Python string library:

>>cntn4_seq.index('ATG')

- - -
With the developments in whole-genome sequencing, we can not only study the coding 
regions of the DNA - those that encode for proteins - but also the millions of 
basepairs that DO NOT encode for proteins.

Why would these regions be of interest? Because they contain regulatory regions that 
help turn genes on and off.  These regions, often conserved across evolution, are 
tuned to enable the binding of specific proteins that can kick-start the process of 
transcription. 
