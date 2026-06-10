codons = {
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile', 'AUG': 'Met',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'AAU': 'Asn', 'AAC': 'Asn', 'AAA': 'Lys', 'AAG': 'Lys',
    'AGU': 'Ser', 'AGC': 'Ser', 'AGA': 'Arg', 'AGG': 'Arg',   'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'CAU': 'His', 'CAC': 'His', 'CAA': 'Gln', 'CAG': 'Gln',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg',  'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val', 'GCU': 'Ala', 'GCC': 'Ala','GCA': 'Ala', 'GCG': 'Ala' ,   'GAU': 'Asp', 'GAC': 'Asp', 'GAA': 'Glu', 'GAG': 'Glu', 'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',   'UUU': 'Phe', 'UUC': 'Phe', 'UUA': 'Leu', 'UUG': 'Leu',  'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser',   'UAU': 'Tyr', 'UAC': 'Tyr', 'UAA': 'STOP', 'UAG': 'STOP',   'UGU': 'Cys', 'UGC': 'Cys', 'UGA': 'STOP', 'UGG': 'Trp'}
   
def transcription(dna):
    map=str.maketrans('ATCG','UAGC')
    mrna=dna.translate(map)
    return mrna
  
def translation(mrna):
    translation_chain=[]    
    for i in range(0,len(mrna),3):
        codon=mrna[i:i+3]
        if codon in codons:
            if codons[codon]=='STOP':
                break
        translation_chain.append(codons[codon])
    return '-'.join(translation_chain)
    
    
   
print('-------Polypeptide chain sythesis has started')
dna_seq=input("Enter template DNA sequence: ")
mrna_result=transcription(dna_seq)
print(f"mRNA:{mrna_result}")
polypeptide=translation(mrna_result)
print(f"protein:{polypeptide}")
    
        
             
       
    
        
          
        
        
    
    
   
    


 

  
