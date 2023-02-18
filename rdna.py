from Bio.Seq import Seq

# Create a Seq object for the DNA strand
dna_strand = Seq("ATGCAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC")

# Generate the reverse DNA strand
reverse_strand = dna_strand[::-1]

print("Original DNA Strand: ", dna_strand)
print("Reverse DNA Strand: ", reverse_strand)
