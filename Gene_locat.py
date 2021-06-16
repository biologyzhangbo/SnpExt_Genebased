import sys
idlist = []
print("Usage:python3 Gene_locat.py geneid.txt refgenome.gff gene_location.txt")
with open(sys.argv[1], "r") as idfile:
    for lines in idfile:
        idlist.append(lines.strip())
        print(idlist)
with open(sys.argv[2], "r") as gfffile:
    for line in gfffile:
        chromosome, x, y, start, stop, z, strand, v, idComplex = line.split("\t")
        ID1, ID2 = idComplex.split(";", 1)
        id1, id2 = ID1.split("=")
        if id2 in idlist:
            print(id2)
            with open(sys.argv[3], 'a') as file_object:
                file_object.write(id2+"\t"+chromosome+"\t"+start+"\t"+stop+"\t"+strand+"\n")
