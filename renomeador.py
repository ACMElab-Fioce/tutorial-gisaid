with open("nomes.csv") as file:
    arquivo = file.readlines()
    for nome in arquivo[1:]:
        nome.split(";")

with open("all_sequences.fasta",'r') as file:
    fastas = file.readlines()

with open("all_sequences2.fasta", 'w') as outp:
    for c in fastas:
        if c.startswith(">"): 
            for nome in arquivo[1:]:
                if c.strip(">").strip("\n") == nome.split(";")[0].strip("\t"):
                    outp.write(">" + nome.split(";")[1])
        else:
            outp.write(c)

 