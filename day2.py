dna = "ATGCGTACGTAGCTAGCTAGATCGATCGATCGATATAGC"

print(f"DNA: {dna}")
print(f"Length: {len(dna)}")

a_count = dna.count('A')
t_count = dna.count('T')
g_count = dna.count('G')
c_count = dna.count('C')
print(f"A: {a_count}, T: {t_count}, G: {g_count}, C: {c_count}")

gc_percent = (g_count + c_count) / len(dna) * 100
print(f"GC Content: {gc_percent:.2f}%")

rna = dna.replace('T', 'U')
print(f"RNA: {rna}")