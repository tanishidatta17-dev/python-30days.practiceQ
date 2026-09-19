with open("sequence.fasta", "r") as f:
    lines = f.readlines()
    seq = "".join([line.strip() for line in lines if not line.startswith(">")])

seq = seq.replace("\n","").replace(" ","").replace('"',"").strip().upper()

print("Original length:", len(seq))

pairs = {"A":"T", "T":"A", "G":"C", "C":"G"}

comp = ""
for base in seq:
    if base in pairs:
        comp += pairs[base]

rev_comp = comp[::-1]

print("Reverse Complement length:", len(rev_comp))
print(rev_comp[:200])

with open("reverse_complement.txt", "w") as out:
    out.write(rev_comp)

print("Saved to reverse_complement.txt")


# Day 5: Reverse Complement - ORIGINAL LONG VERSION

seq = """
GATCATAACTGTTCTATGAAAGGTGTCTAAC
TATATATATATATATATATATATGCGCGCATATAT
CCCGGGGCCCCTTTTGGGGCCCCGGGGCCCCG
CTAGCTAGCTAGCTAGCTAGCTAGCTACGT
""".replace("\n","").replace(" ","").strip().upper()

print("Original length:", len(seq))
print("Original (first 100):", seq[:100])

# This line must stay exactly like this - never paste DNA here
pairs = {"A":"T", "T":"A", "G":"C", "C":"G"}

comp = ""
for base in seq:
    if base in pairs:
        comp += pairs[base]

rev_comp = comp[::-1]

print("Reverse Complement length:", len(rev_comp))
print("Reverse Complement (first 100):", rev_comp[:100])

with open("reverse_complement.txt", "w") as f:
    f.write(rev_comp)

print("Saved!")