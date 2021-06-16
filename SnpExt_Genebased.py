import sys
a = 1
with open(sys.argv[1], "r") as file:
    for line in file:
        geneid, chromosome, start, stop = line.split("\t")
        real_start = int(start) - 2000
        real_stop = int(stop) + 2000
        with open(sys.argv[2], "r") as f:
            for lines in f:
                CHROM, position, others = lines.split("\t", 2)
                if CHROM == chromosome:
                    if real_start <= int(position) and real_stop >= int(position):
                        print(geneid)
                        with open("extract.vcf", 'a') as file_object:
                            file_object.write(lines.rstrip())
                            file_object.write("\n")
                    else:
                        a = 2
