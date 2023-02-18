from Bio.Seq import Seq

# Create a Seq object for the DNA sequence
dna_seq = Seq("ATGCAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC")

# Find the ORFs in the sequence
orfs = dna_seq.translate()

# Print the ORFs
print("ORFs: ", orfs)

