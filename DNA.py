import os

#settings
keepClearing = False  # Set to True if you want screeen to clear before each command


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

def file_import():
    try:
        filepath=input("file full path:")
        dna_file=open(filepath,"r")
        dna_sequence=dna_file.readlines()
        return(dna_sequence[0])
    except:
        return("")

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
        elif len(base.upper()) > 1:
            all_valid = True
            for carrier in base.upper():
                if carrier not in valid_bases:
                    all_valid = False
            if all_valid:
                for carrier in base.upper():
                    bases.append(carrier)
                print("Bases valid and Accepted. All have been added to sequence.")
            else:
                print("One or more invalid bases present. All bases were rejected to avoid deletion mutation.")
        else:
            print("Invalid base. Please enter a valid DNA or RNA base.")

def check_bases_from_file(valid_bases,file_bases):
    bases=[]
    input_error = False
    for carrier in file_bases.upper():
        if carrier in valid_bases:
            bases.append(carrier)
        else:
            print("Invalid DNA bases present. Exiting back to main menu.")
            input_error = True
    if input_error == False:
        return bases
    else:
        bases = []
        return bases

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

def main_menu_command():
    global genome_import,keepClearing
    command = input("Type 'dna' for DNA or 'rna' for RNA ('h' for help): ").strip().lower()#keep this in mind for future commands, because currently they're all lowercase due to the .lower()
    if command=='dna' or command=='rna':
        if keepClearing:
            os.system('cls')
        valid_bases, codon_map = get_codon_map(command)
        user_bases = get_bases_from_user(valid_bases)
        amino_acids = translate_to_amino_acids(user_bases, codon_map)
        print(f"Amino acid sequence:{user_bases}\nBase sequence:{amino_acids}")
    elif command=='h' or command=='help' or command=='/h':
        if keepClearing:
            os.system('cls')
        input("Type 'DNA' or 'RNA' for their respective conversion to amino acid sequencing.\n'file' for an analysis on a file within working directory or full file path from a file anywhere locally on computer.\n'h' for help\n'e' for exit\n'q' for exit\n\nPress enter to continue...")
    elif command=='e' or command=='exit' or command=='q'or command=='quit' or command == '1':
        if keepClearing:
            os.system('cls')
        quit()
    elif command=='clear' or command=='cls' or command=='clear screen' or command == 'c':
        os.system('cls')
    elif command=='/dokeepclearing':#special command (inspiration from minecraft)
        if keepClearing:
            os.system('cls')
        keepClearing = not keepClearing
        print("Keep clearing:", keepClearing)
        input("Press enter to continue...")
    elif command=='file':
        if keepClearing:
            os.system('cls')
        genome_import = file_import()
        if len(genome_import) >= 3:
            command_nested=input("dna or rna analysis on file data?:").lower()
            if command_nested in ['dna','rna']:
                valid_bases, codon_map = get_codon_map(command_nested)
                file_bases = check_bases_from_file(valid_bases,genome_import)
                amino_acids = translate_to_amino_acids(file_bases, codon_map)
                print("File legnth:"+str(len(genome_import))+"\nTruncated file length:"+str(  ( 3*(len(genome_import)//3) )  ))#simply divide by 3 floor (no remainder) and then multiply by 3 to get truncated length (amino acids are every 3 bases in a non rolling window fashion)
            else:
                print("Invalid command.")
        else:
            print("File does not have minimum 3 bases.")
    else:
        print("Invalid input. Enter 'dna' or 'rna'. Type 'exit' to quit program.")

# Main program logic
print("DNA/RNA base analyser v3 ('h' for help)")

while True:
    if keepClearing:
        os.system('cls')
    main_menu_command()