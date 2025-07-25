DNA_BASES = ["A", "C", "G", "T"]
RNA_BASES = ["A", "C", "G", "U"]

# Codons and amino acids for DNA and RNA
DNA_CODONS = {
    "TTT": "Phenylalanine", "TTC": "Phenylalanine", "TTA": "Leucine", "TTG": "Leucine",
    "CTT": "Leucine", "CTC": "Leucine", "CTA": "Leucine", "CTG": "Leucine",
    "ATT": "Isoleucine", "ATC": "Isoleucine", "ATA": "Isoleucine", "ATG": "Methionine",
    "GTT": "Valine", "GTC": "Valine", "GTA": "Valine", "GTG": "Valine",
    "TCT": "Serine", "TCC": "Serine", "TCA": "Serine", "TCG": "Serine",
    "CCT": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline",
    "ACT": "Threonine", "ACC": "Threonine", "ACA": "Threonine", "ACG": "Threonine",
    "GCT": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine",
    "TAT": "Tyrosine", "TAC": "Tyrosine", "TAA": "Stop", "TAG": "Stop",
    "CAT": "Histidine", "CAC": "Histidine", "CAA": "Glutamine", "CAG": "Glutamine",
    "AAT": "Asparagine", "AAC": "Asparagine", "AAA": "Lysine", "AAG": "Lysine",
    "GAT": "Aspartate", "GAC": "Aspartate", "GAA": "Glutamate", "GAG": "Glutamate",
    "TGT": "Cysteine", "TGC": "Cysteine", "TGA": "Stop", "TGG": "Tryptophan",
    "CGT": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine",
    "AGT": "Serine", "AGC": "Serine", "AGA": "Arginine", "AGG": "Arginine",
    "GGT": "Glycine", "GGC": "Glycine", "GGA": "Glycine", "GGG": "Glycine"
}

RNA_CODONS = {
    "UUU": "Phenylalanine", "UUC": "Phenylalanine", "UUA": "Leucine", "UUG": "Leucine",
    "CUU": "Leucine", "CUC": "Leucine", "CUA": "Leucine", "CUG": "Leucine",
    "AUU": "Isoleucine", "AUC": "Isoleucine", "AUA": "Isoleucine", "AUG": "Methionine",
    "GUU": "Valine", "GUC": "Valine", "GUA": "Valine", "GUG": "Valine",
    "UCU": "Serine", "UCC": "Serine", "UCA": "Serine", "UCG": "Serine",
    "CCU": "Proline", "CCC": "Proline", "CCA": "Proline", "CCG": "Proline",
    "ACU": "Threonine", "ACC": "Threonine", "ACA": "Threonine", "ACG": "Threonine",
    "GCU": "Alanine", "GCC": "Alanine", "GCA": "Alanine", "GCG": "Alanine",
    "UAU": "Tyrosine", "UAC": "Tyrosine", "UAA": "Stop", "UAG": "Stop",
    "CAU": "Histidine", "CAC": "Histidine", "CAA": "Glutamine", "CAG": "Glutamine",
    "AAU": "Asparagine", "AAC": "Asparagine", "AAA": "Lysine", "AAG": "Lysine",
    "GAU": "Aspartate", "GAC": "Aspartate", "GAA": "Glutamate", "GAG": "Glutamate",
    "UGU": "Cysteine", "UGC": "Cysteine", "UGA": "Stop", "UGG": "Tryptophan",
    "CGU": "Arginine", "CGC": "Arginine", "CGA": "Arginine", "CGG": "Arginine",
    "AGU": "Serine", "AGC": "Serine", "AGA": "Arginine", "AGG": "Arginine",
    "GGU": "Glycine", "GGC": "Glycine", "GGA": "Glycine", "GGG": "Glycine"
}

def get_codon_map(base_type):
    if base_type == "dna":
        return DNA_BASES, DNA_CODONS
    elif base_type == "rna":
        return RNA_BASES, RNA_CODONS
    return None, None

def get_bases_from_user(valid_bases):
    bases = []
    while True:
        base = input("Enter base (or type 'end' to finish): ").upper()
        if base.upper() == "END":
            return bases
        elif base.upper() in valid_bases:
            bases.append(base)
        else:
            print("Invalid base. Please enter a valid DNA or RNA base.")

def translate_to_amino_acids(bases, codon_map):
    codons = ["".join(bases[i:i+3]) for i in range(0, len(bases), 3) if i + 2 < len(bases)]
    print(codons)
    amino_acids = []
    for codon in codons:
        amino_acid = codon_map.get(codon, None)
        if amino_acid:
            amino_acids.append(amino_acid)
            print(f"Match found: {amino_acid} -> {codon}")
        else:
            print(f"No match found for codon: {codon}")
    return amino_acids

# Main program logic
import os
print("DNA/RNA base analyser v2 ('h' for help)")

while True:
    command = input("Type 'dna' for DNA or 'rna' for RNA ('h' for help): ").strip().lower()
    if command=='dna' or command=='rna':
        valid_bases, codon_map = get_codon_map(command)
        user_bases = get_bases_from_user(valid_bases)
        amino_acids = translate_to_amino_acids(user_bases, codon_map)
        print(f"Amino acid sequence:{user_bases}\nBase sequence:{amino_acids}")
    elif command=='h' or command=='help' or command=='/h':
        print("Type DNA or RNA. It's that simple.\n'h' for help\n'e' for exit\n'q' for exit")
    elif command=='e' or command=='exit' or command=='quit'or command=='quit':
        quit()
    else:
        print("Invalid input. Please enter 'dna' or 'rna'. Type 'exit' to quit program.")
