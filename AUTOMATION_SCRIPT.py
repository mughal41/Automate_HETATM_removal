import Bio 
from Bio.PDB import PDBList 
import subprocess 
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

pdb_id= input("Enter the PDB ID to be retrieved: ")
pdb_str = PDBList()
pd_b = pdb_str.retrieve_pdb_file(pdb_id, file_format="pdb", pdir= "F:\BIOINFORMATICS COMPUTING 2 PROJECT\PDB STR")

bin_for_removables = []
with open( pd_b, "r") as file:
    for line in file:
        if 'HETATM' in line:
            if 'ATP' in line:
                line = line.replace('ATP', 'LIG')
                bin_for_removables.append(line)
            if 'HOH' not in line:
                bin_for_removables.append(line)
        elif 'CONECT' not in line:
            bin_for_removables.append(line)
print("All Elements removed... Preparing to write file... ")

with open( pd_b, "w") as file:
    for line in  bin_for_removables:
        file.write(line)
print(" File written")
cmd = "start vmd pdb1fmw.ent -e execution.txt"
subprocess.Popen(cmd, shell=True)

data = pd.read_csv("interactions.csv")
array1 = np.array(data['LIG'])
array2 = np.array(data['Amino_acid'])

new = np.arange(len(array1))
sns.barplot(new, list(array2))

plt.xlabel('Ligand')
plt.ylabel('amino acid')
plt.title('Interactions of AA')
plt.legend(fontsize=10)
plt.savefig("Amino_acid.png")
plt.show()








