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
