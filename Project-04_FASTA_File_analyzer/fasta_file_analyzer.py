from Bio import SeqIO
from Bio.Seq import Seq

records = SeqIO.parse("brca1_NM.fasta", "fasta")
report = open("analysis_report.txt", "w")

for record in records:

    sequence = record.seq
    length = len(sequence)

                                                                   # Base Counts
    a = sequence.count("A")
    t = sequence.count("T")
    g = sequence.count("G")
    c = sequence.count("C")

                                                                   # GC & AT Percentage
    gc = ((g + c) / length) * 100
    at = ((a + t) / length) * 100

                                                                   # Header
    print("=" * 55)
    print("    ------------ FASTA FILE ANALYZER ------------   ")
    print("=" * 55)

                                                                   # Basic Information
    print(f"Sequence ID        : {record.id}")
    print(f"Description        : {record.description}")
    print(f"Length             : {length} bp")
    print(f"Sequence Preview   : {sequence[:50]}...")

                                                                   # Base Counts
    print(f"Number of A        : {a}")
    print(f"Number of T        : {t}")
    print(f"Number of G        : {g}")
    print(f"Number of C        : {c}")

                                                                   # GC & AT %
    print(f"GC %               : {gc:.2f}%")
    print(f"AT %               : {at:.2f}%")

    
                                                                   # FILTERING
    if gc >= 50:

        print("Filter Status      : PASSED (GC >= 50%)")

    else:

        print("Filter Status      : FAILED (GC < 50%)")

   
                                                                   # DNA Validation
    valid_bases = "ATGC"
    invalid = []
    for base in sequence:
        if base not in valid_bases:
            invalid.append(base)

    if len(invalid) == 0:
        print("Sequence Status    : Valid DNA Sequence")
    else:
        print("Sequence Status    : Invalid DNA Sequence")
        print("Invalid Bases      :", invalid)

                                                                    # Motif Search
    motif = input("\nEnter DNA Motif to Search : ").upper()

    if motif in sequence:
        print("Motif Found!")
        print("Occurrences :", sequence.count(motif))
    else:
        print("Motif Not Found!")


                                                                     #Transcription

    print("\nTranscription (DNA → RNA)")

    rna = sequence.transcribe()

    print("RNA Preview :", rna[:50], "...")

                                                                      #Translation

    print("\nTranslation (RNA → Protein)")

    Protein = rna.translate()

    print("Protein Preview :", Protein[:50], "...")



                                                                    # Reverse Complement
    print("\nReverse Complement Preview")

    reverse = sequence.reverse_complement()

    print(reverse[:50], "...")

    print("\n")


    
                                                                     # START CODON DETECTION

    print("\n========== START CODON DETECTION ==========")

    start_codon = "ATG"
    start_positions = []

    for i in range(len(sequence) - 2):
        if sequence[i:i+3] == start_codon:
            start_positions.append(i + 1)

    print(f"Total Start Codons : {len(start_positions)}")

    if len(start_positions) > 0:
        print("First 10 Positions :", start_positions[:10])

        if len(start_positions) > 10:
            print(f"... and {len(start_positions)-10} more positions")
    else:
        print("No Start Codon Found")



                                                                       # STOP CODON DETECTION


    print("\n========== STOP CODON DETECTION ==========")

    stop_codons = ["TAA", "TAG", "TGA"]

    total_stop = 0

    for codon in stop_codons:

        stop_positions = []

        for i in range(len(sequence) - 2):
            if sequence[i:i+3] == codon:
                stop_positions.append(i + 1)

        print(f"\nStop Codon : {codon}")
        print(f"Count       : {len(stop_positions)}")

        total_stop += len(stop_positions)

        if len(stop_positions) > 0:
            print("First 10 Positions :", stop_positions[:10])

            if len(stop_positions) > 10:
                print(f"... and {len(stop_positions)-10} more positions")
        else:
            print("Not Found")

    print("\n--------------------------------------")
    print(f"Total Stop Codons : {total_stop}")
    print("--------------------------------------")


    report.write("=" * 50 + "\n")
    report.write("PROJECT 04 - FASTA FILE ANALYZER\n")
    report.write("=" * 50 + "\n")

    report.write(f"Sequence ID : {record.id}\n")
    report.write(f"Description : {record.description}\n")
    report.write(f"Length : {length} bp\n")

    report.write(f"A : {a}\n")
    report.write(f"T : {t}\n")
    report.write(f"G : {g}\n")
    report.write(f"C : {c}\n")

    report.write(f"GC % : {gc:.2f}%\n")
    report.write(f"AT % : {at:.2f}%\n")

    report.write(f"Start Codons : {len(start_positions)}\n")
    report.write(f"Total Stop Codons : {total_stop}\n")

    report.write("\n")
report.close()
print("\nAnalysis Report Generated Sucessfully!")  

                                                                     

    

    

