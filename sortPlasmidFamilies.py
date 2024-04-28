#Credits: written with the help of ChatGPT 09/03/2024
import os
from Bio import SeqIO

def separate_fasta(input_directory, output_directory, families_directory):
    # Iterate over all plasmid family directories
    for family_name in os.listdir(families_directory):
        family_directory = os.path.join(families_directory, family_name)

        # Create output directory if it doesn't exist
        output_family_directory = os.path.join(output_directory, family_name)
        os.makedirs(output_family_directory, exist_ok=True)

        # Find the accession list file for the current family
        accession_list_file = None
        for filename in os.listdir(family_directory):
            if filename.endswith('_plasmid_accessions.txt'):
                accession_list_file = os.path.join(family_directory, filename)
                break

        if accession_list_file:
            # Read accession numbers from the family file
            with open(accession_list_file, 'r') as f:
                accession_list = f.read().splitlines()
        # Process each FASTA file in the input directory
      
        for filename in os.listdir(input_directory):
            if filename.endswith('.fasta'):
                input_file_path = os.path.join(input_directory, filename)
                for record in SeqIO.parse(input_file_path, 'fasta'):
                    accession_number = record.id.split('.')[0]  # Extract accession number
                    accession_list_file = os.path.join(family_directory, f'{family_name}.txt')
                    if any(accession_number in accession_list_item for accession_list_item in accession_list):
                            output_file_path = os.path.join(output_family_directory, filename)
                            SeqIO.write(record, output_file_path, 'fasta')

if __name__ == "__main__":
    input_directory = 'all_contigs/'  # Provide the path to the directory containing the input FASTA files
    output_directory = 'plasmid_families/'  # Provide the path to the directory where output directories will be created
    families_directory = 'plasmid_families/'  # Provide the path to the directory containing the family directories

    separate_fasta(input_directory, output_directory, families_directory)