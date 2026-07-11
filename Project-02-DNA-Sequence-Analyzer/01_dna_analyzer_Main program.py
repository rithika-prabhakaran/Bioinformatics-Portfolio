#--------------------------------------------------------------------------------------------------------------------
#PROJECT : DNA_ANALYZER
#AUTHOR : Rithika Prabhakaran
#LANGUAGE : PYTHON
#--------------------------------------------------------------------------------------------------------------------
#Version details
#--------------------------------------------------------------------------------------------------------------------
#V1 : Basic DNA ANALYZER
#    - User DNA Input
#    - DNA Length
#    - A ,T, G ,C Count
#    - Gc Percentage
#--------------------------------------------------------------------------------------------------------------------
#V2 : DNA Validation
#     - Read FASTA File
#     -DNA Report
#--------------------------------------------------------------------------------------------------------------------
#V3 : FASTA File Support
#     - Read FASTA File
#     - Skip Header
#     -Remove New Lines
#     - Convert to uppercase
#-------------------------------------------------------------------------------------------------------------------
#V4 : RNA Trascription
#    -DNA > RNA Conversion
#    - RNA Sequence added to report
#--------------------------------------------------------------------------------------------------------------------




#Version 3 - FASTA File reading code.------------------------------------------------------------------------------

file = open("brca1.fasta " , "r")  

file.readline()   # skip FASTA header

dna = file.read()  # Read the DNA Sequence

dna = dna.replace("\n" , "")   # Remove the newline character

dna = dna.strip()   #Remove extra space

file.close() #closing code- close file


#convert to upper case:
dna = dna.upper()
print("DNA Sequence is loaded : " , dna)

#Version 1 - Basic DNA Analysis--------------------------------------------------------------------------------------

# DNA length:
length = len(dna)
print("Length of your DNA Sequence: ", length)
# Count G
g_count = dna.count("G")
print("Number of G in your DNA Sequence: " , g_count)
# Count C
c_count = dna.count("C")
print("Number of C in your DNA Sequence: " , c_count)
# Count GC Percentage
gc_count = (g_count + c_count)
gc_percentage = (gc_count / length * 100)
print("GC Percentage of your Sequence: ", gc_percentage)
# Count A
a_count = dna.count("A")
print("Number of A in your sequence: ", a_count)
# Count T
t_count = dna.count("T")
print("Number of T in your sequence: ", t_count)

# Version 2 - DNA Validation----------------------------------------------------------------------------------------------------
# validation the nucleotide ATGC
valid = True
for letter in dna:
    
    if letter not in "ATGC":
        valid = False
    break
if valid:
    print("Valid DNA Sequrnce")

#Version 4 - RNA Transcription --------------------------------------------------------------------------------------------------
   #creating A>U , T>A , G>C , C>G

    rna = ""
    for base in dna :
        if base =="A":
            rna = rna + "U"
        elif base == "T":
            rna = rna + "A"
        elif base == "G":
            rna = rna +"C"
        elif base == "C":
            rna = rna + "G"
    print("RNA Sequence :" , rna)
        
# Version 2 - DNA Report Generator ---------------------------------------------------------------------------------------------
    file = open("dna_report.txt" ,"w")
    file.write(f"DNA Sequence: {dna}\n"
               f"Length: {length}\n"
               f"GC Percentage: {gc_percentage}\n"
               f"RNA Sequence :{rna}\n")
    file.close()
else:
    print("Invalid DNA Sequence") 
    
