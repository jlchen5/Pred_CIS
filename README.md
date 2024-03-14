# Pred_CIS: Cis-Regulatory Element Prediction Script

This script is designed to predict cis-regulatory elements in a genomic sequence using the MEME software. It processes the output from MEME, extracts relevant information, and writes the results to a text file.

## Prerequisites

Before running this script, make sure you have the following installed:
- Python 3.x
- MEME Suite (available at http://meme-suite.org/)
- Necessary Python libraries: `subprocess`, `re`, `os`

These libraries are part of the Python Standard Library and should be available with Python installation.

## Usage

1. Place your genomic DNA sequence file in the same directory as the script. The file should be in FASTA format.

2. Modify the `genome_file` variable in the script if your genome file is named differently than the default `genome.fa`.

3. Run the script using Python:

   ```bash
   python cis_regulatory_element_prediction.py
