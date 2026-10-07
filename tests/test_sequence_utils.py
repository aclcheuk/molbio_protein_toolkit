import pytest


# Unit Tests for src.sequence_utils.py functions
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

def test_is_orf():
    from src.sequence_utils import is_orf
    assert is_orf("ATGAAATAG") == True
    assert is_orf("atgaaatag") == True
    assert is_orf("A t G A A A T A G") == True
    with pytest.raises(ValueError):
        is_orf("ATGAAAT") # Invalid ORF
    with pytest.raises(ValueError):
        is_orf("ATGCB") # Invalid DNA sequence

def test_translate_dna():
    from src.sequence_utils import translate_dna
    assert translate_dna("ATGAAATAG") == "MK"
    assert translate_dna("atgaaatag") == "MK"
    assert translate_dna("A t G A A A T A G") == "MK"
    with pytest.raises(ValueError):
        translate_dna("ATGAAAT") # Invalid ORF
    with pytest.raises(ValueError):
        translate_dna("ATGCB") # Invalid DNA sequence

def test_count_nucleotides():
    from src.sequence_utils import count_nucleotides
    assert count_nucleotides("ATGCAACTC") == {"A": 3, "T": 2, "G": 1, "C": 3}
    assert count_nucleotides("atgcATGC") == {"A": 2, "T": 2, "G": 2, "C": 2}
    assert count_nucleotides("A t G C A T G C") == {"A": 2, "T": 2, "G": 2, "C": 2}
    with pytest.raises(ValueError):
        count_nucleotides("ATGCB") # Invalid DNA sequence

def test_gc_content():
    from src.sequence_utils import gc_content
    assert gc_content("ATGCAACTC") == float(4/9)
    assert gc_content("atgcATGC") == float(4/8)
    assert gc_content("A t G C A T G C C") == float(5/9)
    with pytest.raises(ValueError):
        gc_content("ATGCB") # Invalid DNA sequence

