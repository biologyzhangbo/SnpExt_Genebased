The first script  is Gene_locat.py.  
The script requires two files, one is the processed GFF file, and the other is the gene id file.  
The processed GFF file can be obtained through the following ways:  
First, download the annotation file of the target genome from phytozome, and then run the following command in linux:  
`grep “gene” refgenome.gff> gene.refgenome.gff`  
A usable gff file should be same as the following format:  
  Chr01 phytozomev10 gene 1951 2616 . + . ID=Sobic.001G000100.v3.1;Name=Sobic.001G000100;ancestorIdentifier=Sobic.001G000100.v2.1 
  Chr01 phytozomev10 gene 11180 14899 . - . ID=Sobic.001G000200.v3.1;Name=Sobic.001G000200;ancestorIdentifier=Sobic.001G000200.v2.1  
  Chr01 phytozomev10 gene 23399 24152 . - . ID=Sobic.001G000300.v3.1;Name=Sobic.001G000300;ancestorIdentifier=Sobic.001G000300.v2.1  
  Chr01 phytozomev10 gene 22391 42443 . - . ID=Sobic.001G000400.v3.1;Name=Sobic.001G000400;ancestorIdentifier=Sobic.001G000400.v2.1  

The gene id file should have one gene name per line as follows:  
Sobic.001G355700  
Sobic.002G484000  
Sobic.005G821200  
...  
  
Then, run the command as follows:  
`python Gene_locat.py geneidfile gene.refgenome.gff genelocationfile`  

The second script is SnpExt_Genebased.py.  

The script requires two files, one is the processed VCF file, and the other is the gene location file.  
The processed VCF file can be obtained through the following ways:  
`grep "#" VCFfile > title`  
`grep -v "#" VCFfile > processed.VCFfile`  
The gene location file can be produced by Gene_locat.py.  
Second, run the command as following:  
`python SnpExt_Genebased.py genelocationfile processed.VCFfile`  
`cat title extract.vcf > extracted.vcf`  
`rm extract.vcf`  
  
Contact: bozhang@ibcas.ac.cn
