import pandas as pd
import matplotlib.pyplot as plt

file_path = 'C:/Users/noele/Documents/data analytics filesszzz/CompiledAISpeechVSNaturalFINAL.csv'

df = pd.read_csv(file_path)

# S1 AND S2 NATURALNESS EQUIVALENCE TEST
# Mean values for Naturalness scores of two groups
s1_mean = df['S1Naturalness'].mean()
s2_mean = df['S2Naturalness'].mean()

# Defining the equivalence margin
equivalence_margin = 0.5 

# Boxplots for the two groups
plt.boxplot([df['S1Naturalness'], df['S2Naturalness']], labels=['S1 Audio AI Generated Speech', 'S2 Audio Natural Speech'])

# Adding horizontal lines for equivalence margins
plt.axhline(y=s1_mean - equivalence_margin, color='blue', linestyle='--', label=f'Equivalence Margin (S1 Audio AI Generated Speech) = {equivalence_margin}')
plt.axhline(y=s1_mean + equivalence_margin, color='blue', linestyle='--')
plt.axhline(y=s2_mean - equivalence_margin, color='orange', linestyle='--', label=f'Equivalence Margin (S2 Audio Natural Speech) = {equivalence_margin}')
plt.axhline(y=s2_mean + equivalence_margin, color='orange', linestyle='--')

# Adding mean scores for each group with thicker lines and red color
plt.text(1, s1_mean, f'Mean: {s1_mean:.2f}', ha='left', va='center', fontsize=10, color='black')
plt.text(2, s2_mean, f'Mean: {s2_mean:.2f}', ha='left', va='center', fontsize=10, color='black')
plt.axhline(y=s1_mean, color='red', linestyle='-', linewidth=2)  # Mean line for S1 in red
plt.axhline(y=s2_mean, color='red', linestyle='-', linewidth=2)  # Mean line for S2 in red

# Labeling axes and adding title
plt.xlabel('Audio')
plt.ylabel('Naturalness Ratings')
plt.title('Naturalness Ratings Equivalence Test of S1 Audio AI Generated Speech and S2 Audio Natural Speech', pad=20)
plt.legend()

plt.show()

# S3 AND S4 NATURALNESS EQUIVALENCE TEST
s3_mean = df['S3Naturalness'].mean()
s4_mean = df['S4Naturalness'].mean()

equivalence_margin = 0.5  

plt.boxplot([df['S3Naturalness'], df['S4Naturalness']], labels=['S3 Audio AI Generated Speech', 'S4 Audio Natural Speech'])

plt.axhline(y=s3_mean - equivalence_margin, color='blue', linestyle='--', label=f'Equivalence Margin (S3 Audio AI Generated Speech) = {equivalence_margin}')
plt.axhline(y=s3_mean + equivalence_margin, color='blue', linestyle='--')
plt.axhline(y=s4_mean - equivalence_margin, color='orange', linestyle='--', label=f'Equivalence Margin (S4 Audio Natural Speech) = {equivalence_margin}')
plt.axhline(y=s4_mean + equivalence_margin, color='orange', linestyle='--')

plt.text(1, s3_mean, f'Mean: {s3_mean:.2f}', ha='left', va='center', fontsize=10, color='black')
plt.text(2, s4_mean, f'Mean: {s4_mean:.2f}', ha='left', va='center', fontsize=10, color='black')
plt.axhline(y=s3_mean, color='red', linestyle='-', linewidth=2)  
plt.axhline(y=s4_mean, color='red', linestyle='-', linewidth=2)  

plt.xlabel('Audio')
plt.ylabel('Naturalness Ratings')
plt.title('Naturalness Ratings Equivalence Test of S3 Audio AI Generated Speech and S4 Audio Natural Speech', pad=20)
plt.legend()

plt.show()

# S5 AND S6 NATURALNESS EQUIVALENCE TEST
s5_mean = df['S5Naturalness'].mean()
s6_mean = df['S6Naturalness'].mean()

equivalence_margin = 0.5 

plt.boxplot([df['S5Naturalness'], df['S6Naturalness']], labels=['S5 Audio Natural Speech', 'S6 Audio AI Generated Speech'])

plt.axhline(y=s5_mean - equivalence_margin, color='blue', linestyle='--', label=f'Equivalence Margin (S5 Audio Natural Speec) = {equivalence_margin}')
plt.axhline(y=s5_mean + equivalence_margin, color='blue', linestyle='--')
plt.axhline(y=s6_mean - equivalence_margin, color='orange', linestyle='--', label=f'Equivalence Margin (S6 Audio Audio AI Generated Speech) = {equivalence_margin}')
plt.axhline(y=s6_mean + equivalence_margin, color='orange', linestyle='--')

plt.text(1, s5_mean, f'Mean: {s5_mean:.2f}', ha='left', va='center', fontsize=10, color='black')
plt.text(2, s6_mean, f'Mean: {s6_mean:.2f}', ha='left', va='center', fontsize=10, color='black')
plt.axhline(y=s5_mean, color='red', linestyle='-', linewidth=2) 
plt.axhline(y=s6_mean, color='red', linestyle='-', linewidth=2)

plt.xlabel('Audio')
plt.ylabel('Naturalness Ratings')
plt.title('Naturalness Ratings Equivalence Test of S5 Audio Natural Speech and S6 Audio AI Generated Speech', pad=20)
plt.legend()

plt.show()