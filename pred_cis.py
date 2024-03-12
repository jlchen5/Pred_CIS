import subprocess
import re
import os

# Define file paths
genome_file = "genome.fa"
output_file = "cis_elements.txt"

# Run MEME software to predict cis-regulatory elements
meme_command = ["meme", genome_file, "-dna", "-nostatus", "-oc", "meme_output"]
try:
    subprocess.run(meme_command, check=True)  # Ensure the command runs successfully
except subprocess.CalledProcessError as e:
    print(f"MEME command failed with exit status {e.returncode}")
    exit(1)

# Check if the output directory and file exist
meme_output_html = "meme_output/meme.html"
if not os.path.exists(meme_output_html):
    print(f"Expected output file {meme_output_html} not found")
    exit(1)

# Parse prediction result file
with open(meme_output_html) as f:
    html_text = f.read()

# Extract element position information
start_pos_list = re.findall(r'Start = (\d+)', html_text)
end_pos_list = re.findall(r'End = (\d+)', html_text)
# Extract element sequence information
seq_list = re.findall(r'Strand=.*\n(.*)\n.*\n.*\n', html_text, flags=re.DOTALL)

# Ensure all lists have the same length to avoid IndexError
if not (len(start_pos_list) == len(end_pos_list) == len(seq_list)):
    print("Error: Mismatched information in output data.")
    exit(1)

# Write results to file
with open(output_file, "w") as f:
    for start, end, seq in zip(start_pos_list, end_pos_list, seq_list):
        f.write(f"{start}\t{end}\t{seq.strip()}\n")  # Use strip() to remove any leading/trailing whitespace from sequences
