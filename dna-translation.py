# Transcription
def transcript(counterparts, dnaSequence):
    for index, base in enumerate(dnaSequence):
        for key, value in counterparts.items():
            if base == key:
                dnaSequence[index] = value

# Translation
def translate(genCode, codonlist):
    clist = []
    for index, codon in enumerate(codonlist):
        for key, value in genCode.items():
            if codon == key:
                clist.append(value)
    # return the list as string
    return ''.join(clist)

# Taking Input from User
dna = input("Enter the DNA sequence:")

# Converting String to List
string = list(dna)

# dictionary for counterparts #directly transcripts to Uracil
counterParts = {"G": "C", "C": "G", "T": "A", "A": "U"}

# Table Taken from pythoforbiologists.com T->U change is done by me
gencode = {
    'AUA': 'I', 'AUC': 'I', 'AUU': 'I', 'AUG': 'M',
    'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACU': 'T',
    'AAC': 'N', 'AAU': 'N', 'AAA': 'K', 'AAG': 'K',
    'AGC': 'S', 'AGU': 'S', 'AGA': 'R', 'AGG': 'R',
    'CUA': 'L', 'CUC': 'L', 'CUG': 'L', 'CUU': 'L',
    'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCU': 'P',
    'CAC': 'H', 'CAU': 'H', 'CAA': 'Q', 'CAG': 'Q',
    'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGU': 'R',
    'GUA': 'V', 'GUC': 'V', 'GUG': 'V', 'GUU': 'V',
    'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCU': 'A',
    'GAC': 'D', 'GAU': 'D', 'GAA': 'E', 'GAG': 'E',
    'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGU': 'G',
    'UCA': 'S', 'UCC': 'S', 'UCG': 'S', 'UCU': 'S',
    'UUC': 'F', 'UUU': 'F', 'UUA': 'L', 'UUG': 'L',
    'UAC': 'Y', 'UAU': 'Y', 'UAA': '_', 'UAG': '_',
    'UGC': 'C', 'UGU': 'C', 'UGA': '_', 'UGG': 'W'}

# Transcripts DNA to Massenger RNA
transcript(counterParts, string)

# joining List back to string
mRNA = ''.join(string)
print("DNA Transcripted to mRNA: "+mRNA)

# Converting mRNA string to List with groups of 3 charachters
codonList = [mRNA[i:i+3] for i in range(0, len(mRNA), 3)]
print("Codons Are: ")
print(codonList)

# Translate the mRNA to Amino Acids
aminoAcid = translate(gencode, codonList)

# check if the number of bases are divisible by 3
if len(mRNA) % 3 == 0:
    print("DNA translated to Amino Acid: " + aminoAcid)
else:
    # if number of bases are not divisible by 3 then check if there is an STOP codon
    # '_' is considered as STOP according to table
    if aminoAcid.find('_') != -1:
        x = aminoAcid.split('_')
        for i in range(len(x)):
            print("DNA translated to Amino Acid: " + x[i])
    else:
        # if there is no stop codons
        print("Sequence not divisible by three")

input("Please Enter to Exit Program")
