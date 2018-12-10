# This script prints the Single Cell Genome Total Weight and the Whole Organism Genome Total Weight

base_pair= input("Write n. base pairs: ")
genomic_copies= input("Write n. genomic copies: ")
cells_number= input ("Write average n. cells: ")
single_nucleotide_weight= 5.478*10**-10
pg= 'pg'
g= 'g'

SCGTW= (2)*(base_pair)*(single_nucleotide_weight)*(genomic_copies)

WOGTW= (2)*(base_pair)*(single_nucleotide_weight)*(genomic_copies)*(cells_number)/(10**12)

print("Single Cell Genome Total Weight: %s %s" %(SCGTW, pg))
print("Whole Organisms Genome Total Weight: %s %s" %(WOGTW, g))

for every in range(10):
	base_pair= input("Write n. base pairs: ")
	genomic_copies= input("Write n. genomic copies: ")
	cells_number= input ("Write average n. cells: ")
	SCGTW= (2)*(base_pair)*(single_nucleotide_weight)*(genomic_copies)
	WOGTW= (2)*(base_pair)*(single_nucleotide_weight)*(genomic_copies)*(cells_number)/(10**12)
	print("Single Cell Genome Total Weight: %s %s" %(SCGTW, pg))
	print("Whole Organisms Genome Total Weight: %s %s" %(WOGTW, g))
