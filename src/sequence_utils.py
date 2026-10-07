# Sequence Pre-processing
import src.constants as const  # Access all the constants and codon tables defined in constants.py


def clean_sequence(seq:str) -> str:
    """
    Remove spaces and convert the sequence to uppercase.
    """
    return seq.replace(" ", "").upper()

def is_valid_dna(seq:str) -> bool:
    """
    Check sequence is a valid DNA sequence containing only A, T, G, and C.
    """
    seq = clean_sequence(seq)
    for base in seq:
        if base not in const.DNA_BASES:
            return False
    return True

def is_valid_rna(seq:str) -> bool:
    """
    Check sequence is a valid RNA sequence containing only A, U, G, and C.
    """
    seq = clean_sequence(seq)
    for base in seq:
        if base not in const.RNA_BASES:
            return False
    return True

def transcribe_dna(seq:str) -> str:
    """
    Transcribe a DNA sequence into RNA by replacing thymine (T) with uracil (U).
    """
    seq = clean_sequence(seq)
    if is_valid_dna(seq):
        return seq.replace("T", "U")
    else:
        raise ValueError("Invalid DNA sequence")

def reverse_complement_dna(seq:str) -> str:
    """
    Generate the reverse complement of a DNA sequence.
    """
    seq = clean_sequence(seq)
    if is_valid_dna(seq):
        complement = const.DNA_COMPLEMENT
        reverse_seq = ""
        for base in reversed(seq):
            reverse_seq += complement[base]
        return reverse_seq
    else:
        raise ValueError("Invalid DNA sequence")

def complement_dna(seq:str) -> str:
    """
    Generate the complement of a DNA sequence.
    """
    seq = clean_sequence(seq)
    if is_valid_dna(seq):
        complement = const.DNA_COMPLEMENT
        comp_seq = ""
        for base in seq:
            comp_seq += complement[base]
        return comp_seq
    else:
        raise ValueError("Invalid DNA sequence")

def is_orf(seq:str) -> bool:
    """
    Check if a DNA sequence is an open reading frame (ORF).
    Starting with a start codon (ATG) and ending with a stop codon (TAA, TAG or TGA).
    """
    seq = clean_sequence(seq)
    if is_valid_dna(seq):
        start_codon = "ATG"
        stop_codons = {"TAA", "TAG", "TGA"}
        if seq.startswith(start_codon) and seq[-3:] in stop_codons:
            return True
        else:
            raise ValueError("Sequence is not an open reading frame (ORF)")
    else:
        raise ValueError("Invalid DNA sequence")

def translate_dna(seq:str) -> str:
    """
    Translate a DNA sequence into a protein sequence.
    """
    seq = clean_sequence(seq)
    if is_orf(seq):
        protein_seq = ""
        codon_table = const.TRIPLET_CODON_TABLE
        for i in range(0, len(seq) - 3, 3):
            codon = seq[i:i+3]
            protein_seq += codon_table.get(codon, "_")
        return protein_seq
    else:
        raise ValueError("Invalid DNA sequence or ORF")

def count_nucleotides(seq:str) -> dict:
    """
    Count the occurrences of each nucleotide in a DNA sequence.
    """
    seq = clean_sequence(seq)
    if is_valid_dna(seq):
        counts = {base: 0 for base in const.DNA_BASES}
        for base in seq:
            counts[base] += 1
        return counts
    else:
        raise ValueError("Invalid DNA sequence")

def gc_content(seq:str) -> float:
    """Given a DNA sequence, returns GC content as a float value between 0 and 1."""
    seq = clean_sequence(seq)
    if is_valid_dna(seq):
        gc_total = seq.count("G") + seq.count("C")
        return gc_total / len(seq)
    else:
       raise ValueError("Invalid DNA sequence")

