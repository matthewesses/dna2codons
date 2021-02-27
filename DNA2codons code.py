def dna2codons(dnaString):#function for turning DNA into codons/ proteins
    # Convert the string from DNA to RNA. 
    def dna2rna(dna):
        rna = ''
        for symbol in dna:#transcripts the DNA to its RNA counterpart
            if symbol == 'A':
                rna = rna + 'U'
            elif symbol == 'T':
                rna = rna + "A"
            elif symbol == 'C':
                rna = rna + "G"
            elif symbol == 'G':
                rna = rna + "C"
        
        return rna
    
    # Convert the RNA string to its corresponding protein expression string.
    def rna2codon(triplet):
        genetic_code = {
            'UUU': 'F', 'UUC': 'F', 'UUA': 'L', 'UUG': 'L',        'CUU': 'L', 'CUC': 'L', 'CUA': 'L', 'CUG': 'L',
            'AUU': 'I', 'AUC': 'I', 'AUA': 'I', 'AUG': 'M',        'GUU': 'V', 'GUC': 'V', 'GUA': 'V', 'GUG': 'V',

            'UCU': 'S', 'UCC': 'S', 'UCA': 'S', 'UCG': 'S',        'CCU': 'P', 'CCC': 'P', 'CCA': 'P', 'CCG': 'P',
            'ACU': 'T', 'ACC': 'T', 'ACA': 'T', 'ACG': 'T',        'GCU': 'A', 'GCC': 'A', 'GCA': 'A', 'GCG': 'A',

            'UAU': 'Y', 'UAC': 'Y', 'UAA': '*', 'UAG': '*',        'CAU': 'H', 'CAC': 'H', 'CAA': 'Q', 'CAG': 'Q',
            'AAU': 'N', 'AAC': 'N', 'AAA': 'K', 'AAG': 'K',        'GAU': 'D', 'GAC': 'D', 'GAA': 'E', 'GAG': 'E',

            'UGU': 'C', 'UGC': 'C', 'UGA': '*', 'UGG': 'W',        'CGU': 'R', 'CGC': 'R', 'CGA': 'R', 'CGG': 'R',
            'AGU': 'S', 'AGC': 'S', 'AGA': 'R', 'AGG': 'R',        'GGU': 'G', 'GGC': 'G', 'GGA': 'G', 'GGG': 'G',
        } #this is more or less an index for what is coded when and how
        
        if triplet in genetic_code:
            x=genetic_code[triplet]
            return x
        else:
            return "Invalid" #ignores patterns that don't work
    def rna2codons(triplets): #Cuts up the RNA and assigns it to certain proteins
        amino= ''
        for i in range( 0,int( len(triplets) / 3 ) ):
            amino= amino+ rna2codon(triplets[ 3*i:3*i+3])#slicing and indexing the rna
        return amino
    return rna2codons(dna2rna(dnaString)) #returns the DNA string as what I want it to be, codons