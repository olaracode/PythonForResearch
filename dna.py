


def translate(seq):
    # First lets define the table with which we are going to make the translation
    table = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'D', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '_', 'TAG': '_',
        'TGC': 'C', 'TGT': 'C', 'TGA': '_', 'TGG': 'W'}

    protein = ""
    # Then we check that the sequence length is divisible by 3
    if len(seq) % 3 == 0:
        # We use a range function with the length of our sequence as the top limit
        # and a three as the step
        for i in range(0, len(seq), 3):
            # we make a variable name codon which will the store the sliced sequence
            # consisting of the starting point (i) and going three steps up with i+3
            codon = seq[i:i+3]
            # finally we use codon as the key to get the value and we add it to the empty
            # protein string
            protein += table[codon]
    return protein


def read_seq(inputfile):
    # opens a file and returns the text without special characters
    with open(inputfile, "r") as f:
        seq = f.read()
    seq = seq.replace("\n", "")
    seq = seq.replace("\r", "")
    return seq


dna = read_seq("dna.txt")
protein = read_seq("protein.txt")
one_way = translate(dna[20:935])
or_another = translate(dna[20:938])[:-1]
print(one_way == or_another)
print(protein)