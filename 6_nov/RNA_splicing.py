#rosalind RNA Splicing
#
# https://github.com/radoslavzi/BioInformatics/blob/master/Lectures/RNA_splicing/rosalind_splc.txt
from read_fasta import ParseFASTA, ReadFASTA

def getMatchingPositions(dna, intron):
    result = []
    for p in range(0, len(dna)):
        if dna[p:].startswith(intron):
            result.append(p)
    return result

dna_list = ReadFASTA("rosalind_splc.txt")

dna = dna_list[0][1]
print(dna)

for intron in dna_list[1:]:
    positions = getMatchingPositions(dna, intron[1])
    for p in positions:
        dna = dna[0 : p] + dna[p + len(intron[1]):]

print(dna)
