def parse_fasta(filepath):
    sequences = {}
    current_id = None
    with open(filepath, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            if line.startswith(">"):
                current_id = line[1:]
                sequences[current_id] = ""
            else:
                if current_id:
                    sequences[current_id] += line.upper()
    return sequences

def validate_dna(seq):
    return set(seq).issubset({'A','T','G','C'})

def gc_content(seq):
    if len(seq) == 0:
        return 0
    return (seq.count('G') + seq.count('C')) / len(seq) * 100

def reverse_complement(seq):
    comp = {'A':'T', 'T':'A', 'G':'C', 'C':'G'}
    return "".join(comp.get(b, b) for b in reversed(seq))

def transcribe(seq):
    return seq.replace('T', 'U')

def find_motif(seq, motif):
    pos = []
    start = 0
    while True:
        i = seq.find(motif, start)
        if i == -1:
            break
        pos.append(i)
        start = i + 1
    return pos

if __name__ == "__main__":
    data = parse_fasta("sequence.fasta")
    motif = input("Enter motif to search (e.g. ATG): ").strip().upper()
    
    print("\n--- DAY 3 TOUGH RESULTS ---")
    for sid, seq in data.items():
        valid = "OK" if validate_dna(seq) else "INVALID"
        gc = gc_content(seq)
        rc = reverse_complement(seq)
        rna = transcribe(seq)
        mpos = find_motif(seq, motif) if motif else []
        print(f"\n>{sid} [{valid}] len={len(seq)} GC={gc:.1f}%")
        print(f"Motif {motif} at: {mpos if mpos else 'Not found'}")
        print(f"Reverse Comp: {rc[:40]}...")
        print(f"RNA: {rna[:40]}...")
