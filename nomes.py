with open("sequences.fasta") as file:
    fastas = file.readlines()
with open("nomes.csv", "w") as output:
    for fasta in fastas:
        if fasta.startswith(">"):
            output.write(fasta.strip(">"))