f = open("mfasta.txt, "r")
def parse_fasta(f)
    fasta_list = []
    current_seq = ""

    for line in f:
        if line[0] == '>':
            if current_seq != ""
