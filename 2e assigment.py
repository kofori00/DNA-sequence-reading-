def get_length(dna):
    return len(dna)
    """ (str) -> int
    Return the length of the DNA sequence dna.

    >>> get_length('ATCGAT')
    6
    >>> get_length('ATCG')
    4
    """


def is_longer(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna1 is longer than DNA sequence
    dna2.

    >>> is_longer('ATCG', 'AT')
    True
    >>> is_longer('ATCG', 'ATCGGA')
    False
    """
    Ans='non'
    if dna1>dna2:
        Ans=True
    else:
        Ans=False
    return Ans

def count_nucleotides(dna, nucleotide):
    """ (str, str) -> int

    Return the number of occurrences of nucleotide in the DNA sequence dna.

    >>> count_nucleotides('ATCGGC', 'G')
    2
    >>> count_nucleotides('ATCTA', 'G')
    0
    """
    count=dna.count(nucleotide)
    return count 

def contains_sequence(dna1, dna2):
    """ (str, str) -> bool

    Return True if and only if DNA sequence dna2 occurs in the DNA sequence
    dna1.

    >>> contains_sequence('ATCGGC', 'GG')
    True
    >>> contains_sequence('ATCGGC', 'GT')
    False
    """
    import re
    searchObj = re.search(dna2, dna1, re.M|re.I)

    if searchObj:
        Ans=True
    else:
        Ans=False
    return Ans

def Is_valid_Sequence(dna):
    """ (str) -> bool

    Return True if and only if the DNA sequence is valid
    (that is, it contains no characters other than 'A', 'T', 'C' and 'G') 

    >>> Is_valid_Sequence('TAGP')
    False
    >>> Is_valid_Sequence('TAGC')
    True
    """
    length = len(dna)
    Num_DNA=0
    for char in dna:
        if char in 'TGAC':
            Num_DNA = Num_DNA + 1

    if length>Num_DNA:
        return False
    else:
        return True 
            
def insert_sequence(dna1,dna2,i):   
    """ (str, str, int) -> str

    insert_sequence(ACTG,AT,2)
    """

    index=int(i)
    if (dna1!= dna2):
        dna = dna1[0:index]+dna2+dna1[index:len(dna1)]
    else:
        dna = dna1[0:index]+dna2+dna1[index:len(dna1)]

    return dna


def get_complement(Nu):
    """(str) -> str

    return the complementary of the nucleotide

    get_complement(A) gives T 
    
    """

    if   (Nu=='A'):
        Comp='T'
        
    elif Nu=='T':
        Comp='A'

    elif Nu=='C':
        Comp='G'

    elif Nu=='G':
        Comp='C'

    else:
        Comp='not a nucleotide'

    return Comp

def get_complementary_sequence(dna):
    """(str) -> str

    The parameter is a DNA sequence. Return the DNA
    sequence that is complementary to the given DNA sequence.
    For exmaple, if you call this function with 'AT' as the argument, it should return 'TA'.

    get_complementary_sequence('AT') gives 'TA'
    
    """
    Comp=''
    for char in dna:
        if char in 'A':
            Comp= Comp + 'T'
        
        elif char in 'T':
            Comp= Comp + 'A'

        elif char in 'C':
            Comp= Comp + 'G'

        elif char in 'G':
            Comp= Comp + 'C'

        else:
            Comp= 'sequence with non-nucleotide'

    return Comp 
