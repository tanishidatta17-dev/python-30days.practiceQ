cat > day4.py << 'PYEOF'
# Day 4 - ORF Finder + Protein Translation

def translate_codon(codon):
    table = {
        'TTT':'F','TTC':'F','TTA':'L','TTG':'L',
        'CTT':'L','CTC':'L','CTA':'L','CTG':'L',
        'ATT':'I','ATC':'I','ATA':'I','ATG':'M',
        'GTT':'V','GTC':'V','GTA':'V','GTG':'V',
        'TCT':'S','TCC':'S','TCA':'S','TCG':'S',
        'CCT':'P','CCC':'P','CCA':'P','CCG':'P',
        'ACT':'T','ACC':'T','ACA':'T','ACG':'T',
        'GCT':'A','GCC':'A','GCA':'A','GCG':'A',
        'TAT':'Y','TAC':'Y','TAA':'*','TAG':'*',
        'CAT':'H','CAC':'H','CAA':'Q','CAG':'Q',
        'AAT':'N','AAC':'N','AAA':'K','AAG':'K',
        'GAT':'D','GAC':'D','GAA':'E','GAG':'E',
        'TGT':'C','TGC':'C','TGA':'*','TGG':'W',
        'CGT':'R','CGC':'R','CGA':'R','CGG':'R',
        'AGT':'S','AGC':'S','AGA':'R','AGG':'R',
        'GGT':'G','GGC':'G','GGA':'G','GGG':'G'
    }
    return table.get(codon, 'X')

# read fasta
with open("sequence.fasta") as f:
    seq = "".join([l.strip() for l in f if not l.startswith('>')]).upper()

print(f"Sequence len: {len(seq)}")

# 1. K-mer count (k=3)
k=3
kmer = {}
for i in range(len(seq)-k+1):
    mer = seq[i:i+k]
    kmer[mer] = kmer.get(mer, 0)+1
print(f"\nTop 5 {k}-mers:", sorted(kmer.items(), key=lambda x:x[1], reverse=True)[:5])

# 2. Find all ORFs in frame 0
orfs = []
for i in range(len(seq)-2):
    if seq[i:i+3] == 'ATG':
        protein = ""
        for j in range(i, len(seq)-2, 3):
            codon = seq[j:j+3]
            aa = translate_codon(codon)
            if aa == '*':
                orfs.append((i, j+3, protein))
                break
            protein += aa

if orfs:
    orfs.sort(key=lambda x: len(x[2]), reverse=True)
    longest = orfs[0]
    print(f"\nFound {len(orfs)} ORFs")
    print(f"Longest ORF: pos {longest[0]}-{longest[1]} len {len(longest[2])} aa")
    print(f"Protein: {longest[2][:60]}...")
else:
    print("\nNo ORF found")

# 3. Nucleotide composition dict method
comp = {b: seq.count(b) for b in "ATGC"}
print("\nComposition:", comp)
PYEOF