import os
from Bio.Seq import Seq
from Bio import Align
from Bio import Restriction

def dna_complement(dna_sequence):
    dna_strand = Seq(dna_sequence)
    complimentary_strand = dna_strand.complement()
    return complimentary_strand

def dna_reverse(dna_sequence):
    dna_strand = Seq(dna_sequence)
    reverse_strand = dna_strand[::-1]
    return reverse_strand

def dna_orfs(dna_sequence):
    dna_seq = Seq(dna_sequence)
    orfs = dna_seq.translate()
    return orfs

def dna_align(seq1, seq2):
    aligner = Align.PairwiseAligner()
    alignments = aligner.align(seq1, seq2)
    return alignments

def dna_to_rna(dna_sequence):
    dna = Seq(dna_sequence)
    rna = dna.transcribe()
    return str(rna)

def restriction_site_analysis(dna_sequence):
    dna = Seq(dna_sequence)
    enzyme = Restriction.EcoRI
    sites = enzyme.search(dna)
    return sites

def menu():
    print('''
    1. Find Complementary DNA
    2. Find Reverse DNA
    3. Find Open Reading Frames [Orfs]
    4. Show Sequence Alignment
    5. Show Number of Restriction Sites
    6. Show Transcribed DNA Strand
    7. Exit''')


def main():
    print(r'''
O       o O       o O       o
| O   o | | O   o | | O   o |
| | O | | | | O | | | | O | |
| o   O | | o   O | | o   O |
o       O o       O o       O''')

    print("\nWelcome to SeqGenius")

    while True:
        dna_sequence = input("Enter a DNA Sequence")
        
        menu()
        choice = int(input("Enter Your Choice"))
        if choice == 1:
            complimentary_strand = dna_complement(dna_sequence)
            
            print("Original DNA Strand: ", dna_sequence)
            print("Complimentary DNA Strand: ", complimentary_strand)
            
        elif choice == 2:
            reverse_sequence = dna_reverse(dna_sequence)
            print("Original DNA Strand: ", dna_sequence)
            print("Reverse DNA Strand: ", reverse_sequence)
        elif choice == 3:
            open_reading_frames = dna_orfs (dna_sequence)
            print("ORFs: ", open_reading_frames)
        elif choice == 4:
            dna_sequence2 = input("Enter another DNA Sequence")
            alignments = dna_align(dna_sequence, dna_sequence2)
            for alignment in alignments:
                print(alignment)
        elif choice == 5:
            sites = restriction_site_analysis(dna_sequence)
            print(sites)
        elif choice == 6:
            rna = dna_to_rna(dna_sequence)
            print(rna)
        elif choice == 7:
            print("UAA,UGA,UAG")
            break









if __name__ == "__main__":
    main()