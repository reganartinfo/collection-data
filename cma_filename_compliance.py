import csv, re

def fileRename(csv_input, csv_output):
    with open(csv_output,'w') as f_out:
        writer = csv.writer(f_out)

        with open(csv_input,'r') as f_in:
            reader = csv.reader(f_in)
            header = next(reader)
            
            for row in reader:
                accession_num = row[6]
                separator = "-"
                row[7] = separator.join(re.split('\.',accession_num)) + ".jpg"
                writer.writerow(row)
                
fileRename('cma_batch_prep.csv','cma_batch_manifest.csv')