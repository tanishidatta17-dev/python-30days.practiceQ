# Day 2 - GC conent & DNA Analysis 
dna = "ATGCGTACGTAGCTAGCTAGATCGATCGATCGATATAGC"
print(f"DNA: {dna}")
print(f"Length: {len(dna)}")

# Counts
a_count = dna.count('A')
t_count = dna.count('T')
g_count = dna.count('G')
c_count = dna.count('C')

    print(f"A: {a_count}, T: {t_count}, G: {g_count}, C: {c_count}")

    # T0D0 1: Calculate GC content %
    gc_percent = (g_count + c_count)/ len(dna)* 100
    print(f"GC Content : {gc_percengt:2f} % ")

    # T0D0 2: RNA - replace T with U 
    rna = dna.replace('T', 'U')
    print(f"RNA: {rna}")

    # T0D0 3: Check if DNA is valid ?
