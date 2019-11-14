# Error Correction in Reads
#
# Взимаме под внимание само първата.
# Проверка дали комплементарната секвенция съществува. ако я няма значи е грешка
# АГТ
#АЦТ
#АГТ
#АЦТ 

from read_fasta import ReadFASTA

seqs = ReadFASTA('corr.txt')

for seq in seqs:
    print(seq)
    break

trantab = "".maketrans('ACGT', 'TGCA')
