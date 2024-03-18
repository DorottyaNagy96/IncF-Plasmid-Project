#Credits: adapted from Will Matlock's script 09/03/2024
import sys
from Bio import SeqIO

def split_fasta(input_file):
    # Read the input FASTA file
    records = SeqIO.to_dict(SeqIO.parse(input_file, "fasta"))

    # Split into individual files based on header names
    for header, sequence in records.items():
        output_filename = f"./all_contigs/{header}.fasta"
        SeqIO.write(sequence, output_filename, "fasta")
        print(f"Sequence with header '{header}' written to {output_filename}")

if __name__ == "__main__":
    # Check if the correct number of command-line arguments is provided
    if len(sys.argv) != 2:
        print("Usage: python script_assembly.py <input.fasta>")
        sys.exit(1)

    # Get the input file path from the command line
    input_file_path = sys.argv[1]

    # Call the function to split the FASTA file
    split_fasta(input_file_path)
