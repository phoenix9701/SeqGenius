from Bio.Seq import Seq

def dna_to_rna(dna_sequence):
    dna = Seq(dna_sequence)
    rna = dna.transcribe()
    return str(rna)

dna = "ATGGATTAG"
rna = dna_to_rna(dna)
print(rna) # "AUGCAU"





