from Bio import Restriction
from Bio.Seq import Seq

# Create a Seq object with the DNA sequence
dna_seq = Seq("GAATTC")

# Use the Restriction module to create an enzyme object
enzyme = Restriction.EcoRI

# Use the enzyme object to find the locations of the restriction sites in the DNA sequence
sites = enzyme.search(dna_seq)

# Print the restriction sites found
print(sites)