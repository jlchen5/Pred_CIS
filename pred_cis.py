import subprocess

# 基因组序列文件
genome_file = "genome.fa"
# 顺势调控元件预测结果输出文件
output_file = "cis_elements.txt"

# 运行MEME软件预测顺势调控元件
meme_command = ["meme", genome_file, "-dna", "-nostatus", "-oc", "meme_output"]
subprocess.run(meme_command)

# 解析预测结果文件
with open("meme_output/meme.html") as f:
    html_text = f.read()
    # 提取元素位置信息
    start_pos_list = re.findall(r'Start = (\d+)', html_text)
    end_pos_list = re.findall(r'End = (\d+)', html_text)
    # 提取元素序列信息
    seq_list = re.findall(r'Strand=.*\n(.*)\n.*\n.*\n', html_text, flags=re.DOTALL)

# 将结果输出到文件
with open(output_file, "w") as f:
    for i in range(len(start_pos_list)):
        f.write(f"{start_pos_list[i]}\t{end_pos_list[i]}\t{seq_list[i]}\n")
