with open("nomes.csv") as file:
    arquivo = file.readlines()
with open("sequences.fasta",'r') as inp:
    fastas = inp.readlines()
with open("sequences2.fasta", 'w') as outp:
    for idx,fasta in enumerate(fastas):
        for nome in arquivo:
            if fasta.strip(">").strip("\n") == nome.strip("\n"):
                outp.write(">" + nome)
                outp.write(fastas[idx+1])
 