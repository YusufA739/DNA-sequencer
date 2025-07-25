DNA_BASES=["A","C","G","T"]
RNA_BASES=['A','C','G','U']
i=input("""type 'dna' or 'DNA' for DNA BASES [A, C, G, T]
or type 'rna' , 'RNA' for RNA bases [A, C, G, U]
->""")
if i.lower()=="dna":
    
    codons=["Glutamine CAA","Histidine CAC","Glutamine CAG","Histidine CAT","Proline CCA","Proline CCC","Proline CCG","Proline CCT","Arginine CGA","Arginine CGC","Arginine CGG","Arginine CGT","Leucine CTA","Leucine CTC","Leucine CTG","Leucine CTT","Termination (opal or umber) TGA","Cysteine TGC","Tryptophan TGG","Cysteine TGT","Serine TCA","Serine TCC","Serine TCG","Serine TGT","Termination (ochre) TAA","Tyrosine","Termination (amber) TAG","Tyrosine","Valine GTA","Valine GTC","Valine GTG","Valine GTT","Alanine GCA","Alanine GCC","Alanine GCG","Alanine GCT","Glutamate GAA","Aspartate GAC","Glutamate GAG","Aspartate GAT","Isoleucine ATA","Isoleucine ATC","Methionine ATG","Isoleucine ATT","Arginine AGA","Serine AGC","Arginine AGG","Serine AGT","Threonine ACA","Threonine ACC","Threonine ACT","Methionine ACG","Leucine TTA","Phenylalanine TTC","Leucine TTG","Phenylalanine TTT","lysine AAA","lysine AAG","Asparagine AAC","Asparagine AAT","glycine GGA","glycine GGC","glycine GGG","glycine GGT"]
    amino_acids=["CAA","CAC","CAG","CAT","CCA","CCC","CCG","CCT","CGA","CGC","CGG","CGT","CTA","CTC","CTG","CTT","TGA","TGC","TGG","TGT","TCA","TCC","TCG","TCT","TAA","TAC","TAG","TAT","GTA","GTC","GTG","GTT","GCA","GCC","GCG","GCT","GAA","GAC","GAG","GAT","ATA","ATC","ATG","ATT","AGA","AGC","AGG","AGT","ACA","ACC","ACT","ACG","TTA","TTC","TTG","TTT","AAA","AAG","AGC","AAT","GGA","GGC","GGG","GGT"]
    #sort out the stuff into alphabetical order
    list1=[]
    list2=[]
    input1=""
    valid=False
    while input1!="end loop":
        input1=input("input base: ")
        if input1.lower()=="end":
            break
        for carrier in DNA_BASES:
            if input1.upper()==carrier:
                valid=True
            else:
                pass
        if valid==False:
            print("enter a valid DNA base")
        
        else:
            list2.append(input1.upper())
        valid=False


    string=str()
    """
    for carrier in list1:
        string+=carrier

    for base in amino_acids:
        
        if base=='A':
            list1.append()
        if base=='C':
            list1.append()
        if base=='G':
            list1.append()
        if base=='T':
            list1.append()
    """
    count=0
    inputs=0
    count2=0
    count3=1
    for carrier in list2:
        string=string+carrier
        if len(string)==3:
            list1.append(string)
            count3=1
            string=str()
            inputs+=1
    #print(list1)
    for carrier in list1:
        count=0
        for carrier2 in amino_acids:
            if carrier==carrier2:
                count2=count
                print("match found")
                print("the match was found and it is",codons[count2])
                count=0
            else:
                count=count+1
                pass
        if count2==-50:
            print("match not found for input",count)
        if 1==2:
            print("this is me trying to enumerate 'list(amino_acids)'",enumerate(amino_acids))
        else:
            pass
            #not using any imports for now unless i do random trinuclide generator
            #that tells you what amino acid it is or if you have to guess
        count3+=1


elif i.lower()=="rna":
    codons=["Glutamine CAA","Histidine CAC","Glutamine CAG","Histidine CAT","Proline CCA","Proline CCC","Proline CCG","Proline CCT","Arginine CGA","Arginine CGC","Arginine CGG","Arginine CGT","Leucine CTA","Leucine CTC","Leucine CTG","Leucine CTT","Termination (opal or umber) TGA","Cysteine TGC","Tryptophan TGG","Cysteine TGT","Serine TCA","Serine TCC","Serine TCG","Serine TGT","Termination (ochre) TAA","Tyrosine","Termination (amber) TAG","Tyrosine","Valine GTA","Valine GTC","Valine GTG","Valine GTT","Alanine GCA","Alanine GCC","Alanine GCG","Alanine GCT","Glutamate GAA","Aspartate GAC","Glutamate GAG","Aspartate GAT","Isoleucine ATA","Isoleucine ATC","Methionine ATG","Isoleucine ATT","Arginine AGA","Serine AGC","Arginine AGG","Serine AGT","Threonine ACA","Threonine ACC","Threonine ACT","Methionine ACG","Leucine TTA","Phenylalanine TTC","Leucine TTG","Phenylalanine TTT","lysine AAA","lysine AAG","Asparagine AAC","Asparagine AAT","glycine GGA","glycine GGC","glycine GGG","glycine GGT"]
    amino_acids=["CAA","CAC","CAG","CAT","CCA","CCC","CCG","CCT","CGA","CGC","CGG","CGT","CTA","CTC","CTG","CTT","TGA","TGC","TGG","TGT","TCA","TCC","TCG","TCT","TAA","TAC","TAG","TAT","GTA","GTC","GTG","GTT","GCA","GCC","GCG","GCT","GAA","GAC","GAG","GAT","ATA","ATC","ATG","ATT","AGA","AGC","AGG","AGT","ACA","ACC","ACT","ACG","TTA","TTC","TTG","TTT","AAA","AAG","AGC","AAT","GGA","GGC","GGG","GGT"]
    #sort out the stuff into alphabetical order
    list1=[]
    list2=[]
    input1=""
    valid=False
    while input1!="end loop":
        input1=input("input base: ")
        if input1.lower()=="end":
            break
        for carrier in RNA_BASES:
            if input1.upper()==carrier:
                valid=True
            else:
                pass
        if valid==False:
            print("enter a valid DNA base")
        
        else:
            list2.append(input1.upper())
        valid=False


    string=str()
    """
    for carrier in list1:
        string+=carrier

    for base in amino_acids:
        
        if base=='A':
            list1.append()
        if base=='C':
            list1.append()
        if base=='G':
            list1.append()
        if base=='T':
            list1.append()
    """
    count=0
    inputs=0
    count2=0
    count3=1
    for carrier in list2:
        string=string+carrier
        if len(string)==3:
            list1.append(string)
            count3=1
            string=str()
            inputs+=1
    #print(list1)
    for carrier in list1:
        count=0
        for carrier2 in amino_acids:
            if carrier==carrier2:
                count2=count
                print("match found")
                print("the match was found and it is",codons[count2])
                count=0
            else:
                count=count+1
                pass
        if count2==-50:
            print("match not found for input",count)
        if 1==2:
            print("this is me trying to enumerate 'list(amino_acids)'",enumerate(amino_acids))
        else:
            pass
            #not using any imports for now unless i do random trinuclide generator
            #that tells you what amino acid it is or if you have to guess
        count3+=1
