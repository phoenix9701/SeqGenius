from Bio import Align
aligner = Align.PairwiseAligner()

# Define the DNA sequences to align
seq1 = "ATGCAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"
seq2 = "ATGCAACTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC"

alignments = aligner.align (seq1, seq2)

# Perform the alignment
for alignment in alignments:
    print(alignment)


