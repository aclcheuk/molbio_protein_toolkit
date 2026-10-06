import pytest


def test_clean_sequence():
    from src.sequence_utils import clean_sequence
    assert clean_sequence(" a t g c ") == "ATGC"
    assert clean_sequence("at gc") == "ATGC"
    assert clean_sequence("ATgC") == "ATGC"
    assert clean_sequence(" a t g c") == "ATGC"

def test_is_valid_dna():
    from src.sequence_utils import is_valid_dna
    assert is_valid_dna("ATGC") == True
    assert is_valid_dna("atgc") == True
    assert is_valid_dna("A t G C") == True
    assert is_valid_dna("ATGCB") == False
    assert is_valid_dna("XYZ") == False

def test_is_valid_rna():
    from src.sequence_utils import is_valid_rna
    assert is_valid_rna("AUGC") == True
    assert is_valid_rna("augc") == True
    assert is_valid_rna("A U g C") == True
    assert is_valid_rna("AUGCB") == False
    assert is_valid_rna("XYZ") == False

def test_transcribe_dna():
    from src.sequence_utils import transcribe_dna
    assert transcribe_dna("ATGCCC") == "AUGCCC"
    assert transcribe_dna("atgc") == "AUGC"
    assert transcribe_dna("A t G C") == "AUGC"
    with pytest.raises(ValueError):
        transcribe_dna("ATGCB") # Check function raises ValueError if invalid DNA sequence 

def test_complement_dna():
    from src.sequence_utils import complement_dna
    assert complement_dna("ATGCCC") == "TACGGG"
    assert complement_dna("atgcTTtt") == "TACGAAAA"
    assert complement_dna("A t G C AATTC") == "TACGTTAAG"
    with pytest.raises(ValueError):
        complement_dna("ATGCB.")

def test_reverse_complement_dna():
    from src.sequence_utils import reverse_complement_dna
    assert reverse_complement_dna("ATGCCC") == "GGGCAT"
    assert reverse_complement_dna("atgcTTtt") == "AAAAGCAT"
    assert reverse_complement_dna("A t G C AATTC") == "GAATTGCAT"
    with pytest.raises(ValueError):
        reverse_complement_dna("ATGCB.") # Check function raises ValueError if invalid DNA sequence 

