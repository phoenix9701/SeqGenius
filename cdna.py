from Bio.Seq import Seq

# Create a Seq object for the DNA strand
dna_strand = Seq("ATGCAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGCTAGC")

# Generate the complimentary DNA strand
complimentary_strand = dna_strand.complement()

print("Original DNA Strand: ", dna_strand)
print("Complimentary DNA Strand: ", complimentary_strand)